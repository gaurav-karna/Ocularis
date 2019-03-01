using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Foundation;
using Windows.Graphics.Imaging;
using Windows.Media.Capture;
using Windows.Media.MediaProperties;
using Windows.Storage;
using Windows.Storage.Pickers;
using Windows.Storage.Streams;

namespace Ocularis.Sensors.Camera
{
    class CameraDriver
    {
        public async Task<CapturedPhoto> TakeShot()
        {
            var mediaCapture = new MediaCapture();

            try
            {
                await mediaCapture.InitializeAsync();
                var lowLagCapture = await mediaCapture.PrepareLowLagPhotoCaptureAsync(ImageEncodingProperties.CreateUncompressed(MediaPixelFormat.Bgra8));

                var capturedPhoto = await lowLagCapture.CaptureAsync();

                await lowLagCapture.FinishAsync();

                return capturedPhoto;
            }
            catch (Exception)
            {
                throw;
            }
        }

        public async Task<StorageFile> Save(CapturedPhoto capturedPhoto,StorageFolder storageFolder)
        {
            var softwareBitmap = capturedPhoto.Frame.SoftwareBitmap;
            StorageFile outputFile = await storageFolder.CreateFileAsync("image.jpg",CreationCollisionOption.GenerateUniqueName);

            await SaveSoftwareBitmapToFile(softwareBitmap, outputFile);

            return outputFile;
        }

        private async Task SaveSoftwareBitmapToFile(SoftwareBitmap softwareBitmap, StorageFile outputFile)
        {
            using (IRandomAccessStream stream = await outputFile.OpenAsync(FileAccessMode.ReadWrite))
            {
                var propertySet = new BitmapPropertySet();
                var qualityValue = new BitmapTypedValue(1.0,PropertyType.Single);
                propertySet.Add("ImageQuality", qualityValue);

                var encoder = await BitmapEncoder.CreateAsync(BitmapEncoder.JpegEncoderId,stream,propertySet);
                encoder.SetSoftwareBitmap(softwareBitmap);

                try
                {
                    await encoder.FlushAsync();
                }
                catch (Exception err)
                {
                    const int WINCODEC_ERR_UNSUPPORTEDOPERATION = unchecked((int)0x88982F81);
                    switch (err.HResult)
                    {
                        case WINCODEC_ERR_UNSUPPORTEDOPERATION:
                            // If the encoder does not support writing a thumbnail, then try again
                            // but disable thumbnail generation.
                            encoder.IsThumbnailGenerated = false;
                            break;
                        default:
                            throw;
                    }
                }
            }
        }

    }
}
