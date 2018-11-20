using Microsoft.Azure.CognitiveServices.Vision.ComputerVision.Models;
using Microsoft.Azure.CognitiveServices.Vision.Face;
using Microsoft.Azure.CognitiveServices.Vision.Face.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Storage;

namespace Ocularis.Capabilities.Remote.Face
{
    class FaceAnalyzer
    {
        private static readonly FaceAttributeType[] _faceAttributes = 
        {
            FaceAttributeType.Age,
            FaceAttributeType.Gender,
            FaceAttributeType.Smile,
            FaceAttributeType.Emotion
        };

        private string _subscriptionKey;
        private string _endPoint;

        public FaceAnalyzer(string subscriptionKey, string endPoint)
        {
            _subscriptionKey = subscriptionKey;
            _endPoint = endPoint;
        }

        public async Task FindFaces(StorageFile imageFile)
        {
            using (var faceClient = new FaceClient(new ApiKeyServiceClientCredentials(_subscriptionKey), new System.Net.Http.DelegatingHandler[] { }))
            {
                faceClient.Endpoint = _endPoint;
                await DetectLocalAsync(faceClient, imageFile);
            }
        }

        // Detect faces in a local image
        private static async Task DetectLocalAsync(FaceClient faceClient, StorageFile imageFile)
        {
            try
            {
                using (var imageStream = await imageFile.OpenStreamForReadAsync())
                {
                    var faceList = await faceClient.Face.DetectWithStreamAsync(imageStream, true, false, _faceAttributes);
                    GetFaceAttributes(faceList);
                }
            }
            catch (APIErrorException e)
            {
            }
        }

        private static string GetFaceAttributes(IList<DetectedFace> faceList)
        {
            string attributes = string.Empty;

            foreach (DetectedFace face in faceList)
            {
                double? age = face.FaceAttributes.Age;
                string gender = face.FaceAttributes.Gender.ToString();
                attributes += gender + " " + age + "   ";
            }

            return attributes;
        }

    }
}
