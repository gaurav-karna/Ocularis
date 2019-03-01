using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Windows.Storage;

namespace Ocularis
{
    public static class AppConfiguration
    {
        private readonly static ApplicationDataContainer _localSettings = ApplicationData.Current.LocalSettings;
        public static string LuisApiApplicationId
        {
            get
            {
                return _localSettings.Values["luis.applicationid"].ToString();
            }
            set
            {
                _localSettings.Values["luis.applicationid"] = value;
            }
        }

        public static string LuisApiSubscriptionKey
        {
            get
            {
                return _localSettings.Values["luis.subscriptionKey"].ToString();
            }
            set
            {
                _localSettings.Values["luis.subscriptionKey"] = value;
            }
        }

        public static string LuisApiEndPoint
        {
            get
            {
                return _localSettings.Values["luis.endPoint"].ToString();
            }
            set
            {
                _localSettings.Values["luis.endPoint"] = value;
            }
        }

        public static string FaceApiSubscriptionKey
        {
            get
            {
                return _localSettings.Values["face.subscriptionKey"].ToString();
            }
            set
            {
                _localSettings.Values["face.subscriptionKey"] = value;
            }
        }

        public static string FaceApiEndPoint
        {
            get
            {
                return _localSettings.Values["face.endPoint"].ToString();
            }
            set
            {
                _localSettings.Values["face.endPoint"] = value;
            }
        }

        public static string VisionApiSubscriptionKey
        {
            get
            {
                return _localSettings.Values["vision.subscriptionKey"].ToString();
            }
            set
            {
                _localSettings.Values["vision.subscriptionKey"] = value;
            }
        }

        public static string VisionApiEndPoint
        {
            get
            {
                return _localSettings.Values["vision.endPoint"].ToString();
            }
            set
            {
                _localSettings.Values["vision.endPoint"] = value;
            }
        }

        public static string ProjectAnswerSearchSubscriptionKey
        {
            get
            {
                return _localSettings.Values["projectanswersearch.subscriptionKey"].ToString();
            }
            set
            {
                _localSettings.Values["projectanswersearch.subscriptionKey"] = value;
            }
        }
        public static string ProjectAnswerSearchEndpoint
        {
            get
            {
                return _localSettings.Values["projectanswersearch.endPoint"].ToString();
            }
            set
            {
                _localSettings.Values["projectanswersearch.endPoint"] = value;
            }
        }
    }
}
