using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ocularis.Capabilities.Remote.LUIS.IntentHandlers
{
    [AttributeUsage(AttributeTargets.Class)
]
    public class LuisIntentAttribute: Attribute
    {
        public string Name { get; set; }
        public LuisIntentAttribute(string name)
        {
            Name = name;
        }
    }
}
