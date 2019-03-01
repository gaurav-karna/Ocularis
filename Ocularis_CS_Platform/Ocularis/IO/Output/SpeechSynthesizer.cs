using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Media.Core;
using Windows.Media.Playback;
using Windows.Media.SpeechSynthesis;

namespace Ocularis.IO.Output
{
    public static class SpeechSynthesizer
    {

        public static async Task Read(string text, MediaPlayer mediaPlayer)
        {
             var synth = new Windows.Media.SpeechSynthesis.SpeechSynthesizer();

            using (var stream = await synth.SynthesizeTextToStreamAsync(text))
            {
                mediaPlayer.Source = MediaSource.CreateFromStream(stream, stream.ContentType);
                mediaPlayer.Play();
            }
        }

    }
}
