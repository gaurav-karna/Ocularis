using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime.Models;
using Ocularis.Capabilities.Remote.LUIS.IntentHandlers;
using Ocularis.IO.Input;
using Ocularis.IO.Output;
using Ocularis.LUIS;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Media.Playback;
using Windows.Storage;

namespace Ocularis.IO
{
    public class Buddy
    {
        private ApplicationDataContainer _localSettings = ApplicationData.Current.LocalSettings;
        private MediaPlayer _voicePlayer;
        private Dictionary<string, Type> _intentHandlersDict;

        public Buddy(MediaPlayer voicePlayer)
        {
            _voicePlayer = voicePlayer;
            Init();
        }

        private void Init()
        {
            var intentHandlers = from a in AppDomain.CurrentDomain.GetAssemblies().AsParallel()
                                        from t in a.GetTypes()
                                        let attributes = t.GetCustomAttributes(typeof(LuisIntentAttribute), true)
                                        where attributes != null && attributes.Length > 0
                                        select new { Type = t, Attributes = attributes.Cast<LuisIntentAttribute>() };


            _intentHandlersDict = intentHandlers.ToDictionary(q => q.Attributes.First().Name, q => q.Type);
        }

        public async Task Help()
        {
            var orderText = await SpeechRecognizer.GetText();
            var connector = new LuisConnector(AppConfiguration.LuisApiSubscriptionKey, AppConfiguration.LuisApiEndPoint, AppConfiguration.LuisApiApplicationId);
            var luisResult = await connector.PredictAsync(orderText);
            var intentHandler = GetIntentHandler(luisResult);
            var resultText = await intentHandler.Handle(luisResult);
            await SpeechSynthesizer.Read(resultText, _voicePlayer);
        }

        private IIntentHandler GetIntentHandler(LuisResult luisResult)
        {
            var type = _intentHandlersDict[luisResult.TopScoringIntent.Intent];
            return (IIntentHandler)Activator.CreateInstance(type);
        }
    }
}
