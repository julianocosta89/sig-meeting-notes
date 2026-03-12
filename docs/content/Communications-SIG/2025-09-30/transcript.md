SIG: Communications SIG
Date: 2025-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Patrice CNCF 00:02:24 Hello, hello.
Vitor Vasconcellos 00:02:28 Hello?
Patrice CNCF 00:02:36 How are you, Vitor?
Vitor Vasconcellos 00:02:38 I'm good, I'm good, thank you. And you?
Patrice CNCF 00:02:41 Good. How's everything going?
Busy, but good.
Vitor Vasconcellos 00:02:48 Is that the same food.
Patrice CNCF 00:03:10 Is the note, noteetaker something we set up?
Vitor Vasconcellos 00:03:19 Sure.
Florian Lehner 00:03:21 Hello, everyone.
Patrice CNCF 00:03:22 Hi.
Vitor Vasconcellos 00:03:23 I'm saying, lazy front, hello.
Patrice CNCF 00:03:27 Here's the last Severn one piece.
Dear… Are we in the same time zone, Vitor? Is it noon for you?
Vitor Vasconcellos 00:03:44 It's 1PM here.
Patrice CNCF 00:03:47 Offer you?
One hour later. It's noon.
That's not…
Vitor Vasconcellos 00:03:51 Okay.
It's very close.
Patrice CNCF 00:04:00 Yeah. Except that you are in… is it still in summer, or it's not summer anymore?
Is fall.
Yeah.
But it's… the weather's been quite warm.
Vitor Vasconcellos 00:04:15 Yeah, here it's starting to… to get warm again.
We're… I think we are in spring already.
I don't know.
Patrice CNCF 00:04:30 So it should… we had, Equinox, so… should be… in spring.
Hi, everybody.
Vitor Vasconcellos 00:04:52 Hello.
Patrice CNCF 00:04:52 Tiffany, do you know if Severin is joining us?
Sorry, I didn't get that. Was there… and I wasn't looking, so I couldn't read your…
TH Tiffany Hrabusa 00:05:08 I said, I haven't heard.
Patrice CNCF 00:05:10 Oh, there we go.
TH Tiffany Hrabusa 00:05:10 Oh, there he is. Can you hear me?
Severin Neumann 00:05:14 Hey, did you miss me?
TH Tiffany Hrabusa 00:05:16 Okay.
Patrice CNCF 00:05:16 Yes, we were.
Severin Neumann 00:05:23 To edit the note-taker thing, can we get rid of that?
Patrice CNCF 00:05:27 I was gonna ask you whether this was something we had officially endorsed or not.
Severin Neumann 00:05:35 Okay.
Yeah, I think Deanna, I think, yeah.
I will let her know.
It looks like you can let it nurture Leafs. That's at least a feature I appreciate.
I think I know who.
Patrice CNCF 00:05:58 Okay.
So…
Severin Neumann 00:06:01 Give me a second.
Patrice CNCF 00:06:02 That's… that's the magic incantation to have it leave.
FF leave.
TH Tiffany Hrabusa 00:06:12 And they should make it FF bye-bye.
Severin Neumann 00:06:20 Yeah, at least as a great feature, because we had those kinds of bots in the past, and you could just not do anything, so I had to go in some backends and figure out, like, where these Zoom credentials are and everything. So, yeah, glad it's… it's having that feature.
Yeah, if it's, like, who I think is owner of Dad. I asked her to… Because I think we even have a policy around it that people shouldn't do that. So, just for everybody to know, don't invite your note-taking apps to any of the… of the OpenTelemetry community meetings. They are recorded anyways, right? So there's not really, like.
Any value in that?
anyways, let me… So, first of all, it's great to see so many people. Looks like doing it on Tuesday.
It's much better than doing it Wednesday.
I don't know, so welcome, everybody.
Let me bring up the… agenda. I was just jumping from one meeting into this one, so I'm not well prepared yet, but… Let me change that.
TH Tiffany Hrabusa 00:07:40 I just shared the link to the agenda in the chat for anyone who doesn't know where it is.
Severin Neumann 00:07:47 Yeah.
Patrice CNCF 00:07:48 Thank you.
There's an attendee list, so anybody who's here, and if you don't mind adding your names and… credentials… To the top of the list.
Severin Neumann 00:08:06 We have a few topics on the agenda. If you have anything you'd like to add.
I say add it to this document, pull it out here, put it into the chat, whatever.
Whatever works for you.
Once again, super excited to see a few more new faces.
So welcome to… to the SICK meeting.
yeah, I think for… oh yeah, there was another topic.
No, we haven't. So… Cool. Let's go through the agenda, then, one by one.
The first one was, like, triggered by TAD around the Hotel Unplugged event, that we should have a landing page for that. I think the main question is, like, where do we want to put it?
So I see that, Patrice, you put your suggestion there to have it, like, under events unplugged.
I was wondering… So my initial suggestion was, like, hey, have it under OpenTelemetry I.O. Unplug.
But I think the question is, like.
Could we have a top-level domain pointing to it? So did we do unplug.opentelemetry.io?
that just… Point to wherever we put it.
And then we are like, Free of that.
Patrice CNCF 00:09:26 So… Maybe if we step back, can we agree that we have… we will have a page?
That will be untitled, unplugged, that will be… agnostic of the year, so I… I would rather not have the year in the URL, and that's pretty much what the CNCF and the Linux Foundation do, which I think helps us avoid links going stale and having to add redirects, because most people… and that page can have… backlinks to resources from previous events, but at least it'll be managed in that one page. And otherwise, people are coming to it to get the current information of whatever's upcoming or what just passed.
So, can we agree on that?
Is there a agreement? Okay.
TH Tiffany Hrabusa 00:10:16 Yeah.
Patrice CNCF 00:10:18 Otherwise… Sure, if we want to manage subdomains, I'm… Kinda hesitant, because… I would rather have a URL in the path that I've given there, which is events, and then Slash events, then slash the name of the event.
That gives us maximum flexibility, we don't have to deal with subdomains, and we don't have to deal with… well, how important is the event, and does it merit a subdomain? And this one wants a subdomain, but we don't want to give it… because this event is too small, or it's just a co-located event? What… what do you think about that?
Severin Neumann 00:10:56 So first of all, I think that's an important event. Yes. At least from, like, how the GC thinks about it, because, like, this is, like… a lot of the TC members are super, like, Adamant about having it.
And when I was thinking about the subdomain, it was less about, like, using that subdomain throughout, like, our website and everything. It was more like, think about people putting that Ling on a… Poster, or put it on another website, or something like that.
That is, like, unplug.opentelemetry.io just resolves 302 or whatever into whatever place for use, right? So it should not have, like, a… its own dedicated URL under which, like, everything works, but more like blog.opentelemetry.io just redirects to Opentelemetry.io slash blog to just make it easier for people to access it. That was the only thing I was thinking about, the subdomain, right?
and then have it under OpenTelemetry I.O. Events Unplugged, or maybe even OpenTelemetry I.O.
Community events unplugged, so it would… Nicely tie into the structure that we have already.
I think that that was the only reason why I said, I was thinking about, like, having a subdomain And then URL, because then we have, kind of, the best of both worlds, so to speak, if this makes any sense. Like, the easy, accessible thing is the… It's the subdomain, and then everything we use within the website is the, like, fitting into… into our existing hierarchy.
Patrice CNCF 00:12:35 Right. I forgot about community intervening in that path.
just… I, understand your point of view.
as an intermediate, if you look at what Linux Foundation has, the subdomain is events.
So, events… it could be events.opentelemetry.io slash unplugged, and then that redirects Maybe the whole events page redirects to community events.
As an alias, or as a redirect.
How does that sound?
And then again, we can always have a dedicated, if… if… you think… Okay, stepping back.
My concern is if we have unplugged.opentelemetry.io, are we going to want to do that for every event?
And if not, that means we have to draw a line in the sand somewhere, and we have to debate with some people whether… which side of the line they're on. Whereas if we don't have a dedicated subdomain for Unplugged, then we don't have to deal with that quite.
Severin Neumann 00:13:38 Hold on.
No, I think that's a fair point. I mean, at the end, it's more like a… and I will bring this up at the GC meeting, I think that's… that's probably something we as comms can just defer to them and say, like, hey.
I mean, a part of the GC, but now talking about different entities within the project, right? To say, like, hey.
We, as comms, this is what we do.
And if GC is overwriting that, that's a different decision, but what we offer you, if you're running an event, is that you can have this and that. And sorry, Tiffany, I see you raised her hand, so I will shut up.
TH Tiffany Hrabusa 00:14:17 I just had a question as a relative newbie. Is the name… is the event name Unplugged unique to OpenTelemetry, or do other open source projects in the ecosystem use Unplugged as an event name?
Severin Neumann 00:14:34 My understanding is it's unique, and it was used previously already.
I think it's, like, repurposing something that existed already, but we would need… I think Austin or Ted would have more context on that. I don't… I think there was something very, very, very early on called OpenTelemetry Unplugged, I would need to dig up the history on that.
And they're like, yeah, let's, let's… Yeah.
Patrice CNCF 00:15:05 Tiffany, is your question in terms of open telemetry, or more broadly as to whether unplugged is used?
TH Tiffany Hrabusa 00:15:13 Yeah, more broadly, like, I'm thinking most people are gonna end up on this page from a link to some kind of promotional material, right? Whether it's a banner, a blog post, a social media post.
So the URL in that context doesn't matter so much. So for people who are searching for the event page, if they search for unplugged, are they going to find a bunch of other event pages? Because that's a common term across OSS.
projects, or is it unique to OpenTelemetry? And then maybe that helps with how… whether we do subdomains, or we kind of bury it in the… In the, the path.
I don't know.
I'm not an expert on this, so…
Patrice CNCF 00:16:00 So, I just wanted to present my point of view. I don't have a strong opinion. Now that we've had a discussion, I'm thinking maybe just opentelemetry.io slash unplugged as an alias, going into the community events unplugged page.
would probably seem like the best approach to go. I think I'm just pushing back on subdomains because we're… We've been having issues with subdomains, and the list seems to be growing, and I'm not sure how much you want us to manage that.
And again, there, it's not a big deal, but… I'm okay with… a top level slash unplugged as an alias to Community Events Unplugged.
Severin Neumann 00:16:47 Okay, so, but, but, like, And let me put it that way. We put it under… OpenTelemetry, I.O, community events unplugged, that's, like, where it just lives.
And we can do, like, the OpenTelemetry I.O. slash unplugged.
Or, in a sense, this is something like, the GC can override sitcoms on that if they insist on having a subdomain or whatever, then yeah, let's have it, right? But, like, this is the place where we say, like, hey.
if someone comes and says, like, hey, I prepared, like, this page and everything, that's where it lives, right? That's, like, the place where it lives. Everything else we can manage via redirects and everything else, right?
Patrice CNCF 00:17:32 Yes.
Severin Neumann 00:17:34 Okay.
Patrice CNCF 00:17:35 That works for me.
Yeah.
TH Tiffany Hrabusa 00:17:39 There's also the future possibility of if we start having a lot of OpenTelemetry-specific events, we could pull events up to, the top nav, right? Outside of community, and just make that But I think that would only happen if we started having a lot of open telemetry-specific events.
Severin Neumann 00:18:06 Yeah, I don't think that's going to happen, so… I don't know, like, I mean, at the end, also, like, I mean, we appreciate that community members are doing events, but they should more embed it into CNCF.
chapters and everything, right? But it's a very separate discussion, right? This is more like, hey.
the GC decided to run this OpenTelemetry Unplugged thing, it's like a… Event by the community, for the community.
And that's what we do, right? And everything else, that's worth a discussion another time. But yeah, I think if we have more and more events, there's some space for that.
Cool.
But I think we have, like, our decision on that.
Okay.
Next topic is… And I think Fabrizio had the problem that he cannot join.
But we had, like, an open discussion around, like, hey, it's time to add profiling to our website.
Because, like, The project is moving towards… I don't know, alpha state, better state, version 1.
Something like that.
And I think one thing is very obvious, like, hey, on the concept page, we need profiles as a signal, right? And we maybe need to find a few spaces… places where we say, logs, metric, traces, common profile. There's a little bit of a work.
But I think the more challenging question is, like, in our information architecture, where should, like, the… profiling… what's the right term for it? Profiling agent, profiling solution that we offer live, right? Because it's not like… it's not language-specific, is my understanding, so we cannot say, like, hey, here's Java, and then here's how you enable… it's more like this zero-code instrumentation solutions.
But I'm not exactly sure if it fits that description. But Florian, you can probably speak about that.
Florian Lehner 00:20:21 Yeah, hi everyone. I'm from the Profile Exec, and I saw the topic on the iGENT and thought about joining.
Yeah, as you mentioned, profiling is moving on. We are about to announce the alpha state of the profiling signal.
And it's become major and major. Just to catch up.
with, where should it land. Personal opinion, serial code implementation is the wrong place.
With the reasoning, or we don't touch code, and we don't, enrich code, like it does with the, like the existing solution do, like, SDKs for auto instrumentation, or even Obi. Profiles is a dedicated signals, and if you look into concept signals, there's already a link for signal, for Profiles.
But it's leading to something very different, and so it's not leading to, specification, just, I think it's at the moment a document, of the, of the profiling secure.
Severin Neumann 00:21:27 Yeah.
Florian Lehner 00:21:27 Position where we should want to go.
Yeah, I think the idea should be to promote profiles from just, something under development, to more stable ones.
And then, yeah, the question really is, where should we land as profiling more in the rest of the concepts?
So it's basically a fourth pillar of observability, rather than… Another solution to how to instrument something.
I hope this clears something up. Patrice?
Patrice CNCF 00:22:07 It seems that we're agreeing on a first step, that it, the current profiles link on that signals page, which goes elsewhere.
So could we get a first PR in to rework this and have a… An actual dedicated profiles page first, and then maybe that'll give us inspiration and time to figure out where else, We might want to position it.
Florian Lehner 00:22:36 Yeah, sounds good to me.
Filling in these profiles, spaces, under signals with with value is something important, I think, and if you look into traces, metrics, and logs, It… it's… mmm… everything… everyone does a little bit different, and so, I was wondering, is there a concept profiles should do to be… Under these four, or, what is the expectation to land there?
Severin Neumann 00:23:11 Just to clarify that, this is, like, what we also talk about, right? So there is the profiler as a tool itself, right? Here's a signal profile.
Florian Lehner 00:23:21 Yes and no. The eBay Proviler you just showed is just, an, exporter in the terms of OpenTelemetry Collector. But for example, if you look into, async profiler of Java, they can also export, nowadays the hotel profiling signal.
Severin Neumann 00:23:48 Okay, then maybe my question is more like, my understanding, like, was this is, like, the thing we do. I mean, because if you say, like, hey, we have… we have language-specific stuff.
Then, yeah, it should lock… But we say a language API, and SDKs.
I think what would help us… Is independent of buried lands.
And this is maybe something what Patrice was also referring to, like, if we start with the signals profiles page.
like, an understanding of, like, the landscape, so… so… because, like, yeah, I have a superficial understanding of profiling, but But what can you do today, right? Because what I hear right now is, like, it's more like the situation that we have with logs, is that, like, yeah, sure, our APIs and SDKs can do logs, but, like, other people can do open telemetry logs as well, and we are super happy with that. And if… there's tools out there, and I think also Pyroscope is doing OpenTelemetry profiles already in the OpenTelemetry format. I saw at least something that they have, like, OpenTelemetry support.
Florian Lehner 00:25:00 Something like that. OpenTelemetry EBPF profile you just opened.
Severin Neumann 00:25:06 Okay, so they're just wrapping that as well. So, I think, like, what would help us, A, that having the page off under signals, where we just see, like, profiles.
and just write it as you would write it. I mean, we have, like, the capability to help you to copy-addit it, right? To make it, like… so don't hesitate to throw something over a fence where you say, like, yeah, I'm not super happy with how it sounds, but, like, here's my mental model of that, right? And we can… turn this into something. But then the next step is for us also to understand, like, okay, what solutions are out there?
So that we can figure out, like, do we need a new top-level domain, a top-level section here in that navigation?
Or do we need something entirely different? Is it also, like, something that we can move in existing categories, right?
Yeah, Tiffany?
TH Tiffany Hrabusa 00:25:58 And to Florian's question about whether he should model the profiling page on the traces, metrics, or logs, if there's a standard there, I don't think that there really is. I think it just depends on the signal. So, write the page as it Is… as it best explains the profiling signal.
Severin Neumann 00:26:17 Yeah, I think…
TH Tiffany Hrabusa 00:26:18 Users would need to know.
Severin Neumann 00:26:21 Yeah, I think nobody broke that one with the other ones in mind, so yeah.
Florian Lehner 00:26:28 Okay, yeah, makes sense to some degree, yeah. With regard to the… EVPF profiler, so the, the implementation of the profiles protocol. I think it's… the situation is similar to OB, I think there, at the moment, there's a switch in the observability space from sidecar solutions and outdoor instrumentation.
to daemon set, instrumentations.
And, yeah, it would be nice to have a dedicated move around this area where you say, hey, I don't… you don't need to instrument your application, but you get the same value with these daemon-set deployments.
Severin Neumann 00:27:17 Yeah. Patrice?
So, I, yeah.
Patrice CNCF 00:27:21 following through with what Tiffany said, the reason I suggested taking a concrete step forward in actually writing some content is… I think it'll help us, first of all, the rest of us, as we review it, to have a better understanding and, so, no, there are no standards, and I would say… Feel free to write more than less.
And that will give us content, and if… with that concrete content, we'll be able to suggest, oh, well, maybe this doesn't go in the concept signals profiling page, let's move it somewhere else. But at least we'll have concrete content to move around.
The other thing I wanted to suggest is, Severin, if you could go to the status page… And then the specification status page.
This one? Yes, scroll to the bottom, and there'll be the specification, and click on the specification status summary.
Severin Neumann 00:28:24 Yeah. And scroll down, all the way down.
Patrice CNCF 00:28:27 So, we have profiles here. There should be, I guess the… the… status will be changing to alpha at some point? Is that… Correct?
Florian Lehner 00:28:41 Star idea, yes.
Patrice CNCF 00:28:43 But I just wanted everybody to be aware that there is a status here, and this is, in principle, the status page where people should go to. We don't necessarily repeat those statuses elsewhere, like in the concept pages.
But I wanted to make sure you were aware that there's an entry here.
Florian Lehner 00:29:02 Yeah, thanks for sharing, just clearing about this.
Patrice CNCF 00:29:05 Yep.
Severin Neumann 00:29:08 But this is taken from the spec, right? So this is just us rendering the spec page on that, so you need to update.
Then on the SPAC, and then we take it from there.
So if you say, like…
Patrice CNCF 00:29:20 extracted.
Severin Neumann 00:29:22 Yeah.
Yeah, exactly.
Yeah, so I think the action is, like, Step one is, like.
you, Thorian, or anybody else from from the sick.
you provide us with a PR on, like, the signal.
And, as I said, feel free to add more context than is necessary, so we can… We have a better understanding then, and we can then work towards figuring out Where and how to put it.
So maybe just to throw this in, and then we don't have to have a long discussion on that, I think a few weeks back, we reconsidered this whole serial code instrumentation section.
Because, like, it… it's not… exactly fitting a few of the solutions that are under that as well. I think even OBI is not exactly a serial code instrumentation to some extent.
The same is true for a few other ones, where we say, like, yeah, you still need to touch code, technically.
But maybe we can… But maybe profiling is a big enough topic that we can move it into its own category. I don't know yet. I think that's the long answer, right? So… so let's start with the concepts page and move from there. So, Yeah.
Florian Lehner 00:30:49 Thank you.
Patrice CNCF 00:30:51 Thank you.
Severin Neumann 00:30:54 Awesome.
Cool.
I don't think we have anything else on this profiling topic.
maybe just to call this out, Florian, anytime you join us, and if you're only interested in a specific topic, just let us know so we can also put it to the beginning of the meeting. So if you say, like, hey, the rest of this meeting is not relevant for you, we can just, spare you some time sitting through some event discussions, except you're enjoying them, so we are always happy to have you here.
Florian Lehner 00:31:33 Thanks for the invitation, yeah.
Severin Neumann 00:31:34 Yeah. That's fine.
Back to the next topic. Patrice, you had something on blog post localization, so… Yeah.
Go ahead.
Patrice CNCF 00:31:47 I know we discussed this on… or there was a discussion on chat briefly.
I don't know if it was ever discussed during this comms meeting.
At some point, I think it's mainly the… There's a name that, escapes me at the moment.
the Ukrainian… Andy, who's been pushing translations of old blog posts. And as we know, our policy Is we consider blogs… blog posts that are More than a year old as potentially outdated, and there's a banner posted at the top.
Well, let me first ask the question, has this been discussed already, in terms of whether we should support…
Severin Neumann 00:32:44 So, is there…
Patrice CNCF 00:32:45 Authorization of outdated blog posts, or older blog posts.
Severin Neumann 00:32:50 I'm not 100% sure. Tiffany?
TH Tiffany Hrabusa 00:32:53 I don't think we discussed it in a meeting Or I don't remember us discussing it in a meeting. I did raise this… specific PR in Slack.
because I think this was the first one that Andy had raised. Since then, there have been subsequent PRs, but… Yeah, I mean, it… to me.
if you're going to… I mean, I guess at this point, he thinks, like, he has already translated the entire docs website into Ukrainian, and there's that PR that's kind of standing out there, so, like, telling him that maybe translate Docs is… is a… is not… Priority.
Yeah.
In this specific case, I didn't have a strong objection, because it's, like, kind of a pivotal moment in OpenTelemetry history, and it also relates to, like, transitioning. I don't know if anybody would still be on OpenCensus and need to migrate, but… I didn't have a strong objection at the time, but now that there seems to be a pattern, I think, yeah, it's worth talking about.
Patrice CNCF 00:34:06 Okay, thank you for the context.
Severin Neumann 00:34:08 Just for my clarification, we only talk about old blog posts, right? Because we have a pattern now that some of the more recent blog posts got localized into things Spanish and Portuguese, and I think we have a bunch of, like.
blog posts that have been localized. So, okay, so it's more around, like, hey, someone coming and saying, like, oh, I can localize you this blog post from 2022, And then specifically now with the Ukrainian localizations, yeah.
Patrice CNCF 00:34:43 I'd like…
Severin Neumann 00:34:44 I also… Yeah, because…
Patrice CNCF 00:34:46 step back, since it's concerning the Ukrainian translations.
For which, I think maybe that's the broader… Discussion here, which has come up.
multiple times.
And I kind of get the feeling that our SIG is… oscillating, trying to do its best to support that localization, but… and trying to figure… it's challenging our principles, and I think one of our main principles is to build community.
and to be sustainable. Because right now, we… in, SIG comms are feeling the weight, and the… Increased workload that is there, with some of us being less available, and there's movement in terms of approvers and maintainers.
Every extra bit of work.
And so, that's where this came up, where to me.
an officially outdated blog post, what is the value, and are there community members to review it and approve it? And I don't think there is, and so we… I agree with what Tiffany was saying. There should be a focus on getting a community built some approvers for Ukrainian for the docks first, before we spend any… Cycles on the blog.
Severin Neumann 00:36:18 Yeah, yeah. No, I, I, I, So it's an overall at the end.
Bye-bye.
overall, I agree. There's… So I think we are tapping in a lot of very complex topics right now, right? So let me comment on the UK situation first.
I'm a little bit… I'm not liking the right English word for that, but… I feel sad for Andy right now, because, like, we pushed him… to follow Our agenda, and said, like, yeah, it's great that you did all this localization.
On your own time and then everything, but please follow what we asked you to do. We even helped him to find people, help him with that. So we had two or three people say, like, yeah, I help you with Ukrainian localization.
And we started the Ukrainian localization and independent of if it's blog posts or not, all his PRs towards that have not been reviewed, right?
We merged one… More or less by accident, because, like, it was not reviewed by a localization, it was just, like, we oversaw that ourselves, but at the end of the day.
nothing has been, like… there's nobody, like, helping him with that, right? So he's back to a one-person effort, and I think… and that goes back to what you said, the crucial part is about building community, and I think that the big question is what can we do?
to… to help the UK localization group, right?
Also anticipating that they're politically in a very difficult situation right now with what's going on in Ukraine.
Yeah, Tiffany?
TH Tiffany Hrabusa 00:38:17 Yeah, I was just going to say, I noticed on the recent Romanian localization PRs that I think, Diana has recruited, some, Romanian speakers who don't have any experience with, like, GitHub or software or anything to come in and just review the Romanian PRs from a language perspective.
Severin Neumann 00:38:45 Yeah.
TH Tiffany Hrabusa 00:38:46 That's an interesting idea. You know, maybe there aren't, people in docs or documentation or Software development who have the bandwidth and also speak Ukrainian, but maybe there are other people that Andy could reach out to who literally could just read the translation and give, like, some feedback. I don't know if that's something we would recommend to him, but I did notice it happening on a Romanian PR, which… Was an interesting concept to me.
It does kind of fly in the face of building community, because those people probably aren't going to stick around to join the community.
But… If we wanted to help him move things forward.
asking if he knows anybody who would be willing to just read the PRs and check that might be an option.
Patrice CNCF 00:39:41 Does anybody know if Andy's, Well, I know the fact that he's translated the whole thing, and that there's a PR with the entire translation, which I think he's keeping up to date.
Severin Neumann 00:39:51 That means there's a preview available for…
Patrice CNCF 00:39:57 the Ukrainian community, even though it's not endorsed. But… That raises the question, and I think I brought this up in our chat, I understand that the circumstances are different, very particular for Ukraine at the moment.
the question is, how do we wish to support them? And my concern is I want to make it so that we are not Imposing extra burden on ourselves.
severin, you and Vitor had kind of proposed, well, maybe we can review it by doing double translations.
that… Is a creative way to… support the Ukrainian translation, but I don't think it's scalable, and we're overlooked already. So… what I'm going to propose is opening up a new can of worms, but since it's very circumstantial, I would say we could… accept Andy's PR, but put a big banner at the top to say that this is not endorsed by hotel, see comms, It's provided by… You know, some message to say that there are…
Severin Neumann 00:41:15 Yeah, yeah, yeah, endorsed is probably, in that situation, maybe a very… not endorsed is a strong word, but I get your point, like, it's not peer-reviewed, or, like, we normally would do that, but, like, anticipating the circumstances and something like that. So, Yeah, I remember that you brought up that suggestion, and since you said, like, it opens up a can of worms to say, like, yeah, where do we draw the line to… to accept Brooke like that, and don't accept it.
because there's probably other… Communities that would say, like, oh.
We are also in a very difficult situation, and we want to provide you with a… with a… Full-size localization, But…
Patrice CNCF 00:42:07 The other backup solution is… I don't remember if I… so we have Google Translate, Available.
on fallback pages. I just don't remember… I haven't added all of the new, most recent locales, but I do have an issue open for me to do that. That gives a fallback.
Severin Neumann 00:42:28 Yeah, yeah.
Patrice CNCF 00:42:29 That's a separate issue.
Severin Neumann 00:42:30 Yeah.
Maybe, and it's… but that's maybe something we cannot solve today, and maybe take home, is like.
let's suppose we want to support Andy to have his major PR merged.
what's our… what's our measurement stick, right? Not that someone comes the other day in and says, like, hey, here's my German localization, I did all of that in German just yesterday.
Would you willing me to, to, to accept that, right?
And that's… I think there we need to be 100% clear, right? We need to say 100%, like.
And even if we say, like, we only do this for the Ukrainian localization after Hours of debating that, or whatever.
And it's a one-off decision, and we might even reverse it at some point, whatever. I don't know, but yeah, Tiffany?
TH Tiffany Hrabusa 00:43:26 Well, I think we have, context to point back to.
We asked Andy to follow the procedure. He followed the procedure. We've tried recruiting fellow Ukrainian reviewers, and there just aren't any. So…
Severin Neumann 00:43:42 Okay, yeah.
TH Tiffany Hrabusa 00:43:43 you know, we can say, like, if someone else comes to us and says, I translated the entire website into German yesterday, here it is, you can say, no, but you still need to follow the process. And then if, you know, we can set a time limit, 3 months, 6 months later, if there are no German fellow reviewers, then maybe we do accept that. Because at the end of the day.
maybe some localization is better than nothing, I don't know. But I think we do have… it's not like we just granted Andy this special privilege out of nowhere, like, we did ask.
for the Ukrainian localization to follow the process.
So, maybe there's something there for an exception to be granted in the future, even if It's not, I mean, outside of Ukrainian as well.
Patrice CNCF 00:44:35 That's a very good, point, good context. Thank you, Tiffany.
Well, I was gonna say we can always decide to stick to our… current policies.
Keep promoting and asking if there are any, Ukrainian… people who, I hope, are knowledgeable of OTAL, who can review, as opposed to just… people who know the language. And the reason I bring this up is because there is, especially at the beginning.
there's… An important opportunity and responsibility to choosing terms.
for the field in that language. And that happens only once at the beginning.
Severin Neumann 00:45:26 Hmm.
Patrice CNCF 00:45:29 And sometimes there's a quick way to do it, which comes… and then you're stuck with terms that you make… make you scratch your head and say, why did they choose that?
It's historical. So, maybe if we all feel comfortable just sitting back and sticking to our current policy, I'm okay with that.
Severin Neumann 00:45:51 Yeah. I think… I agree with you, and I think the other reason is, like, the moment we open that up and have, like, this massive localization in our project.
this closes the door for people to show up, right? Because you see this massive localization, and it's like, yeah, there's no service I can bring to the community, right? I'm not going to sit down and read those and peer review them anymore.
I think the… Yeah, let's maybe sit with that for another few days.
But I think the thing we should do, and this is a service that I'm very open to offer, is, like, to be allowed again in social media, whatever, to say, like, hey, we need people that speak Ukrainian, That'd help us with… making here a progress, right? I mean, there's no issue in that, like, sending out another social media post saying, like, hey, we're still trying to make this fly, we're lacking people helping us with that, and I could do this for any other localization as well, right? That's not coming with a lot of effort.
Patrice CNCF 00:46:55 I just had an idea while, you were sharing that another… service that we could do is, right now, when there are fallback pages, if somebody chooses the Ukrainian locale, and they're on a page that hasn't been translated, there's a banner at the top that says, by the way, this is in English, because nobody has translated it.
Do you want to help? Please come help. We could, for the Ukrainian localization, add a link to say, this hasn't been translated, please come and help, but by the way, here's a link to unofficial docs.
So this could kind of be a… semi-win-win?
Severin Neumann 00:47:41 So that we kind of semi-endorse Or appreciate the work that he's doing, and say, like, hey.
Patrice CNCF 00:47:47 Yes.
Severin Neumann 00:47:48 Here's a non-peer-reviewed Version that one of our…
Patrice CNCF 00:47:53 localization.
Severin Neumann 00:47:54 and contributors has… has been building, and he… he needs your help to… to take that over the finish line or something like that. Yeah, that's an interesting, interesting thought.
I like that.
Patrice CNCF 00:48:08 And we could just link directly to the… the mass… the big PR preview.
Or.
Severin Neumann 00:48:14 Yeah, I think the funny thing is, like, his big PR is rendering a preview The R?
So we technically could link to that, or we could link out to… I think he's doing his own rendering as well, if I remember correctly, like, from his own… thing, if I remember correctly, if you go to his website, there's a link to his… Ukrainian version or something like that. But yeah, let's… let's go back to that.
Patrice CNCF 00:48:44 So maybe to get closure, what is our position now? Do we… status quo, we don't do anything, or do we… one of us, maybe you, Severin, get back to Andy and ask him what he likes about our current proposal, which is to add a comment to the banner.
Severin Neumann 00:49:02 Now, I think, one, the most important one is, that we… push again and reach out via social media and everything, and say, like, hey, are you speaking Ukrainian? We urgently need people to help us with that. That's step one.
The other one, let's… Yeah, I'm… Let's maybe also… I think that, like, linking out to that… I, I, I'm just thinking, like, that, like, if someone would show up tomorrow and say, like, hey, I did a… Non-endorsed localization of whatever other language we maybe have already today.
Than… yeah, we could also link out to that, right? If it's a community member already, right? So… let's say Vitor is doing, like, a Portuguese version on his own, in parallel, just picking on you, sorry for that, and saying, like, hey, but I'm not, like, people are not reviewing it fast enough, but I have everything ready, and I just piecemealing it in.
I would also be fine with linking out to it and saying, like, hey, here's a non-peer-reviewed version of this page, right? Why not? I think I would be totally fine with that.
And yeah, Deanna, thank you for calling out that you could reach out to a few Ukrainian helpers.
Yeah, so I think I'm… I'm personally fine with that. Tiffany, do you… do you have any… or anybody else, if… have you any… any objections on that, or any… Any thoughts on that?
Don't let's do that.
Yeah.
Anything else? I have, like, an adjacent comment on that, so… Just wondering if there's anything left on the…
Patrice CNCF 00:50:53 I'd say that's… that's it for the, like, the main… for Ukrainian, localization in general, but we're still back to blog posts. Could… could we… well, do we want to adopt an official position now?
In terms of old blog posts, and just say… Just push back for outdated blog posts, and… not have them… well, it's more in terms of, do we have the bandwidth to review, and we're still in the same situation, that if there are no Ukrainian, localization folks.
Severin Neumann 00:51:26 That's… I think that's, for me, the point. I mean, if… if now Portuguese… Portuguese, I cannot pronounce this in English, or Japanese, are, like, have done 100% of talks, and, like, and are just looking for something to localize, and just like, hey, I'm localizing the 2022.
Patrice CNCF 00:51:42 Open Census blog post.
Severin Neumann 00:51:46 be that, right? I mean, at the end, we want those communities to be a little bit more self-sufficient.
But if now… Maybe we can give out a guidance again, and say, like, hey, de-localization teams, we recommend that you focus on docs first.
and then think about the other pages. And for blogs, we recommend that you do the most recent ones.
And old ones, we recommend not to do, especially when they're outdated, right? And then leave it… hand it over to, really, the communities to say, like, yeah, we are… we are driving that. And that also means, like, for the For the bootstrapping communities.
we are in the lead there, right? So we can tell them, like, hey, it's great that you do a block localization, but While we're bootstrapping that, Please pick Docs pert pages first, right? So it's not like us imposing something on the localization teams. How do you think about that?
Patrice CNCF 00:52:47 Sir?
Yes.
Severin Neumann 00:52:51 Awesome.
Again, I have also a tasted topic on that, I'm not sure if we need to hold 10 minutes on that, or… Just an observation, and that's based on what you also said, Patrice. Like, we have a lot of… Stuff on our plate.
With all the localizations, and right now, also blog posts, so, like, Growing massively, right?
I… at least I don't have a lot of bandwidth right now to write docs for docs, and it's like… a problematic situation, and then I guess, like, Most of us feel that.
I don't have a solution for that, right? I mean, even a lot of the blog posts are like, yeah, we should publish that. I mean, right now, and that's, of course, with KubeCon coming up, and GC election coming up, like, yeah, there's, like, a bunch of 12 blog posts or something like that, that… That just need our attention.
I don't have a good… Pined on, like, how we can… make our lives easier. I just wanted to… recognize and emphasize that, that right now I have the feeling that, like.
We spend a lot of time in maintaining and approving versus contributing ourselves, right? So… yeah, I don't know. Except that I appreciate everybody doing that, and also being understanding.
Or to understand full that, like, that's… that's not what we want to spend that much time on, so yeah.
There's nothing to be said about it right now. I mean, we can spin our heads around that, but it's not really that easy to be solved right now.
Yeah, except recruiting more approvers, like, recruiting more maintainers, and something like that, which is definitely also something I want to spend more time on.
and that's maybe also to… since we have a few new faces here, like, if you… want to get started here, right? If you have any questions, like, how can I help, what can I do?
ask us here, reach out via Slack, send us direct messages on Slack. That's always something where I am more than happy to carve out some time.
Because we can only get better by having more people helping us, and yeah. Docs is also getting more and more complex with, like, OBI, Profiler.
and a bunch of other projects that are just floating into our project. So even there, I think we… we need to think about different concepts in the future. So, anyways.
Patrice?
Patrice CNCF 00:55:47 A quick question about KubeCon that's coming up is, is anybody planning on, adding one a banner?
To a blog post.
And if the answer's no, I'm willing to submit a PR with a banner.
At least getting that up, because it's… In a month and a bit.
TH Tiffany Hrabusa 00:56:10 It's on… it's on my list for tomorrow.
Patrice CNCF 00:56:13 Both? Both the bands?
TH Tiffany Hrabusa 00:56:15 Well, I was going to do both, but… as we've seen, when something's on my list, it tends to migrate to later in the week, so feel free to put up the banner. I will get to the blog post this week, but… and hopefully tomorrow, but yeah.
Patrice CNCF 00:56:35 Glad to do that.
Severin Neumann 00:56:43 Deanna, you're raising your hand, so…
Diana Todea 00:56:45 Yeah, hi everyone. I wanted to say hi, and sorry for hijacking at the end of the meeting. Yeah, so, I was already, like, in contributing to the localization project for a few months now.
I know Patrice and Selerin, and some of you from some conferences, and yeah, I'll try to be, like, also present, to, to this community, well, these, meetings. It's… more European-friendly, I think. And yeah, I can also ask some Ukrainians that are in my company currently, and see if they could chip in, and any other way I can help as well, just let me know.
Patrice CNCF 00:57:35 Thank you.
TH Tiffany Hrabusa 00:57:35 Thank you.
Patrice CNCF 00:57:37 Welcome.
Welcome to the meeting.
Severin Neumann 00:57:39 Thank you.
TH Tiffany Hrabusa 00:57:43 I'm still working on the collector docs refactoring, and that's also on my list for this week. But Sophia and I have a meeting set up for tomorrow, so hopefully we will, actually make some progress.
the plan is to come up with a plan for moving the pages, which, as Patrice mentioned, is probably going to be better done in small chunks.
But we'll see how that goes.
And then, we're also going to be doing a gap analysis, so what is missing?
And what kinds of examples we want to add, and then we're going to be mapping those gaps and examples to SMEs and the collector's sake, who can best help us Fill in those gaps.
And then we'll go from there. But that's the plan for this week, is just kind of coming up with a plan for, how we're going to approach things. Just a quick update.
Patrice CNCF 00:58:40 Super, thank you. Maybe just to explain the, Reason to partition the changes into small chunks is that because link checking is done on canonical links. That means that whatever you move around, you have to update links across Alt the pages, and, doing that piece piecemeal is usually more manageable for everybody. Well, for reviewers in particular, but… For you in terms of what you're submitting.
TH Tiffany Hrabusa 00:59:15 Definitely.
Patrice CNCF 00:59:17 On the topic of link checking, as some of you know, I worked on parallelizing the link checking across locale groups. I'm… It's experimental, hopefully it'll work. I think this morning, we might have hit a first snag, so I'm going to be looking into that, where, because things are split up, we're not getting the same level of checking that we did before.
And so the Romanian… build, for me, a recent change is breaking link checking, but that didn't show up in our checks on GitHub, so I'll be looking into that.
Severin Neumann 00:59:59 Awesome, thank you.
Cool.
Finally, I think this Tuesday evening seems to work for a lot of people. I don't know what happened, but it looks like we hit jackpot on the time here. And even Fabricia said, like, yeah, normally he would join, but as he said he has a conflict just today.
So yeah, let's catch up in 2 weeks from now, and I said, if there's anything… Please let us know, ping us on Slack, on GitHub.
Yeah.
Took 2.
Patrice CNCF 01:00:34 Thank you. Thanks, everybody.
Severin Neumann 01:00:35 Bye-bye. See you next time, bye.
Sophia Solomon 01:00:37 Thank you.
