using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Ocularis.Capabilities.Remote.Bing.ProjectAnswerSearch
{
    public class ProjectAnswerSearchConnector
    {
        private string _subscriptionKey;
        private string _endPoint;

        public ProjectAnswerSearchConnector(string subscriptionKey, string endPoint)
        {
            _subscriptionKey = subscriptionKey;
            _endPoint = endPoint;
        }

        public async Task<InstantAnswer> Answer(string question)
        {
            return await BingLocalSearch(question);
        }

        private async Task<InstantAnswer> BingLocalSearch(string searchQuery)
        {
            var uriQuery = _endPoint + "?q=" + Uri.EscapeDataString(searchQuery) + "&mkt=en-us&count=5&offset=0&safesearch=Off";

            using (var httpClient = new HttpClient())
            {
                httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", _subscriptionKey);
                var httpResponseContent = await httpClient.GetStringAsync(uriQuery);
                var findings = JsonConvert.DeserializeObject<InstantAnswer>(httpResponseContent);
                return findings;
            }

        }
    }

    public class InstantAnswer
    {
        public string _type { get; set; }
        public Querycontext QueryContext { get; set; }
        public Webpages WebPages { get; set; }
        public Rankingresponse RankingResponse { get; set; }
    }

    public class Querycontext
    {
        public string OriginalQuery { get; set; }
    }

    public class Webpages
    {
        public string WebSearchUrl { get; set; }
        public int TotalEstimatedMatches { get; set; }
        public Value[] Value { get; set; }
    }

    public class Value
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Url { get; set; }
        public About[] About { get; set; }
        public bool IsFamilyFriendly { get; set; }
        public string DisplayUrl { get; set; }
        public string Snippet { get; set; }
        public Snippetattribution SnippetAttribution { get; set; }
        public DateTime DateLastCrawled { get; set; }
        public Richcaption RichCaption { get; set; }
        public string Language { get; set; }
        public bool IsNavigational { get; set; }
        public Deeplink[] DeepLinks { get; set; }
    }

    public class Snippetattribution
    {
        public License license { get; set; }
        public string licenseNotice { get; set; }
    }

    public class License
    {
        public string name { get; set; }
        public string url { get; set; }
    }

    public class Richcaption
    {
        public string _type { get; set; }
        public int RowCount { get; set; }
        public int ColumnCount { get; set; }
        public string[] Header { get; set; }
        public Row[] Rows { get; set; }
        public Seemoreurl SeeMoreUrl { get; set; }
        public Section[] Sections { get; set; }
    }

    public class Seemoreurl
    {
        public string Text { get; set; }
        public string url { get; set; }
    }

    public class Row
    {
        public Cell[] cells { get; set; }
    }

    public class Cell
    {
        public string _type { get; set; }
        public string text { get; set; }
        public string url { get; set; }
    }

    public class Section
    {
        public string _type { get; set; }
        public string Name { get; set; }
        public string SiteName { get; set; }
        public string Description { get; set; }
        public Tabulardata TabularData { get; set; }
    }

    public class Tabulardata
    {
        public Row1[] Rows { get; set; }
    }

    public class Row1
    {
        public Cell1[] cells { get; set; }
    }

    public class Cell1
    {
        public string _type { get; set; }
        public string text { get; set; }
        public string url { get; set; }
    }

    public class About
    {
        public string name { get; set; }
    }

    public class Deeplink
    {
        public string name { get; set; }
        public string url { get; set; }
        public string snippet { get; set; }
    }

    public class Rankingresponse
    {
        public Mainline mainline { get; set; }
        public Sidebar sidebar { get; set; }
    }

    public class Mainline
    {
        public Item[] items { get; set; }
    }

    public class Item
    {
        public string answerType { get; set; }
        public int resultIndex { get; set; }
        public Value1 value { get; set; }
    }

    public class Value1
    {
        public string id { get; set; }
    }

    public class Sidebar
    {
        public Item1[] items { get; set; }
    }

    public class Item1
    {
        public string answerType { get; set; }
    }
}
