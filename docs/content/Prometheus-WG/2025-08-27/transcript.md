SIG: Prometheus WG
Date: 2025-08-27
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Arve Knudsen** 00:48 Hello.
**Owen Williams (he/she)** 00:51 Hello.
**Arthur Silva Sens** 01:45 Hello!
**Arve Knudsen** 01:50 Bye.
**Arthur Silva Sens** 02:17 Hey, whoever… School organizing the docs. Thanks.
Let me ping Gregor.
But he has the first point, he's not here.
I'll just move Gregor behind.
Hey, I have the first point, but if people have other things to discuss, feel free to add to the agenda.
My topic is… about a PR that I have open in the Collector.
It's, several months ago, we did a change to the spec, saying that scope attributes
Should become labels, instead, like, basically making them identify, instead of exposing them in a metric called Telescope info.
I… we already implemented this change in the Go SDK exporter, in the Prometheus… …
Prometheus exporter in the collector, and also in the Prometheus OTLP endpoint.
But we still haven't done it in the receiver.
So if people are…
compliant to this change, like, if they are using the Go SDK, or the Prometus Exporter, or the Prometus
Export in the collector to send metrics.
the receiver cannot understand this format yet. We'll parse it in a different way.
Well, this PR is open for quite a while, waiting for reviews. I just noticed that David
review it while I was in another meeting.
But if anybody else has the time to take a look, That would be awesome.
If nobody has any questions, we can move to the other topic.
But I still don't see Gregor, though.
**Owen Williams (he/she)** 06:01 I'm just looking over my… Various lists, and if there's anything…
I have questions on, and I don't think so.
**Arthur Silva Sens** 06:12 Right?
**Owen Williams (he/she)** 06:13 Things have been…
I guess we could… we could just talk, do a little status and what… sort of what's left for the stuff that you and I have been working on, because I know, like, there was the config API stuff.
So let's just do this.
… So, my PR has, 3 approvals, which is great, so just have to, …
Do the last nits, and then that should go in… … Let me just link that.
And then, Arthur, on your side… …
What, yeah, what's on your list for that sort of bucket of work?
**Arthur Silva Sens** 07:13 8.
I…
When we suggested the Go SDK to migrate to the OTLP translator package, they requested us to eventually release 1.0 and declare the package stable.
So… I think my priority here is to make the…
The breaking changes that we need to do before… declaring 1.0.
That would be that PR with the multiple underscores. I saw that Arif left a review.
Which I plan to… to address today.
And yeah, that key prefix…
Which is unfortunate, like, it literally does nothing, but we need to keep for backwards compatibility.
**Owen Williams (he/she)** 08:01 Yeah, just for context, …
there was code… which piece of code had it? Was it the hotel collector had it?
**Arthur Silva Sens** 08:10 the collector.
**Owen Williams (he/she)** 08:11 Yeah, the collector had a feature where if your label name began with an underscore, it would prepend the word key.
And it's… there's a bug about this, and people were like, I have no idea why this is there. Unfortunately, some people are relying on it, and other people are relying on it not being there. So what we're gonna do is we're gonna make it an option.
like you do, and we will have the default be don't prepend key. It will still, by the way, prepend key if your label name begins with a number, because that's not allowed in Prometheus, but it will not do it if it's an underscore. And if somebody wants
the thing, they can set it manually, we're not going to make it a very discoverable feature. I think we will have to make it a flag in Otel Collector Config, because that's where people were using it, but we're not going to expose it anywhere else.
Thus, thus, we continue to iron out the differences between all these different things.
**Arthur Silva Sens** 09:09 Ugh.
Hopefully, 2.0, like, if we ever get to a 2.0 of the TLP translator, we remove this feature.
**Owen Williams (he/she)** 09:29 Yeah, and I think… so those… yeah, I think those are the last two things. And then, should I do that PR, or were you doing that?
One… I mean, I have to.
**Arthur Silva Sens** 09:39 … I don't know, I….
**Owen Williams (he/she)** 09:42 I can, I can do that one.
Yeah.
Cool. And then, yeah, then we should be able to do OTLP Translator 1.0, and then we'll… Brain….
**Arthur Silva Sens** 09:53 Shelter.
**Owen Williams (he/she)** 09:53 update all the dependencies in OTelGo, in Prometheus, in the collector, and then everybody will be happy, and…
You'll never have to think about this ever again.
Cool.
**Arthur Silva Sens** 10:06 Until the next book.
**Owen Williams (he/she)** 10:09 No, no, no, no, no more bugs.
I mean, eventually, this is going to be a library that was last updated 10 years ago, and just every… it just… because it's so… it's fairly simple. Like, yeah, it's gonna be one of those things that just sort of…
Stops… stops being updated, because this is not going to be a thing that needs to evolve.
**Arthur Silva Sens** 10:30 Yeah.
Alright, you or I wanna take the next one?
**Juraj Michalek** 10:39 Yeah, because this is….
**Arthur Silva Sens** 10:40 Kyle has a… sorry, Kyle has a raised hand.
**Kyle Eckhart** 10:43 I just wanted to ask, like, I work on Grafana Alloy. I know pretty much everybody here is a Grafana person, but I was kind of interested in the translator, because I'm pretty sure we don't use it in Alloy, but it seems like we probably should.
If somebody just wants to link me, okay.
**Arthur Silva Sens** 10:59 Oh.
**Kyle Eckhart** 11:00 At least so that I can get a better understanding of what its goal is.
**Owen Williams (he/she)** 11:04 So you might use it indirectly if you are pulling in things. Yeah. Essentially, the library exists because there was forked code in both OTEL Collector and Prometheus to do the same thing, which is translating names from
hotel to Prometheus, and they did it differently, and so there were inconsistent results. And so it exists to unify that process so that
as we fix these bugs, everybody gets the bug fixes. So, if you're already pulling in code that uses it, you should not need to worry about it.
Unless, for instance, you want to expose one of these stupid extra features, like somebody says, oh, I absolutely need key underscore. But generally, the intent is that you should not have to think about it.
**Juraj Michalek** 11:50 I looked at the codebase a little bit, just out of curiosity, to see if they need to update, and I think for you guys, you just need to update to Prometheus 3.0 version, and that should solve most of it for you.
**Kyle Eckhart** 12:04 Which is, yeah, that's in the next release, but….
**Owen Williams (he/she)** 12:10 Yeah, I'd say, the only thing you might have to… so the main thing that this affects, sort of, upstream… downstream, who knows, is how users configure
the…
translation. So, in Prometheus, that's on the OTEL native endpoint, and in the collector, that's in the Prometheus Exporter, has a configuration. I'm not sure what it looks like for Alloy, but essentially.
We're getting away from the, like.
Mimir had an option for, disable…
suffixes, and we're getting rid of that, and it's all about translation strategy. So as long as translation strategy is exposed somewhere in Alloy.
Then… then you will get the benefits of that package.
**Kyle Eckhart** 13:05 I'll check. It does not sound… doesn't sound, like something, but… Yeah, definitely.
**Owen Williams (he/she)** 13:11 Definitely DM me. I want to make sure… yeah, and also to make sure that the defaults are correct, because again, the vision is that no matter how you get your OTEL into Prometheus, that the defaults are consistent, and then the option… the configuration options are consistent. So yeah, send me a DM, we'll take it offline.
**GZ Gregor Zeitlinger** 13:31 Hi, sorry, missed the date.
**Arthur Silva Sens** 13:34 Oh, hello.
… Yeah, so I'm not sure if, like, next topic could be Yurai, or Greg, or whoever.
**Juraj Michalek** 13:45 of mine at the bottom again.
**GZ Gregor Zeitlinger** 13:47 No, no, no, I'm late, so I'll wait.
**Juraj Michalek** 13:51 Okay, no worries. Mine is pretty short, I guess, TrustAndify I.
we're doing two LFX mentorships that are a bit more related to Prometheus, but it'll involve
potentially some work in the auto collector too, right? We have one which is around Remote Ride V2 stability, so it's things like, running some compliant tests, improving documentation, finishing some
to-dos in Prometheus side. Hopefully, from my side, it's gonna mean that I have something nice to test against the remote ride exporter implementation.
And the second one is native summaries. So, summaries, right, are not supported in the Prometheus emote rider receiver, because they will be basically split by batching into multiple requests, potentially. So that, …
hopefully it's gonna be addressed by adding support for, like, native… the same way we have, like, one single struct for…
histogram in the, in the protobuf of RV2, I guess the goal for that is to have the support for the same for native summaries, so we then can support, receiving them in the, remote varieties.
**Arthur Silva Sens** 15:02 Nice.
**Juraj Michalek** 15:02 Have you… Yep. Have you picked the mentees already? Yeah, we just, …
we just created the, like, private Slack channels with them, so, yeah, they might start contributing next week, potentially.
We'll see.
**Arthur Silva Sens** 15:22 How are you feeling about selection?
**Juraj Michalek** 15:24 A lot of good candidates. I was surprised that it sort of came down to, like, we have, like, 4 or 5 different people who already started to, like, contribute at least a little bit, right? So it's like…
Basically moves the bar to, like, oh, if you haven't even, like, touched the codebase, you can't necessarily get selected.
So, that sort of was a pleasant surprise, but yeah, hopefully that'll allow us to make some nice progress on these things.
Awesome.
Yep.
That's it from me.
**Arthur Silva Sens** 15:57 Like, let us know if you can help somehow. We'll probably not…
Do, like, mentor work, but, like, maybe facilitate some stuff.
**Juraj Michalek** 16:05 Yeah, PR previews might come down the line, but I feel like a lot of it might be a bit more on the previous side at first than in the auto collector.
**Arthur Silva Sens** 16:13 Alright.
Hey, Gregor?
**GZ Gregor Zeitlinger** 16:19 All right, …
Let me, try to share.
Can you see, Maya? ….
**Arthur Silva Sens** 16:40 Yes.
**GZ Gregor Zeitlinger** 16:41 Tap…
Cool. Yeah, so this issue came up when I added a UTF-8 support to the Prometheus Java client.
… And, … I'm wondering how to proceed there. So…
combination of certain characters, for example, two percent signs, or two lambda characters,
would be turned into a single underscore before UTF-8 support. And that is because, first.
The strange character would be converted to an underscore.
And after that, consecutive underscores would be turned into a single underscore.
And now, it turned out that with UTF-8 support, this is changing.
And that is because, at first, when, hotel data is turned to Prometheus data, it is not changed at all.
That is how I happened to implement
the UTF-8 support in the Prometheus client.
And… The reason for that is…
That, we, keep the full data.
And when a Prometheus server is scraping the data, they, … Say, if they support.
UTF-8, using the escaping character, and if they do, then…
Either by saying explicitly underscore, or by just not saying anything, because they're an old Prometheus server.
Then they would get two underscores, because at that time.
Every single of those percent signs would be turned into a single underscore.
And… Arthur already explained that this is different for the Go client.
And I think this is interesting to discuss. So Arthur, if I understand you correctly.
You have to enable…
from OTel to UTF-8, and then also when scraping the Prometheus server. Is that right?
**Arthur Silva Sens** 19:03 Yes, there is two… two times where escaping can… can happen.
Oh, we… we first do escaping if asked.
doing the metric registration. If, for example.
… the user doesn't want to… to escape anything. You want… the user wants to keep UTF8.
But then the Prometheus, who is scraping this application, doesn't support UTF-8, has legacy, …
it requires legacy, validation, don't remember the name, but then there's another escaping happening during the scrape time, and that's because of the content negotiation.
**GZ Gregor Zeitlinger** 19:48 Yeah.
**Arthur Silva Sens** 19:49 If I understand correctly, you are focusing only on the content negotiation, but not during the registration of the metric?
**GZ Gregor Zeitlinger** 19:56 in the… Prometheus Java client, yes. And the reason for that is that, the…
Prometheus Java client is rarely used.
directly by end users. It's more used, by, … the, hotel.
SDK, where this is now coming up, or it's used by the JMX scraper, it's used by Spring Boot, so all tooling that is building on it.
And… When you use those tools, you typically don't want to have an extra… setting, like, …
Then we would have to add a setting to Spring Boot the Jamex scraper.
And now hotel. But, now when I also worked on the hotel part.
I ran into this issue, and … my current… …
pull request adds a UTF-8 flag that you just set to true, and that only changes
how double underscores behave, and I'm… a little bit… unhapp.
**Juraj Michalek** 21:17 Is it just me, or good work experience?
**Owen Williams (he/she)** 21:19 Trigger keeps, yeah, chop, choppy.
**GZ Gregor Zeitlinger** 21:23 Oh, damn.
How much did John say?
**Owen Williams (he/she)** 21:27 Yeah, so, so I just wanted to exp… …
Sort of describe, sort of, the… the…
the escaping and why there's two sets of escaping. And essentially, what we found… yeah, so the first thing we implemented was the content negotiation escaping stuff.
And…
It's… that doesn't give you a lot of control, and it's very opaque, because it's all in headers that are hard to debug, like, you have to do…
packet sniffing to figure out why you're getting one escaping versus the other. So, we've kept the content negotiation escaping step as kind of a fallback. Basically.
okay, I'm sending a UTF-8 metric, but the Prometheus I'm sending it to doesn't support that, so rather than just have everything explode, we do a simplistic replacement.
So that something can get through.
… We've had a lot better success having the…
first round escaping, which is what we've been describing, where you do it on the SDK side. …
Now, as for people not wanting to create a setting, I mean… Do you, you know…
That's what defaults are for, and it's… it's… we… we have established the…
the default that a Prometheus exporter should…
use underscore escaping with suffixes as the defaults, because then you get a predictable Prometheus-style metric, because that is what you should do. And then if people want the original name, they can flip the flag to no translation and set, you know, set that. So the intent is that
On the metrics production side, there's some way of… configuring that.
If, you know, I think, I think it's acceptable if it just always translates to Prometheus style.
…
you know, I feel like we're trying to establish that hotel people can send the original names if they want to.
But…
it's just having that configuration being done from the scraping side, from that Prometheus through content negotiation, was kind of… was just very awkward and unpredictable, and led to a lot of confusion, so that's why we've been moving away from that.
… So, so the intent is that, basically, by the time the metrics are being…
are getting produced for scraping, or they're being sent remote write. They are in the final form that the user wants them to be, and that we don't… we would prefer not to have any of this sort of translation being done automatically, sort of.
Because of the content negotiation.
… I don't know if that sort of…
That's sort of the history of what the intended workflow is.
**GZ Gregor Zeitlinger** 24:29 Oh, so it's not really about this double underscore thing that I explored, it's more about
educating users, if I understand that correctly.
**Owen Williams (he/she)** 24:39 Yeah, I mean, so the double underscore thing, this is coming from one of these
inconsistencies in how escaping was done. …
And Artur, I can't remember if the content negotiation escaping, I don't think that reduces the underscores, I think that just does the replacement, because that's all it's doing, is it's saying, oh, I've got an invalid character, I'm sticking in an underscore, so it's a very… it's a very simple replacement. Whereas the translation package
is doing a lot more complex work. So the translation compa- package is not only replacing things with underscores, it's then shrinking the underscores down.
It's then attaching suffixes, it's checking to see if the suffix has been repeated, because sometimes people put the unit in the metric name, and so then you don't want to also append the metric name. So it's doing some complex work.
And so you get a….
**GZ Gregor Zeitlinger** 25:33 That is actually done by the Prometheus Java client, not by the… translator in case of Java.
**Owen Williams (he/she)** 25:39 True, okay, yeah, that makes sense, because the translator we're talking about is just GoCode.
So, so yeah, the, the, the, and I think, yeah, and I think FedE,
who worked on the Java client, was basically reproducing that set of operations. So, in other words, if you do the translation ahead of time with
The sort of spec-compliant stuff, you end up with a more consistent result and a more correct result.
If you're relying on the content negotiation part of it, you're getting a very…
Simple character replacement that is not… does not have any knowledge
it doesn't know it's coming from OTEL. It knows… it just sees an invalid character and replaces it, whereas the OTEL exporter
uses the knowledge that it has about the metric that it's converting to do that. Now, I think in OTLB Translator, we have a
Archer's working on this, is it in a feature flag to maintain the multiple underscores?
**Arthur Silva Sens** 26:42 It's gonna be configurable.
**Owen Williams (he/she)** 26:44 Yeah, so then….
**Arthur Silva Sens** 26:45 Yeah.
**Owen Williams (he/she)** 26:46 So then that's just a flag you flip in the…
On that side. And again, that could be a default if you don't want to… …
Expose this to users.
**GZ Gregor Zeitlinger** 26:57 Hmm, okay, yeah, so… My takeaway is that having this flag on the interest side
It's… is a good thing.
**Owen Williams (he/she)** 27:08 Yeah, it's… yeah, I think it is, and this sort of matches…
this isn't something we sort of invented on our own, this is coming from customers saying, hey, I want to set it up this way. There's been… there's always this hypothetical of, like.
oh, what if a customer has a thousand agents, and they want to flip them all at the same time? Oh, that's easier to do if you flip a flag on the scraping side. That hasn't actually…
happened as a… as a situation. It's much more common that somebody says, hey, I'm sending these metrics, and I want to send the metrics the way I want to send them. And so having the configuration being done there…
and philosophically, the way I think of it is, where is the translation from OTEL to Prometheus happening? That's where the configuration should be.
In the case of the Prometheus endpoint, the OTEL endpoint in Prometheus, you're putting it in Prometheus. In the case of OTEL Collector, you put it in the Prometheus exporter. And that's been… that has worked well for users. Like, okay, where am I doing this translation to Prometheus? That's where the configuration should be.
**GZ Gregor Zeitlinger** 28:16 Well, I could also take your argument and flip it around, saying that
Prometheus, supports UTF-8, then the translation from UTF-8 to underscore should not be when converting to Prometheus.
**Owen Williams (he/she)** 28:35 Yeah, I mean, it's… like I say, this is how things have evolved based on…
What people have found more or less confusing in practice.
… it's… it has worked better that Prometheus Takes what it's given.
**GZ Gregor Zeitlinger** 28:55 Yeah, okay, yeah, good.
I think that's, that's, that's great feedback.
**Arthur Silva Sens** 29:03 oh, what do you want to do with this issue? Like, is there anything that we need to… to…
Change in the spec to make it clear? Or, like, should we just close?
**GZ Gregor Zeitlinger** 29:14 No, the specs as should, so, ….
**Owen Williams (he/she)** 29:22 I mean, we could, ….
**Arthur Silva Sens** 29:24 Like, that you've talked about.
**GZ Gregor Zeitlinger** 29:26 be helpful.
**Owen Williams (he/she)** 29:27 Oh, sorry, yeah, you cut out again, sorry.
**GZ Gregor Zeitlinger** 29:30 Yeah, my internet is really bad. No, all good. I was just looking for the feedback.
**Arthur Silva Sens** 29:36 Yeah, if you wanna CC me on….
**Owen Williams (he/she)** 29:40 on changes you're making, I'm happy to look them over.
**GZ Gregor Zeitlinger** 29:43 Okay.
**Arthur Silva Sens** 29:51 Alright, any other topics for today?
**Kyle Eckhart** 29:56 Real quick, just wrapping background about the translator. Is the end goal to deprecate the package translator, Prometheus, that's currently in OTEL Contrib, essentially? Like, that's what it looks like from the context of the ticket, is to replace that everywhere in OTEL with the library.
**Arthur Silva Sens** 30:13 Yeah, but, but, there is a but. This… this translator and the collector, it translates both ways.
Prometheus to Hotel and hotel Prometheus, where this new package only translates OTLP to Prometheus.
So…
So this old package will stay there to do the reverse translation. If you're getting Prometheus metrics with bytes.
Sorry, with, units… With underscores, and you want to translate to a tell?
**GZ Gregor Zeitlinger** 30:46 Then this package is still there.
**Arthur Silva Sens** 30:56 Yeah, I see you and I added a comment, a topic, say, please review my PR, like, anything…
That you want to add, or it's just literally just….
**Juraj Michalek** 31:07 Really quick for that. There's one point, I pinged Bartik in there, where I'm not sure… if the…
the, like, histogram hints, so if anybody's familiar with that, that would be helpful, but I already have one approval from David Ashpole, and then it's…
one or two more PRs, and then I'm gonna reach out to some people to test… ask them if they would be willing to test the…
RV2 version for me.
**Arthur Silva Sens** 31:37 Right.
**Juraj Michalek** 31:38 I'll already set up some testing environment.
**Arthur Silva Sens** 31:42 Sounds good.
**Juraj Michalek** 31:43 I have it running, at least.
**Arthur Silva Sens** 31:45 I'll try to find a little, find time to review this week for you.
**Juraj Michalek** 31:50 North.
I also have, like, just out of curiosity, I also see that…
Some of the… so this is for the translator package?
But I see some of the tests for the exporter in order that exporter actually failed. Locally, for me, it's succeeding, so I think it just might be something finicky with the pipeline. Did you encounter that by any chance before, Arthur?
Where, like, something would….
**Arthur Silva Sens** 32:18 I….
**Juraj Michalek** 32:21 It also, like, fails on a test that shouldn't even be running, I think, that says, literally, it's not supported when using Val.
**Arthur Silva Sens** 32:32 Theyher says the process cannot access the file because it's being used by another process.
**Juraj Michalek** 32:37 Yeah.
**Arthur Silva Sens** 32:37 It seems… it sounds like flakiness.
**Juraj Michalek** 32:41 Yes?
The interesting part is, at least the two rounds of the pipelines I had, it failed both times.
But… and I don't see an issue open yet on the, like, there's the…
There's some automation, right, that detects this flakiness phase.
**Arthur Silva Sens** 32:59 Yeah.
**Juraj Michalek** 33:00 I need… I don't see one open for this yet, but yeah, I'll try to run it in a loop for a while locally, see if I can get it to reproduce.
**Arthur Silva Sens** 33:09 I'll take a look as well.
**Juraj Michalek** 33:11 Yeah, I don't think it's related to my changes, because I'm just touching the…
Yeah, I'm just touching the translation package.
Anyway, that's it.
**Arthur Silva Sens** 33:26 Okay… Less chance to add another topic.
5… 4… Tree.
2.
What?
Alright, thanks everybody. See you in two weeks.
Bye-bye.
