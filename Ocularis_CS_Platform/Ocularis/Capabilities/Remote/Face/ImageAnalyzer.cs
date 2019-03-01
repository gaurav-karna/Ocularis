using Microsoft.Azure.CognitiveServices.Vision.ComputerVision;
using Microsoft.Azure.CognitiveServices.Vision.ComputerVision.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Windows.Storage;

namespace Ocularis.Capabilities.Remote.Face
{
    class ImageAnalyzer
    {

        private static readonly VisualFeatureTypes[] _visualFeatures = 
        {
            VisualFeatureTypes.Description,
            VisualFeatureTypes.Faces
        };

        private readonly string _subscriptionKey;
        private readonly string _endPoint;

        public ImageAnalyzer(string subscriptionKey, string endPoint)
        {
            _subscriptionKey = subscriptionKey;
            _endPoint = endPoint;
        }

        public async Task<ImageAnalysis> Describe(StorageFile imageFile)
        {
            using (var computerVision = new ComputerVisionClient(new ApiKeyServiceClientCredentials(_subscriptionKey), new DelegatingHandler[] { }))
            {
                computerVision.Endpoint = _endPoint;
                return await AnalyzeLocalAsync(computerVision, imageFile);
            }
        }

        private static async Task<ImageAnalysis> AnalyzeLocalAsync(ComputerVisionClient computerVision, StorageFile imageFile)
        {
            using (Stream imageStream = File.OpenRead(imageFile.Path))
            {
                var analysis = await computerVision.AnalyzeImageInStreamAsync(imageStream, _visualFeatures);
                return analysis;
            }
        }
    }
}
