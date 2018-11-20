using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Media.SpeechRecognition;

namespace Ocularis.IO.Input
{
    public static class SpeechRecognizer
    {
        public static async Task<string> GetText()
        {
            var language = new Windows.Globalization.Language("en-US");
            using (var speechRecognizer = new Windows.Media.SpeechRecognition.SpeechRecognizer(language))
            {
                await speechRecognizer.CompileConstraintsAsync();

                speechRecognizer.StateChanged += SpeechRecognizerStateChangedHandler; ;

                var result = await speechRecognizer.RecognizeAsync();

                if (result.Status == SpeechRecognitionResultStatus.Success)
                {
                    return result.Text;
                }
                else
                {
                    // we need to control confidence and other factors
                }
            }
                
            return null;
        }

        private static void SpeechRecognizerStateChangedHandler(Windows.Media.SpeechRecognition.SpeechRecognizer sender, SpeechRecognizerStateChangedEventArgs args)
        {
        }
    }
}
