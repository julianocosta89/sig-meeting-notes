SIG: Browser SIG
Date: 2025-08-07
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 01:48 Hey? What's up?
It?
**Ted Young** 01:55 Yo yo! What's up y'all.
**Jared Freeze** 01:58 We're visiting Argentina. So we're all together today.
**Ted Young** 02:02 Oh, cool, nice is the company based out of Argentina.
**Jared Freeze** 02:13 No, I live here. So he came to visit me. Our team members as well.
**Ted Young** 02:20 Nice.
**Jared Freeze** 02:21 They started in California. I think it's it's all remote now.
**Ted Young** 02:29 We're in Argentina.
**Jared Freeze** 02:31 Quite a Cyrus.
**Ted Young** 02:58 So feel free to add things to the agenda.
**Dan Gomez Blanco** 03:32 Hello!
**Ted Young** 03:35 Hello, Hello!
Cool. Okay.
Alright. I've got a looks like we've got nice little backlog of stuff.
We don't have Martin today or RAM, but we've got the rest of us.
so let's kick it off.
The 1st item here is from Martin, who's not here? But has anyone actually like had a look at this pr.
so browser page, view event.
Do people have any thoughts on this.
**Daniel Dyla (Dynatrace)** 06:42 There is a comment left by RAM on the dock.
**Dan Gomez Blanco** 06:46 Yeah.
**Ted Young** 06:50 Yeah, use human readable valuables for type instead of 0 and one? If so, which ones I renamed this sorry. Go ahead.
**Daniel Dyla (Dynatrace)** 07:10 Yeah. So I think in the Sem conv he has human readable names in the enum right?
This is what we do for all of the other sem conf was suggesting that we use.
Oh, it's the opposite in any case, whether we decide to do like, regardless of which is which, I think we should go with what is commonly done in some comp which is human, readable, enums
**Ted Young** 07:48 Do you know.
**Daniel Dyla (Dynatrace)** 07:49 Organizations like making them numeric like. If you look at the the type enum in the body fields here, he just has 0 or one, and there's no description of it, you know. I I think human. Readable enum names are what the rest of semcom is doing.
**Ted Young** 08:09 Right.
**Daniel Dyla (Dynatrace)** 08:10 And then optimizations like, you know, numericizing them seems like a potentially a protocol level optimization. I don't know.
**Dan Gomez Blanco** 08:27 I also added a comment in terms of think it's in the.
in the schema itself to to use references. I think we're trying to like, we're basically have, like URL in it, which I think could be a reference to the existing URL dot full.
If that's what we're, I think that is basically a copy of what we're trying to do.
But yeah, so I'm I'm not sure if this was written before we're using like weaver like registry references and all that.
Maybe.
**Ted Young** 09:09 Sorry. So you're saying there's something.
**Dan Gomez Blanco** 09:12 No, not in this one, no, in this one is the on the URL attribute that has been.
**Ted Young** 09:21 This attribute.
**Dan Gomez Blanco** 09:23 Yes.
but is but it's below in the in the other part, in the schema, part in the yaml.
I think that should be automatically generated if we set the URL scroll. Keep scrolling down a little bit.
Yeah. So.
**Ted Young** 09:43 Here.
**Dan Gomez Blanco** 09:44 Yeah. So I think if we are Ref, I think the compilation will. Then, after compiling, it would just basically, yeah, use the definition of URL full, if that's what we're wanting to do.
**Daniel Dyla (Dynatrace)** 09:57 No, but it's it's because he has it as a body property. That was another comment that I was gonna make is, there's a lot of body properties added here.
It was my understanding that we were meant to be moving away from body fields when possible, and moving to attributes that was like the whole motivation for adding complex attributes.
And that body is left for either large binary payloads or you know, stuff like that, or or for the logs, bridges for them to to shove in stuff to say we don't really know what this is. If something's well defined. It's my understanding it's supposed to be an attribute, anyway.
**Dan Gomez Blanco** 10:46 Yeah, no, we might.
Yeah. I completely missed that. It was part of the the body? No. And you know, a top level attribute. Yeah.
But yeah, that makes sense. Yeah.
**Daniel Dyla (Dynatrace)** 10:58 Yeah, a lot of these things are bodies that I are body fields that I think should be attributes instead. I think that's just not because Martin doesn't know what we're doing, but because, this pr predates all of those policy decisions.
**Ted Young** 11:15 Right. So all of this in here, basically.
**Daniel Dyla (Dynatrace)** 11:18 Essentially, everything. Yeah.
**Ted Young** 11:24 So.
I think there's still like kind of this question around when we're taking stuff from a 3rd party source and putting it in here, I know to some degree we don't want to flatten those things right? So I think the answer would be that it would be a single complex attribute.
as the way we potentially handle this. If that's where all of this I kind of assume everything in the body here is down here, because it's the actual event from the browser. But I could be wrong about that.
**Dan Gomez Blanco** 12:17 Hmm!
I'm not sure.
**Daniel Dyla (Dynatrace)** 12:22 What event from the browser would you be talking about here?
**Ted Young** 12:29 Some kind of page view event.
**Daniel Dyla (Dynatrace)** 12:33 I I think I know there's a soft page view like draft specification right now. But I think a hard page view is just a page load. I don't. I don't know that there's an event from the browser that represents that because the whole.
the whole index load is the page view from the browser's perspective.
**Ted Young** 12:55 Right.
**Dan Gomez Blanco** 12:56 And actually here, I think we're the intention with this was to do it as fast as possible, right? So not even like wait for the load event, or or anything like that, just to count it.
Count the page, view.
**Ted Young** 13:11 Okay.
**Dan Gomez Blanco** 13:12 Soon as possible in the page load which leads me to another question, I think probably.
Well, I posted a comment on the general sort of like discussion rather than on the Pr itself, as in on the code itself. But the the I think, you know it's the intention of this event is not to measure any timings.
and maybe I'm not sure if we should make it clear there that the page view I'm just thinking of like legacy of other other solutions out there that currently basically put like the time in for, like, how long it took to load a page end the page view, event, and this is not intended to at any performance, and timers to this event.
**Ted Young** 14:01 I see.
**Dan Gomez Blanco** 14:02 So.
**Daniel Dyla (Dynatrace)** 14:03 The the note says, capture metrics.
**Dan Gomez Blanco** 14:08 Yeah. So that's why maybe we should be clear on like saying, this is only to count page views, and it will not be used for duration, and because then there will be another one. That will be the the page view, timing.
One that's measuring that stuff.
and I guess same would apply to like the soft navigations. If it's going to be another event to measure.
Times I click a button to the Sba loads and to get a root change.
**Ted Young** 14:41 This. This kind of gets back to this desire to have a document somewhere that's like our model, like our rum model, you might say, or our client model. Right? Like there are like, we are producing some amount of data. And that data is designed to paint a specific picture right? Like. There's this subset of browser monitoring that we're going after with this initial set of events.
And some expectations, for, like how these things should be used, and I feel like we don't. We don't. We might have that loaded in our heads, but we don't actually have it like written down anywhere, and that seems like a useful.
like a useful document, to to have.
**Daniel Dyla (Dynatrace)** 15:28 As someone joining late to this. That doesn't have it in my head. I would also appreciate that.
**Ted Young** 15:33 Yeah, so that that actually seems like like a high level task.
I'm curious if anyone wants to champion that who's on the call right now to at least coordinate with Martin and other people, to to kind of get it written down.
**Jared Freeze** 15:53 Yeah, I mean, we can. We can definitely get into that, you know. Cause I have.
You know, there's a lot of different ways. You can do stuff like that, right like is is a page view. Do they have to see something, or do we call it as fast as possible? Like, are you talking about that level of detail.
**Ted Young** 16:09 Kind of like, like, you know, there's We're trying to describe a model of computation right? There's a browser. Right? Browsers do things. They load pages, etc. They give us a certain amount of data. So we're saying, like the view, what we expect you to be able to see is like the sequence of page loads occurring within a session.
and that's going to be represented, you know, by this like set of events and spans and when you set up your dashboards for monitoring.
you know, browser like not library stuff, but but the browser Runtime, you know we think like this is like a good default set of dashboards right? And so it's like these are the things we want to observe. And because we want to observe this like pages, loading as part of a session, and like a set of dashboards for tracking errors and latency and whatever like. We're gonna generate this set of events and spans.
Okay, and yeah.
resources and things. And this is the model. And this is what you do with it. And then it's also super clear that we aren't doing things like like full dom session replay, or something like that, right? Like there's all kinds of other observability stuff. But we're not. We're not touching any of that right now.
**Jared Freeze** 17:34 Yeah, okay, cool. Yeah. We'll yeah. We'll look at that, because I feel, I feel like, you know, like soft navigation is neutered without timing?
So, yeah, yeah.
**Ted Young** 17:47 Right. So if we're not having that here, then we're saying we're not having that here because we're expecting to have these other performance timing events or something like that, right? And like, that's how you should be constructing this.
Yeah, I will create an issue for this. I'm just gonna add it as draft. For now define browser observability model, maybe thing.
Now for things like this, it does seem like, I want to start turning these things into issues.
I'm curious semantic convention or the Javascript repo. Where would we put this as an issue?
Maybe semantic conventions.
**Daniel Dyla (Dynatrace)** 18:47 Well, where? Where's the artifact gonna live?
**Ted Young** 18:51 I would say, if you're gonna.
**Daniel Dyla (Dynatrace)** 18:55 Google, yeah, Google Docs is not a good permanent repository of knowledge. It's not what we use in hotel. So I would say like. Likely there will be a set of design docs and whatever, and we'll want to keep those somewhere like a a decision record, and those would, I think, most likely be in the Js repo so I would put the issue there.
**Ted Young** 19:20 Would they? Or would they be in the the simcom repo.
**Daniel Dyla (Dynatrace)** 19:26 So there's nothing like that in some comp right now.
**Ted Young** 19:29 There is nothing like that in Simcom right now. But is that a good thing?
Like, in the sense of like with simcom like we have been feeling a bit of a push to be like when people maybe in the future like, can we create more room in Simcom? So when people define semantic conventions, they're also are defining some default dashboards and some suggestions, for, like how all this stuff is supposed to be used because it does feel a little weird sometimes when we're defining semantic conventions, and there's just no description, for, like what anyone is expected to do with this span or this event or something, and it seems a little obvious with Http. But maybe we're just getting into domains where that's less obvious.
**Jared Freeze** 20:18 Yeah. To me, the output of the model is some semantic conventions about how like we're going to model stuff and to me, having it on. The Js report looks closer than to the implementation side that we're not going to talk about that right now. Not this document. So to me. It makes sense as well.
**Ted Young** 20:39 How about this? I'll I'll raise it there, and that community can decide where they want to put this stuff. And if their answer is like we don't want it. Then we'll put it in the Js repo.
**Daniel Dyla (Dynatrace)** 20:52 Yeah, I guess a Google Doc is probably fine for the early part of the process, and the the more I think about it. The semantic invention should be.
you know, readable on its own. You should be able to implement a a semantic convention without going to the Js repo, if you're, you know, say.
developing an instrumentation outside of the Js repo and, like you said about Http.
all of the necessary, not necessarily. The the motivations behind the design decisions. But all of like, what do you actually do with this data is in like, it's it's codified in some conf, so I guess that's the that's the permanent home for it. So for a temporary place, a Google, Doc might actually be reasonable.
**Ted Young** 21:40 Yeah.
yeah. So why don't you all start by making a Google Doc version of this? I'll create an issue in Simcom. And I think this would be helpful stuff to have in Simcom in the long run is like some explanations, for, like how these semantic conventions are expected to be used I mean, I could see us backfilling some of the server stuff there as well.
But but that's like separate. I mean, this is like something we want to do with my team at Grafana labs. We are very interested in figuring out how to add things into semantic conventions to make dashboards as code. A more realistic thing like should be possible to generate Grafana dashboards and Percy's dashboards and stuff some kind of like default experience out of semantic conventions.
But we need to add a little bit more information to semantic events and set to work. Anyways, I wanna leave the rest of this meeting time, though, to I see there's a test harness plan on the agenda, and we only have 30 min. So I think I want to close this out and maybe hand it over to Joaquin.
Yeah.
**Jared Freeze** 22:56 Yeah, I can share my screen. I guess you can share. Yeah, or well, hold on. Let's see. Hold on.
Hmm!
Let me just pull those.
Let me see.
let's see.
Yeah, I don't know which one's gonna be sorry. Hold on one second. Can you share just for the sake of time, because we don't have set up the permissions. Probably if I start the Zoom Meeting.
**Ted Young** 23:37 Sure I can share.
**Jared Freeze** 23:39 Laptop.
**Ted Young** 23:42 How's that?
**Jared Freeze** 23:43 Yeah, that's great.
So yeah, basically, what I put up here in this document is what we're doing on embrace to test our own SDK, when I define, I define here the scope of testing is, what what do we want to test? Or the reasoning like under his test? So basically, it's like.
are we submitting the right stuff? Are we getting the right information? Is information going through the from the SDK to the collectors and the servers. Are we impacting the browser in a way that is actually impacting the user? In terms of like, how much time it takes to load the SDK the CPU usage or the memory.
How compatible is the SDK across all the browsers that are out there.
and then how it works with different frameworks like react angular view whatever, and then how they work in combination with different bundlers like Webpack beat band, and the rest of them.
Then what I define is where we're going to run this test. So what we have is, we have a really really simple like Demo App, in a way that is only used to run the test.
I was thinking about the open Tremity Demo App. But then I saw that it's really complex, that it runs a lot of things. So maybe we can have something similar. But it's only like Ui with some hard coded or mock back end like we are not testing back in here. So it's fine.
And then what we do have locally, we have this like mock collector where we send an entry to. But it's a basically a node server that runs with the test. So we know when data reaches the collector, and we can see the data there and see that it's correctly serialized. And like, basically, we want to see that it reaches the right place in the right format.
That's something that we run directly. So I'll recommend doing something like that. Now, if you can scroll down so pretty much, I divided the test cases into, I think, 3 tests that are different from each other.
The 1st one is just make sure that we build like in the web is really not as easy as know that if you import a package that pretty much works.
You have to be sure that the target that you are targeted in the the vendor, that you're using everything works together. So we have a set of like a metrics of tests.
Pretty much. It's like, Okay, now, we're going to build with Webpack version 5 and es, 2020 import in our SDK, build everything to it, and just make sure that that doesn't crash the the bill the bill that the consumer is going to use. So that is one set of tests.
The next set of tests we use the output of this 1st test to measure how big is the baggage that we are creating, based on what we are adding to the to their app application.
So, for example, we have a Github action that runs on all our Prs.
And it will add a comment, basically, that says, All right. With these changes the SDK is now a hundred Kilobytes, 200 kB, whatever.
and we can compare that across many bundles that they may bundle the app differently. So you have an idea on like, how are you going to impact the end user.
And then, we thought it was important to test how is the like? What's the impact of the application on the load on the load of the page. Basically.
we are running lighthouse. I'm pretty sure you know it. We run lighthouse on an app, a simple app that knows our SDK, and then we'll get some metrics from them. In this case we get like total blocking time men trade time and script validation time.
So this, what we're looking for is is the end user, having to wait longer times because the SDK is running on the background when the page loads Let me know if you have any questions. I'm trying to fit it in time, but you can add comments, and we can talk about it offline.
But yeah, then the next set of tests are, I think it's measuring performance if you scroll down. So the last yeah, sorry this one are just measuring that it actually works like.
if we create a span in an sorry, it sends a span to the server. If we create a log, it sends a log to the server.
And then it's also testing it on the different conditions that the browser may have like. For example.
when you load the page like, do you create all the auto instrumentation that you have in place when you navigate to another page? Do you create a navigation event when you close the browser, that's all. Your telemetry is sent to the the collector or no like, do you, miss? Do you lose something? If the user closes the browser. If the user closes the tab, if the user refresh a page.
one of those scenarios that may be tricky because you may have data in flight, and then the user closes the the tab, or where you want to see what happens there. So we have a bunch of tests running down.
And I think. Lastly, I have performance testing.
Yeah, on the end.
So yeah, this is what I was talking about, like different scenarios where that ends the session or ends the current like browser activity. And then you want to know what happens there?
And lastly, I am testing also, like stress, or like doing some sort of stress testing where I will create a lot of spans and see what happens. Like, is it browser, tab slower or like? Are we adding a lot of load time to the browser to the user that they have to wait longer for their own stuff like they click something and they have to wait longer for something to happen, because we are creating a span or log in the middle.
So for this I'm using mostly chrome devtools that you can get all the metrics from.
Basically, you have a setup where everything runs on using playwright. So I have the playwright end-to-end test set up in a way that I run all these scenarios. Then I get metrics from chrome, the headless chrome browser that is running the test.
And I output all this into a Pr comment. It's another. Give a list of action.
and I can't compare now like what the things that I'm doing. How are they affecting? Also, I think it's been a while since I've used this. I think I have a few a list of metrics that I wanna I use to compare. Maybe if you scroll down. No. So here I can share.
They want sample of the Pr comment that we have with all the metrics.
But yeah, that's pretty much what we're doing right now.
The thing, is it? It requires some setup, like, for example, we have to set up play right. You have to set up this fake collector that gets all the telemetry where you then look at.
and a bunch of other stuff.
But yeah, I don't know if this is what you were looking for, or if this is useful. But to me it's a good starting point, at least.
**Ted Young** 31:02 I think it's super useful. I mean, I'm curious how portable that test harness code is, and like how much we could literally reuse it as like a baseline for setting all this stuff up.
**Jared Freeze** 31:16 I think it's really real. So like at least the way I'm as I'm setting it up.
It doesn't really matter like you have, like 2 separate things, right? You have the framework that runs all the tests. And then, on the other hand, you have the page that is being tested.
So the page that is being tested maybe like it has embrace code because it's what we are testing. But you can change that. You can use the base. SDK, right? And just to test over that. But you can keep using the same framework because the framework doesn't know what is going on on the test page.
**Ted Young** 31:50 Yeah, we're we're out of time.
This is great. I think this is fabulous. So we need to get through these semantic conventions, you know before we can move to testing. But I think I'm really excited to see this. I think it's a just the right amount of testing for us to get started with.
**Jared Freeze** 32:10 Yeah, I'm happy to share the set. I mean our repos of it. So I'm happy to share the links to where the setup is.
**Ted Young** 32:17 Yeah.
**Jared Freeze** 32:18 My only concern will be if we are doing this on the Js repo it may overload the like. The non js, the non browser part, because, like, we're going to start running playwright tests on end-to-end tests on the browser, helpless.
And then we are going to start building the SDK on every Pr. And all that stuff that it may not be related to know.
**Ted Young** 32:47 There's definitely a question for the the Js community to decide how they want to deal with it. But in the short term, do you mind just posting posting this stuff to like the slack channel and asking for more comments? This is great.
**Jared Freeze** 33:02 Yeah, yeah, I can share again, the Google, the Google Docs. And I'm also happy to share the link to our own red bull where you can see how it works.
**Ted Young** 33:11 Awesome.
Alright. See you all on slack.
**Jared Freeze** 33:14 Right.
