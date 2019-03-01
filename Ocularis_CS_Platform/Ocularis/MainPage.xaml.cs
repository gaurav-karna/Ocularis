using Ocularis.IO;
using Ocularis.IO.Input;
using Ocularis.LUIS;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Devices.Gpio;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.Graphics.Imaging;
using Windows.Media.Capture;
using Windows.Media.Core;
using Windows.Media.MediaProperties;
using Windows.Media.Playback;

using Windows.Storage;
using Windows.Storage.Pickers;
using Windows.Storage.Streams;
using Windows.UI.Core;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

namespace Ocularis
{
    public sealed partial class MainPage : Page
    {
        private readonly MediaPlayer _speechPlayer;
        private Buddy _buddy;

        public MainPage()
        {
            _speechPlayer = new MediaPlayer();
            InitializeComponent();
            _buddy = new Buddy(_speechPlayer);


            AppConfiguration.LuisApiSubscriptionKey = "3e2934014f074071b2e976fa07a6b3b8";
            AppConfiguration.LuisApiEndPoint = "https://westus.api.cognitive.microsoft.com/";
            AppConfiguration.LuisApiApplicationId = "34cba600-73d1-45de-b30d-a80156854438";
            AppConfiguration.FaceApiSubscriptionKey = "d5c5af33cd604b78bc6f85de2600549b";
            AppConfiguration.FaceApiEndPoint = "https://westcentralus.api.cognitive.microsoft.com";
            AppConfiguration.VisionApiSubscriptionKey = "c629cf862be745d49e5f1e1ba5273d4b";
            AppConfiguration.VisionApiEndPoint = "https://westcentralus.api.cognitive.microsoft.com";
            AppConfiguration.ProjectAnswerSearchSubscriptionKey= "6c8eb7b5c0964e61930c5fa4ed693900";
            AppConfiguration.ProjectAnswerSearchEndpoint = "https://api.labs.cognitive.microsoft.com/answersearch/v7.0/search";
        }

        private async void  Button_Click(object sender, RoutedEventArgs e)
        {
            await _buddy.Help();
        }

    }
}
