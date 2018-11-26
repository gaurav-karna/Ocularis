using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.CognitiveServices.Language.LUIS.Runtime.Models;
using Ocularis.Capabilities.Remote.Bing.ProjectAnswerSearch;

namespace Ocularis.Capabilities.Remote.LUIS.IntentHandlers
{
    [LuisIntent("InstantAnswer.Question")]
    class InstantAnswerQuestionIntentHandler : IIntentHandler
    {
        public async Task<string> Handle(LuisResult param)
        {
            var connector = new ProjectAnswerSearchConnector(AppConfiguration.ProjectAnswerSearchSubscriptionKey, AppConfiguration.ProjectAnswerSearchEndpoint);

            var question = param.Entities.First(q=>q.Type== "InstantQuestion").Entity;
            var answer =  await connector.Answer(question);

            return GenerateResult(answer);
        }

        private string GenerateResult(InstantAnswer answer)
        {
            if (answer.WebPages.Value.Length == 0)
                return "Sorry, i couldn't find anything";

            var result = $"Let me share my findings with you. I've found {answer.WebPages.Value.Length} different sources.";
            result += $"First source says that, {answer.WebPages.Value.ElementAt(0).Snippet}";

            if (answer.WebPages.Value.Length == 1)
                return result;

            result += $"Second source says that, {answer.WebPages.Value.ElementAt(1).Snippet}";

            if (answer.WebPages.Value.Length == 2)
                return result;

            result += $"Third source says that, {answer.WebPages.Value.ElementAt(2).Snippet}";

            if (answer.WebPages.Value.Length == 3)
                return result;

            result += $"Fourth source says that, {answer.WebPages.Value.ElementAt(3).Snippet}";

            if (answer.WebPages.Value.Length == 4)
                return result;

            result += $"And last source says that, {answer.WebPages.Value.ElementAt(4).Snippet}";

            return result;
        }
    }
}
