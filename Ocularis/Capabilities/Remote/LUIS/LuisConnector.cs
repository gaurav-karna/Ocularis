using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime;
using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime.Models;
using Newtonsoft.Json;

namespace Ocularis.LUIS
{
    public class LuisConnector
    {
        private string _subscriptionKey;
        private string _endPoint;
        private string _applicationId;

        public LuisConnector(string subscriptionKey, string endPoint,string applicationId)
        {
            _subscriptionKey = subscriptionKey;
            _endPoint = endPoint;
            _applicationId = applicationId;
        }

        public async Task<LuisResult> PredictAsync(string text)
        {
            var client = new LUISRuntimeClient(new ApiKeyServiceClientCredentials(_subscriptionKey));
            client.Endpoint = _endPoint;

            try
            {
                var result = await client.Prediction.ResolveAsync(_applicationId, text);
                return result;
            }
            catch (Exception e)
            {
                throw;
            }
        }
    }
}
