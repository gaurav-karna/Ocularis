using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ocularis.Capabilities.Remote.LUIS.IntentHandlers
{
    public interface IIntentHandler
    {
        Task<string> Handle(LuisResult param);
    }
}
