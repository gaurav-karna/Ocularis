using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime.Models;
using Microsoft.Azure.CognitiveServices.Vision.ComputerVision.Models;
using Ocularis.Capabilities.Remote.Face;
using Ocularis.Sensors.Camera;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Storage;

namespace Ocularis.Capabilities.Remote.LUIS.IntentHandlers
{
    [LuisIntent("Vision.Describe")]
    public class VisionDescribeIntentHandler : IIntentHandler
    {
        public async Task<string> Handle(LuisResult param)
        {
            var cameraDriver = new CameraDriver();
            var capturedPhoto = await cameraDriver.TakeShot();
            var storageFile  = await cameraDriver.Save(capturedPhoto, ApplicationData.Current.TemporaryFolder);

            var imageAnalyzer = new ImageAnalyzer(AppConfiguration.VisionApiSubscriptionKey,AppConfiguration.VisionApiEndPoint);
            var imageAnalysis = await imageAnalyzer.Describe(storageFile);

            var description = GetDescription(imageAnalysis);

            return description;
        }

        private string GetDescription(ImageAnalysis imageAnalysis)
        {
            return imageAnalysis.Description.Captions.First().Text;
        }
    }
}
