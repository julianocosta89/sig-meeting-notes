SIG: Android SIG
Date: 2025-09-30
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/D9QEEQqHGLmkgM9mGA1xcnNCI5nSAIzFrKHcPx3ecNLSyDtSVCu15loYkBpuJeA.odTqvaDrJ99QDhpI
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:25 Good morning.
**Mustafa Haddara** 00:30 Hello.
**Cesar Munoz** 00:31 Hey, good morning.
**Jason Plumb** 00:46 I am supposed to be volunteering later today, but I don't think they want me to bring whatever this cold is that I have over there, so I'm not going to be able to.
Which is a bummer.
Still getting set up over here.
Okay.
How's that working? Okay, good, good, good, good. The other day, I opened this document, and this Android was, like, massive. It was like… it was like that. It was just for no reason, it was just big.
So someone… someone was getting creative, and it wasn't me.
And sometimes, sometimes they'll just be, like, random, like, somebody, like, leaned on their keyboard, or the cat walked across, or whatever, it's funny.
**Mustafa Haddara** 01:56 It sounds like you're trying to disavow it, you know? Like, 100 was huge, but it wasn't me, I swear, guys. Yeah.
**Jason Plumb** 02:03 No, I saw it too.
**Cesar Munoz** 02:07 I think Google Docs has a history of changes, you know, just like Git.
**Jason Plumb** 02:13 It does, you can't follow it that well, though, right? Like, it's pretty… I don't know.
There has to be hundreds, right?
Well, maybe not.
Anyway, it's just anonymous users, it's not gonna be all… oh, look at this! Yeah, so that was me moving it back, I don't know, something weird happened. Oh, look at that! Yeah, yeah.
**Cesar Munoz** 02:40 Yeah, it's religious.
**Jason Plumb** 02:42 Anyway.
**Cesar Munoz** 02:43 Issue with mouse or something.
**Jason Plumb** 02:45 Yeah. Cat. I blame… I blame the cat.
Okay, well, I've front-loaded some stuff, let's get through kind of quickly and make sure we get some other… other folks represented in here, and if I have to go on mute all the time, I apologize.
**Cesar Munoz** 03:02 No, Chris.
**Jason Plumb** 03:06 Okay, so I didn't link to the blog post, why not?
Let me open it up.
**Cesar Munoz** 03:16 I think you had it in the Slack group.
Let me check.
**Jason Plumb** 03:21 I did.
Can't imagine that it got merged yet, yeah, here.
Oops.
Why is copy-paste not working?
Now you're gonna watch me do it.
Weird.
Okay.
Right, so I thought that this would be a good idea for us to…
try and solicit some feedback from users around the APIs, and the thoughts around going 1-0. It's also, just making our intent a little more public, and getting, like, full transparency and feedback from folks, so…
I think…
I mean, I welcome everyone to go ahead and read this if you have feedback on it, but
The main takeaway is that we've got an issue that's linked down below.
It looks like there's some more feedback I haven't seen.
This thing… Hopefully copy and paste will work now. Alright.
And I placed this in specifically with the hope that people would see this link in the blog post once it gets published, and then they could come into here and start leaving some feedback. So that exists. Please feel free to give it a read-through and or some…
some feedback, before it gets published. Hope… I'm hoping… was really hoping it'd be yesterday, but maybe sometime this week, probably, is when it's gonna go out.
Assuming that we're close and there's no critical feedback on it yet.
And then, I think I went ahead and asserted in there that our next, release.
In October would be our RC1, and I wanted to check in with people here to think if that's, if that's reasonable.
**Cesar Munoz** 05:24 I don't have any problems with that.
I actually think it's a good idea to put a deadline, so that, you know, It's always helpful to…
Probably prepare better.
Or plan better.
Based on what we discussed, it's only one module that we're planning to actually release a stable.
And… I don't think there's really much left, we… Could add to it, or…
I created two PRs that… that are the only changes that I'm aware.
I wanted to try and add before going stable, but… Apart from that, I mean, I don't see…
too much work left, you know, for that money, so… I think it's fine in October.
**Jason Plumb** 06:16 Cool. At least for RC1, you know, and we can do an RC2 if we want to.
But at least for our students…
**Cesar Munoz** 06:23 Just to make sure, RCs are still… changeable Like, in a breaking way.
**Jason Plumb** 06:32 Yes.
But we want to try to minimize the changes. Go ahead, Mustafa.
**Mustafa Haddara** 06:37 I was gonna say exactly what you said.
**Jason Plumb** 06:39 Okay.
**Cesar Munoz** 06:40 Got it.
**Jason Plumb** 06:41 Yeah, it's available to change, but we really don't want to unless we feel like it… like, it allows us the opportunity to make changes, but we're gonna try and avoid doing that if possible.
It's kind of like a dry run.
**Cesar Munoz** 06:52 Sweet.
**Jason Plumb** 06:53 Damn.
Okay.
Sounds like yes.
If you disagree with this, now would be a good time to voice it. Otherwise, you can voice it in the issue.
Cool, let's move on to the next one. So, I was thinking about the logistics of doing this, right? So the intention is to add an alpha suffix to everything. Right now, nothing publishes with an alpha suffix.
So… our Android agent, once we get past RC, like, our first RC will publish this…
Is that me beeping?
What is that beeping?
Okay, whatever.
**Cesar Munoz** 07:35 I don't hear it.
**Jason Plumb** 07:36 Good, it was probably something on my end. It was… something was beeping like crazy.
Alright, so the Android agent will release like this next month, and then every other module, and I just picked one as an example, their version would release as 1.0 RC1 Alpha.
And then, once we get past RC, Then these become… Then after… stable. Then these become…
You know, we drop the RC1, is all we do. But this maintains the alpha.
So, is everyone on the same page about this? Like, this is where we will end up after we're RC. And actually, what do you think about this order? Is it RC1 then alpha, or is it Alpha, then RC1?
**Cesar Munoz** 08:29 I'm not sure, because I usually don't… I don't work with RCs, but… I guess from a…
Automation point of view, it will be easier to do that order that you added.
First, because then we'll just set version 1.0.0-RC1.
**Jason Plumb** 08:49 Right.
**Cesar Munoz** 08:50 And then the alpha will be added to everything else.
**Jason Plumb** 08:54 Okay, I think I agree with that.
And then, I'm sure…
**Cesar Munoz** 08:59 It would be easier. I'm not sure if it's correct, but it would be easier.
**Jason Plumb** 09:02 I think I agree with that, and then I think we will need to do some build work to make this happen. I think there's probably a few places in the release process that don't…
Handle those suffixes correctly yet.
So that probably needs to happen in the next couple weeks.
**Cesar Munoz** 09:23 I can take a look at that.
**Jason Plumb** 09:26 That's cool, thank you.
Okay, Jamie, did you have something you were gonna add? I just saw you come off mute, sorry.
**Jamie Lynch** 09:44 No, I think it's fine as long as…
Like, as long as we're kind of noting that alpha means that the…
But when it's not, like, stable. Yeah, I think…
My initial instinct was it looks slightly strange to have alpha and RC in the same version string, but I also don't really care that much.
As long as the intent is fair.
**Jason Plumb** 10:14 Yeah, I understand that.
**Mustafa Haddara** 10:21 Do we have to version all of the modules at the same… number?
**Jason Plumb** 10:25 We… we do.
**Mustafa Haddara** 10:28 Okay.
**Jason Plumb** 10:28 I mean… Yeah, I think trying to version them separately would be a nightmare.
Or even one of them separately, I think, is…
**Mustafa Haddara** 10:37 Yeah.
**Jason Plumb** 10:37 a lot of work.
But I am now thinking about whether or not we could, like, drop the RC1, since we're kind of not…
we're not going stable with it, so does… do the modules, the other non-agent modules, do they need RC1 at all?
I guess that's something to think about, Cesar, when you're looking at this.
**Cesar Munoz** 10:58 I'm thinking right now, if… we have to release another RC
and we didn't add it to the other modules, then that probably could cause some crash… clashes in the… in Maven Central.
**Jason Plumb** 11:15 That's a good point, right? So if… if…
If this didn't have RC1, and we needed to do an RC2, then we'd be trying to publish the same module into the same version again, and that would be a problem.
I think it's easier if we include it.
It's kind of more consistent across the project than…
Okay.
**Mustafa Haddara** 11:50 So, in this scenario.
All of the packages are… we're versioning all of the packages at the same version number so that we know these are the versions of the stuff that works together.
And for agent, we're just calling it 1.0.0RC1, because that's going to be our 1.0 release.
**Jason Plumb** 12:09 Yeah.
**Mustafa Haddara** 12:09 All of the other packages get that exact same version code with the dash alpha suffix to signify, yeah, we know the number says 1.0.0, but actually it's not stable yet.
**Jason Plumb** 12:21 That's right. Yeah, I think that pattern is pretty well established elsewhere in OpenTelemetry, at least on the Java projects it is, and I'm pretty sure elsewhere. I wonder if there's a…
I wonder if there's, like, a…
I mean, it's an industry term, so I don't know that they've called it out, but let's… Maybe…
Yeah, maybe in here…
**Mustafa Haddara** 12:50 Oh, yeah, yeah, go back. There was… on one of those search results, on the .NET search result, third from the top.
**Jason Plumb** 12:57 versioning.
**Mustafa Haddara** 12:58 Pre-release packages are denoted by appending identifiers such as alpha, beta, RC.
**Jason Plumb** 13:05 I wonder why that's called out… like, it's also called out here, so maybe we should also…
**Mustafa Haddara** 13:10 Yeah.
**Jason Plumb** 13:11 Yeah.
Yeah, to the point… to the point that it should be… it should be findable or understandable for users to understand that if it's marked with alpha, that it's not stable, even though it's a 1.0.
And we have semantic versioning.
Alright, let's make a note of that. I think,
Okay.
And then there was… there were a couple asks already around,
kind of additional documentation, specifically getting the Android stuff into the registry.
And by stuff, I mean the instrumentation.
So I think the goal would be to…
For users to be able to come into here. Now, this is where it starts to get weird, is… do you go Android?
I think you do, even though it's not really a language.
But I think, like, Swift is in here, arguably that is a language, and there's no iOS in here, but I think we would probably just put Android in here, and then we'd be able to see all of the instrumentation modules for it. I think that was the idea.
in… In this feedback, I think.
Yeah, Severin had some feedback about this, so…
**Cesar Munoz** 14:56 Yeah, because right now that's, it's an empty.
**Jason Plumb** 14:59 Yeah, yeah, exactly. So, you know, there's some requests to have the docs fleshed out.
I'm not gonna use some help.
Okay, anything else on this topic of alpha and RC suffixes?
Okay, I will also, I think I added…
an issue in the website repository to add stuff to the registry, but I will also take an action item
So that at least we don't lose track of that.
Okay.
Let's move on to the next item.
Sorry for writing the mute so hard,
Right, so something when I was thinking about, stability and ease of use and the agent API, right now we have a way to specify the ingest URLs, and that's great.
But I'm curious about, any sort of authorization or authentication mechanisms that vendors might use. I was thinking about the way we do it.
We just have a token that you provision in the UI, and then you put that token into your app somehow, and then that token needs to come across as a bespoke header value. And, I'm curious how other vendors do it, and if we want to make that a first-class part of the API.
Now, that doesn't have to be for 1.0. I think if we do it right, we can probably add it later. But I just think that, for users coming in and seeing this, I think that's one thing that they're going to be evaluating, is the ease of use.
**Mustafa Haddara** 16:44 And I want it to be easy.
**Jason Plumb** 16:49 So how do other vendors do that?
Headers?
**Cesar Munoz** 16:54 Yeah, as in Elastic, it's an out header.
**Jason Plumb** 16:57 Okay.
Right now, the…
**Cesar Munoz** 17:01 Initializer allows you to, set headers, you know, as a map.
But not specifically this, you know, authorization one.
**Jason Plumb** 17:13 Oh, it does? You can?
**Cesar Munoz** 17:16 Yeah, you can… Yeah, let me show you.
**Jason Plumb** 17:22 Yeah, sorry, I… oh, that's the wrong repo. I am very much not awake yet.
**Cesar Munoz** 17:27 Alright.
**Jason Plumb** 17:35 Oh, yes.
Okay, and those are the same for… metric.
**Cesar Munoz** 17:44 by default, those…
**Jason Plumb** 17:45 Yeah.
**Cesar Munoz** 17:46 Yeah, that goes to the whole… all of the endpoints, but you can also…
You know, set a specific endpoint.
Differently, if you want.
**Jason Plumb** 18:01 I think this is enough, then. I just wanted to see if there were any users that do anything special, or if they do anything different than a header.
I know there are… go ahead.
**Jamie Lynch** 18:15 I know that Embrace basically creates a subdomain based on the project ID, but we're… we're not actually exposing, like, a hotel collector endpoint.
**Jason Plumb** 18:26 Okay, so the subdomain is, like, based on customer?
**Jamie Lynch** 18:31 Yeah.
**Jason Plumb** 18:31 Okay, and… Request or sending of data to that subdomain is not verified or authorized or authenticated at all?
**Jamie Lynch** 18:41 Yeah, but I think there's a…
Header, similar to how everyone else is doing as well.
**Jason Plumb** 18:46 Okay, cool.
**Mustafa Haddara** 18:53 Honeycomb's using an auth header, and our… in our SDK, we're not using the endpoint, or the API that,
Cesar just pointed out, we just create our own span exporter.
**Jason Plumb** 19:06 You do, okay.
**Mustafa Haddara** 19:07 Yeah, yeah.
**Jason Plumb** 19:08 Is it OTLP?
**Mustafa Haddara** 19:10 Yeah.
**Jason Plumb** 19:10 Okay. Is there a reason why you're not using the built-in ones, or the ones that we create for you?
**Mustafa Haddara** 19:16 We have a… toggle… like, we have an option to let users configure either HTTP or gRPC.
**Jason Plumb** 19:24 Okay.
**Mustafa Haddara** 19:26 So our SDK takes a…
a Boolean, and it's like, oh, okay, gRPC, let's create that spanexpert, or HTTP, let's create this other one. And we just set the headers.
**Jason Plumb** 19:36 Okay, okay.
**Mustafa Haddara** 19:37 Yes, I don't hear you.
**Jason Plumb** 19:38 Makes sense.
Alright.
Well, it sounds like we've supported the 90…
percentage case already, so it sounds like there's nothing else to do on this. I somehow, when I wrote this, didn't realize that it was already exposed directly.
And it's, like, the first thing, or it's the third thing, so clearly this was already thought about, and I apologize. Alright, let's move on.
Registry, we already kind of talked about that. I have a tracking issue, in case you hadn't seen or heard this. Here it is.
Yep, that's all.
It's in the I.O. repo.
Okay, and we are only 21 minutes in, Serbi, so I think time is allowing, even though it looked like I front-loaded a lot, I think you're in line.
**Surbhi A** 20:39 Awesome. Yeah, I… seeing the agenda, I thought it might take longer.
So this one is about… adding… certain events to HTTP spans.
Currently, we only get the total request duration from a span.
And we do not get granular details, like how much time was the DNS resolution, the TLS setup, the connection setup, and then how much time the server processing took, the payload uploading took, the response downloading took.
So these are valuable metrics that a backend can derive.
and show as a drill down per request, right? Currently, there are metric signals.
for certain things, but they do not… they aggregate everything at the agent level and send it to the backend, right? There is no per-request correlation there.
And also, there are no metrics around these things right now.
So… Yeah, I proposed, the… these certain events, like.
breaking down the lifecycle of an HTTP request to the semantic conventions repo, where I suggested what names we can use, perhaps, for those events. Name and timestamp matters the most, we even don't need attributes because they are already part of the span.
So the backend can take it from the span itself.
So… Hoping we hear this gets through.
And also, there is, I, like, last time when I joined the SIG,
I did not have a chance to read the comments, I'll take a look.
But yeah. So last time I joined the JavaSeg, I heard that there is a separate proposal wherein we want to do away with span.events, and instead use standalone events, and
contextually correlate them with the context to the span, but that is underway, right? Right now, the way we have is the add timestamps, the add time events API, right?
So, I think we can, in the interim, until that is approved, do this as a solution.
**Jason Plumb** 23:10 Yep. So, span events, long-term are going away in favor of just events that have, span correlation.
That's… that's the long-term approach. It's actively being worked on by some folks in the spec repo.
But yeah, I think in the short term, it's probably fine. That API, it's probably going to be around for a while.
And they will probably have a configuration that will allow it to bridge.
So, even when you call span.adEvent, it might generate A log-based event.
with…
**Surbhi A** 23:43 And…
**Jason Plumb** 23:44 Yeah.
So… This is great. I think there's…
for some libraries, you can't get any of this stuff, right? Like, if you're using…
HTTP URL connection, for example, I don't think you can get any of this.
**Surbhi A** 24:01 Yeah, some of it we can.
Yeah, but, like, the DNS connection and TLS, they are all bundled into one, because it's a black box, we just know the connection timing, and not individual timings, yeah.
That's true.
**Jason Plumb** 24:18 pretty deep.
**Surbhi A** 24:18 He is a good one, which allows us… which gives listeners for all of this.
But, like, this is sort of an exhaustive list.
It makes sense for all of it to be defined, and then whatever the instrumentation can possibly use, they can use.
**Jason Plumb** 24:36 Yeah, this seems like a very reasonable start to me. I will leave some feedback on that. And then what was the other one?
**Surbhi A** 24:43 And then in the Java instrumentation repo, we have the OKHTTP instrumentation library, which is what we use in OpenTelemetry Android as well, parts of which to create the automatic OKHTTP3 instrumentation. Yeah.
I proposed we add that OKHTTP listener, wherein, which takes the span and adds the events as the callbacks happen for each of these phases.
So, if that is added there, then both
Consumers of manual instrumentation can use it.
And we, at our end, in the OpenTelemetry Android, can take that listener and put it in the OKHTTP client during our auto-instrumentation as well, and we can leverage it as well.
**Jason Plumb** 25:36 Cool, and then is the idea to show these events, like, along, within a session, like, some sort of drill down, like, let's say you're looking at a session, the user did something that made an HTTP request.
Is the user… is the intent for the user to be able to go in and see these individual data, or is it for the… is the intent for it to be aggregated across certain calls?
**Surbhi A** 25:58 Oh…
**Jason Plumb** 26:00 Could be both.
**Surbhi A** 26:00 Yeah, could be both. So Splunk has troubleshooting metrics and MMS. So, like, showing the P95, P90, P75 stuff for DNS resolution, those charts.
**Jason Plumb** 26:15 Yeah.
**Surbhi A** 26:16 And individual drib… like, correlation to the individual request is important as well, but yeah, that is not yet completely defined, but that's the goal, to have exact timestamps, so we can work with it.
**Jason Plumb** 26:29 Okay.
**Surbhi A** 26:40 I can, yeah, maybe, work with the product here and get those bullet pointers about how we are going to leverage it.
**Jason Plumb** 26:53 So, I don't… I haven't read this yet, but it seems like maybe there was some pushback about the length of verbosity. Span events, if I'm… if I… from memory, span events cannot have attributes, is that true?
**Surbhi A** 27:07 It can.
It can have attributes.
**Jason Plumb** 27:11 So, there could be, rather than having separate events for start and end.
You could imagine an event that's just DNS, HTTP, DNS, and then there's two different attributes, maybe?
Same with connection, TLS. Each of these kind of has…
two facets to it, so if the event was just… HTTP request header.
And then that event could have two different attributes on it, and I can put this in the issue as well, just as an idea.
That just shrinks the total number of events, and allows you to maybe more easily calculate durations.
In the cases where you can. I mean, if everything's optional, then you have… all bets are off, like, you have no guarantee.
**Surbhi A** 27:51 Yo.
**Jason Plumb** 27:51 Calculating durations for, like, how long does it take to do the TLS?
session start, or whatever, handshake.
If both of those attributes are on the same event, it might be simpler.
**Surbhi A** 28:04 Yep.
**Jason Plumb** 28:05 Yeah.
**Surbhi A** 28:06 That reduces the number of events, but it… does it fit the… like, a span is supposed to have a duration.
But an event is a timestamp.
And an event that happens at that timestamp.
**Jason Plumb** 28:22 Yeah, yeah…
**Surbhi A** 28:25 We don't even need attributes, we just need the event timestamp and the name.
**Jason Plumb** 28:32 Yeah, I understand that. Like, if, yeah, if you collapse these into one event, then how meaningful is the timestamp? Like, what do you even do with the timestamp?
**Surbhi A** 28:40 Yo.
**Jason Plumb** 28:41 Yeah.
Yeah… interesting.
**Surbhi A** 28:48 And hopefully… Timestamp is…
a higher level attribute than attributes, adding to… but yeah, I don't think it adds much.
**Jason Plumb** 28:59 Okay.
**Cesar Munoz** 29:00 It's also probably… Or maybe, definitely, at least at the beginning, something we can…
You know, when we implement it, it could be opting, you know?
**Surbhi A** 29:10 Yeah. So only the people that want that amount of…
**Cesar Munoz** 29:13 data.
You don't get it.
With them, then we wouldn't, you know, wouldn't be a problem.
**Surbhi A** 29:20 There's a configuration flag in all the instrumentations. If that is turned on, then they get these events, otherwise it remains the same for them as it is right now.
**Cesar Munoz** 29:31 Yeah.
I'm just wondering on what you mentioned about not all HTTP
Clients providing this kind of data.
If I understood correctly.
**Surbhi A** 29:46 Yo.
**Cesar Munoz** 29:47 But they do provide…
**Surbhi A** 29:49 Yo?
**Cesar Munoz** 29:51 They do provide at least the duration.
Like, is that a constant? Because…
Maybe there could be, like, a third… Whoa.
Yeah, but it's not exactly an event, because… Yeah, duration is, like, yeah.
No, never forget, that's hurry.
It would be nice if we could get it from, like, at least for most of the clients,
But again, at least for Android.
probably OKCDP is really the one
We should care about the most, probably.
**Surbhi A** 30:30 Yaw.
Like, even for… there are… Ways, crude ways.
Like, in HTTP URL connection also, there is a crude way of getting these details, if we wanted to.
That probably doesn't make sense in an automatic instrumentation, but, like, you can call those steps separately.
And get those details if an instrumentation wanted. So sometimes… depends on what details you want, yeah.
**Cesar Munoz** 30:59 Got it.
It overall sounds good to me, Survey. I really don't have…
much to say, because I haven't had the need to gather these information yet.
But, it's, it's, it's great that at least there's an issue there, and, you know, hopefully it gets, it gets through.
**Surbhi A** 31:25 Awesome. I'll try to justify that how backends can use it, so it's more,
Like, we can pursue the… Group more to get it through.
**Jason Plumb** 31:40 Yeah, I think… I think having that just helps to solidify the utility of it in my brain, like, knowing how it would be used helps to influence the design or the modeling of the data, somewhat, and…
**Surbhi A** 31:53 Yeah.
**Jason Plumb** 31:53 My supposition, like, what I… what I guess is that,
It's app developers using a RUM product that are like, oh yeah, every call to X service is taking Y time, and that's, like, hindering or making the user experience worse.
And then you go talk to that team, and they're like, our service is fast.
Like, well, here is the breakdown. If you have the breakdown, then you can see in a slow, in any request, how long you're spending in each of the phases, and I think that can sometimes be really informative.
Yeah.
**Surbhi A** 32:29 Yes, and like, if we… Generally, you get histograms from metrics, like, there are no metrics around it.
But, like, that doesn't include exact durations, so showing the… but I'm not sure if already metric histograms would show the…
75 percentile, 90 percentile, for each of these phases. Those graphs are also important.
**Jason Plumb** 32:59 Yeah… This kind of stuff might be an interesting use case for… Four metrics on mobile.
**Surbhi A** 33:09 Yes, yeah.
**Jason Plumb** 33:12 It's not without the same problems that we always talk about, but it's… it is… it's maybe a little different, because it's so network-focused.
But, like.
**Surbhi A** 33:23 Oh my god.
**Jason Plumb** 33:23 But, like, a TLS handshake, for example, if it's computationally intensive and you're running it on a crappy device versus a modern device.
Those two CPUs are gonna have very different performance characteristics.
**Surbhi A** 33:38 Yeah, but then we will probably have those attributes as well to drill down with.
we have the… Yeah. Device, name, manufacturer.
**Jason Plumb** 33:50 Good day.
That's interesting, though.
**Surbhi A** 34:01 Do put your concerns or, like, positive, push for it.
**Jason Plumb** 34:14 That's cool.
**Surbhi A** 34:15 Awesome.
**Jason Plumb** 34:20 Okay, anything else on the HTTP…
Semantic conventions that we're talking about.
**Surbhi A** 34:27 Nothing else.
**Jason Plumb** 34:29 From anyone else?
**Surbhi A** 34:30 Should I tag somebody from… who worked on… I'll, maybe tag,
the person who created OKHTTP3 manual instrumentation in the Java instrumentation repo. Any people we could tag, if you guys can know and can tag.
**Jason Plumb** 34:51 Yeah, that's not a guarantee that they will see it, though, like, even if we leave a comment and mention them.
**Surbhi A** 34:57 Yum.
**Jason Plumb** 34:57 That doesn't mean that they'll get notified.
Because that's a… it limits the abuse, the potential for abuse. Like, if I just came in here and started spamming in people's GitHub handles, and they get notified, I could do that across a lot of repos or a lot of issues, and that would be…
you'd basically be flooding people's inboxes. So they… they don't allow that unless the person chimes in first.
**Surbhi A** 35:22 Got it. Good to know that.
**Jason Plumb** 35:25 But the community's not that big, and you were on this SIG call in Java last week, so…
**Surbhi A** 35:29 Yo.
**Jason Plumb** 35:30 I can also reach out. Do we know, like, who are you… who do you think you want eyes on this? Like, Lori or Trask or someone? Whoever wrote it originally?
**Surbhi A** 35:39 Okay, I do not know who wrote the semantic conventions around HTTP originally, but…
**Jason Plumb** 35:45 You're talking specifically about the semantic conventions.
**Surbhi A** 35:48 Oh, no, I was talking about the Java instrumentation…
**Jason Plumb** 35:54 Okay.
**Surbhi A** 35:54 person who created the OKHTTP3 manual instrumentation. I don't know how to pronounce its name, but it starts with M.
**Jason Plumb** 36:01 Mateus, yeah.
**Surbhi A** 36:03 Yo.
**Jason Plumb** 36:04 He is no longer part of OpenTelemetry, sadly.
**Surbhi A** 36:08 Okay…
**Jason Plumb** 36:10 He was my coworker for a few years.
He did a lot of work in the instrumentation repo, and then he went on.
**Surbhi A** 36:17 Okay.
**Jason Plumb** 36:21 But yeah, I mean, the maintainers over here can help out with this, too. And there's a lot… there's a lot… there's a good brain trust over there.
**Surbhi A** 36:27 Okay. And I think it is already marked for triage, so I think I'll wait for the process to take it up.
**Jason Plumb** 36:35 Yeah, so this one I took triage off there, because we talked about it. I don't… I mean, I think this is pretty complete. It's not… doesn't really need a lot of… I'm sure there's questions that might come up, but there's not additional detail needed immediately.
It's very thorough.
You're always very thorough, Servi.
**Surbhi A** 36:51 Thank you.
**Jason Plumb** 36:59 Alright, is Grace on? Yes, Grace is on. How's it going?
**Grace Lim** 37:04 Morning, Dane, good, how are you?
**Jason Plumb** 37:07 Sick, but…
**Grace Lim** 37:09 Oh, no.
**Jason Plumb** 37:10 Hanging in there.
**Grace Lim** 37:10 It is that season, I think, with, like, the weather getting colder and everything.
**Jason Plumb** 37:16 Yeah, and it's so weird, like, after COVID, and just having so many years of never being sick, like, I didn't get COVID, and I was masking everywhere, and everyone else was, it was great. And now I'm getting sick, it's weird.
**Grace Lim** 37:27 Okay.
**Jason Plumb** 37:29 So, yeah… That's not better.
This PR here…
Yep. Yeah, so.
**Grace Lim** 37:36 basically, I know Android SDK already captures a lot of this information, but, like, I didn't see it in the SEMCOM, so that's one thing I wanted to add. And then there were a couple additional…
span definitions I also wanted to discuss. So, I think, like, AppStar, it's…
pretty straightforward, but… so I wanted to move on specifically regarding the spans for screens. So,
the first one, time… basically, like, the first appear span, I was thinking it'd be, like, the time to first draw, time to first appear, pretty…
Universal for mobile platforms, but,
Kind of originally, we were thinking, like, the time to first appear could be…
used as, like, a screen load definition. But then…
Technically, in terms of our user experience, just because the screen, like,
component, like, there's something been drawn, that doesn't necessarily mean, or, like, the app developer might not consider it to be, like, actually loaded, and so I wanted to…
kind of propose, what the screen load definition could be for mobile applications, and so that's, like, the main thing I wanted to talk about, and then also the
Like, the screen visible time, those two.
**Jason Plumb** 39:03 Cool, yeah, I haven't taken a look at this yet. Hopefully other people are able to.
**Cesar Munoz** 39:11 I haven't yet, but I do remember we've talked
A couple of times about this, and it's…
My… what I remember is that it's usually a bit challenging to automatically tell when a screen is fully loaded, because it might rely on some HTTP calls or stuff like that, and…
**Grace Lim** 39:33 It's difficult to, you know.
**Cesar Munoz** 39:35 No, ultimately.
**Grace Lim** 39:36 Nope.
**Cesar Munoz** 39:37 So…
**Grace Lim** 39:37 Right.
Sorry, sorry, please, finish.
**Cesar Munoz** 39:42 No, no, that's… it's kind of pretty much it, so…
I remember the last time I talked about this.
I think the consensus was, well, we can tell when the screen was rendered, which I guess is what you…
Refer to as, visible.
The first appear.
**Grace Lim** 40:00 Yeah.
**Cesar Munoz** 40:01 Yeah.
**Grace Lim** 40:02 So…
So I was… I was thinking, like, along the same lines, right, that's kind of the…
what's the word I'm looking for? Like, arbitrary, like, what is the end of the screen, though? Like, is it when all the network requests are finished, when components are, like, fully downloading? So that's definitely…
ambiguous, and I don't think, like you mentioned, there's an automatic way to capture this in the SDK without, like, some user, like, configuration. And, like, at that point, it's just kind of asking them… asking users or, like, app developers to…
have to manually instrument the span. So I wanted, like, to start, at least, with some definition, and so kind of what I was thinking was, like, at least for mobile devices, if
the time until, like, the main thread is idle again? Could that be, like, the end of a screen load? I… like, I… so I'm not a mobile developer, let me… let me go off of that, to begin with. This was made on the assumption that
Determining, you know, the time to when the main thread is idle is…
is not, like, a significant amount of work, and it's not… there's no, like, technical limitations to get this. So if this assumption is wrong, then, you know, obviously back to the drawing board. But assuming this, I was thinking maybe we could consider that as the…
end of a screen, though, so it's not fully, fully loaded, because, like you said, it's… I don't think that's something we can capture automatically without some user configuration.
**Cesar Munoz** 41:35 Got it. No, I think I understand what you're saying. It's like, regardless of how could this be implemented, at least it would be good to have a definition, so that.
**Grace Lim** 41:45 Exactly.
**Cesar Munoz** 41:46 if it's possible, even via some manual APIs, at least we know what to, you know, what names to use, and yeah, it makes sense.
I will say that we'll…
I don't know, I haven't gone through this, but the only thing that I… probably you already did, that I would do, is to have
Two different names, one for when
When it's rendered, which is probably kind of related to what you were mentioning about the main thread.
And one for it when it's actually, you know, the users can actually do what they need on that screen.
At least we have a distinction between those. I'm not sure about namings, but I will do that.
Broly, you're ready. I have to take a look at it.
**Grace Lim** 42:35 For sure, yeah, this was done kind of late yesterday, but, yeah, that's the basic idea. Like, one that's very deterministic, where you can determine, like, when was the first,
part of the, the UI drawn, like, or, like, in terms of, like, iOS, there's the, like, view did appear, like, life cycle, so that's something that we could use,
At least for the rendering part. And then for the actual load, because my understanding is when the main thread is idle again, that's when it can start taking, like, user interactions. And so, kind of the definition is, like, end of, like.
Or, like, until the main thread is idle again, but, like.
Semantically, like, to me, that kind of sounded like when the screen is able to interact with the user, and so that could be, like, considered when the screen is done loading.
**Cesar Munoz** 43:30 I'm not sure if we can…
Use the word in idle, because the main thread, my understanding, is that it's always, you know, rendering.
So, so…
in a more technical, deeper meaning, at least in Android, we could go to the lifecycle of the screen when it's viewed.
But again, I guess we shouldn't use… Platform-specific terms, so…
**Grace Lim** 43:59 I'm.
**Cesar Munoz** 43:59 I would agree to go with something like rendered, and then at least we… at least that tells me that word, that
whatever UI work needed to open that screen, it's done, even though it might be still waiting for something else. So, yeah.
**Grace Lim** 44:19 I see.
**Jason Plumb** 44:20 So, also, I just… I can leave some feedback on this as well, but stylistically, I think using camel case is not typically what OpenTelemetry favors for span names. It's usually lowercase with dots, just in general.
there might even be exceptions to that, but just stylistically, I think you'll probably see some… some feedback about that. And then, I think there was some…
Yeah, this web vital, I think, would have been nice to link to that, but I think…
I couldn't find… yeah, this right here.
So that's an external link, though. Is that what they're referring to?
**Grace Lim** 44:58 Oh, I was able to find the event YAML in the repo.
**Jason Plumb** 45:03 There's this one, is this the one you were describing?
**Grace Lim** 45:05 Dink.
**Jason Plumb** 45:05 Yeah.
**Grace Lim** 45:06 Oh, okay, no, I think I was just assuming they were talking about the browser events.
YAML file…
**Jason Plumb** 45:18 Well, it'd be cool to know which… exactly which one they're… they're talking about, but there's… yeah, there's already some feedback here, like, yeah, it's.
**Grace Lim** 45:24 Yeah, yeah, yeah.
**Jason Plumb** 45:24 and then whether or not we want the visibility to be long-running, there's already some good feedback, so this is a good start, it's great, yeah. And we would love these things to be dialed in. Like, right now.
Don't we… in Android, we have something around this, don't we?
**Grace Lim** 45:40 Yeah, it's called Time to First Draw, and it's only for activities.
**Jason Plumb** 45:45 Okay.
**Grace Lim** 45:47 Yeah.
I can… I… so I think this is the one I can link it, in the comments.
**Cesar Munoz** 45:57 C.
**Jason Plumb** 45:59 We do have some… we still have some capital K stuff in here, you know.
**Grace Lim** 46:03 Yeah, yeah, so it kind of came from what was already there, especially, like, the activity lifecycle restrictions are also all Pascal keys, so I was like, okay, let me just keep it to minimize, kind of, the changes we'll make to the Android SDK, but then…
Yeah, I kind of didn't look at the spam names for the other existing ones, so I can definitely go and update that.
**Jason Plumb** 46:25 No, I mean, for anyone who's familiar with OpenTelemetry looking through this, like, this stands out like a sore thumb, so having actual semantic conventions, I think, will be very nice to be able to replace these. Like, these have history, these are just bespoke names that came from Splunk, you know, years ago, so…
It would be awesome to have those dialed in.
**Grace Lim** 46:45 Gotcha.
**Jason Plumb** 46:46 That might be the only place where we create telemetry there. Oh, startup. We were talking about startup.
This probably doesn't generate telemetry.
**Grace Lim** 46:55 Yeah, App Store.
**Jason Plumb** 46:55 It is also possible case.
There it is, yeah.
Yeah, having these dialed in would be awesome, yeah. So thanks for taking that on, it's great.
**Grace Lim** 47:04 Gotcha. Okay, yeah, so… I just want to note…
**Cesar Munoz** 47:08 Probably a bit pedantic here myself, but just wanted to know that the… the spans That we have there.
For activities, and we also have some for fragments.
I think are helpful in the sense that for Android developers, they know exactly what
Stage in the lifecycle their… Screen is, if you will.
But from a more generic standpoint, we…
or at least this… it's been a while. Sorry, I don't remember quite correctly, but I do remember that there was some concern that if we add some very generic names.
Then that probably could hide some sort of information that was needed, specifically on a platform
Or, you know, be a bit confusing, because then people will…
you know, kind of wonder, okay, what does render mean in my activity? Does that mean it's created, or it's resumed? Things like that, so…
I think it's… probably we need both, like, we need, you know, framework-specific
Names, and then also generic ones for… for…
different purposes, and I'm guessing the one that you're focusing on right now are the generic ones, if I'm… if I'm correct.
**Grace Lim** 48:29 Yes, exactly. So I did start a thread for this in the, in the Slack channel, I forget which one, one of them. And so I had, like, brought up the question, like, do you want to make
these definitions, like, as specific as possible, or do we, and by as specific as possible, I mean, like, you know, for Android, this is the span, and for iOS, this is the span. Even though, like, at a higher level, they may be referring to, like, very similar, view lifecycle… view…
like, life cycle phase, and so…
it was just… it wasn't, like, many people, but kind of the discussion was towards, like, we should definitely have, like, one platform-agnostic, span, and then, like you mentioned, I also think, like,
as these develop, we can't go into, like, more specific ones for the platform. So, like, from my end, like, kind of what I was looking for was kind of one way, regardless of a platform,
the platform type to determine, like, what is the screen load of this mobile application. And so I just wanted to get
you know, that generic, one going. And so, you know, depending on whether that works or not, like, definitely it doesn't fit the case of, like, recording all the view lifecycle phases. Like you mentioned, like, activity has, like, a lot, and then also, like, even for iOS, it has, like, multiple
Phases that aren't going to be captured by this span, but it does capture that generic, like, when did
the screen load, or when did the first, draw appear, or was,
was it rendered? So, kind of that was the goal, and then the more specific ones, that are specific to platforms, I think that will be, like, a separate, kind of effort to get those defined.
**Cesar Munoz** 50:19 Makes sense. Thanks for clarifying. I haven't been able to take a look at your.
**Grace Lim** 50:23 Yeah, yeah, for sure.
**Cesar Munoz** 50:24 I'll take a look and add some comments.
**Grace Lim** 50:27 Please, yeah. I do believe we need… it would be nice to have this generic.
**Cesar Munoz** 50:31 Turks.
**Grace Lim** 50:33 For sure. Yeah, so, like.
screen, though, that's the proposal for the, like, generic one. And then also, like, I wanted one kind of just, like, the visibility,
span, and so I forget who was doing this. It was, like, either
Datadog were, one of the oldies book goodies. So, like, this one came from, like, just getting some…
insight into, like, a user journey for a view. So, like, if I wanted to construct a user journey, I want to know, kind of, how long a user stays on a view, and so that was kind of where the, like, view visibility came from, like, which…
lifecycle that you use for the specific screen may differ, and probably will, or it definitely does, across the platforms. But that was kind of one thing, I was thinking of proposing as well, just so that we can, like, get that visibility. So, like, I didn't consider this
to be potentially, like, a very long running span. I'll have to read up on, kind of how we want to treat those and how we should treat those. But, yeah, the initial proposal was, like, assuming
the span shouldn't span, like, hours and hours, or, like, the time on the screen doesn't span hours and hours. I want… I propose just, like, one span for the visibility, or, like, the time the screen was visible.
**Jason Plumb** 51:58 Just as an example, if someone opens, like, their podcast player, and they just push play, and it's an hour-long podcast, do you have an hour-long span? Like…
Maybe? Yeah.
**Grace Lim** 52:08 Gotcha. No, yeah, that's… Sorry, go ahead.
**Cesar Munoz** 52:12 It sounds like, going back to what we were talking about with survey.
That maybe events could help, too.
Here, maybe? If at least it's, you know, useful to at least know when a screen was rendered, even though it might not.
I don't know.
We don't… we might not get the end of it, but yeah, I'll have a look.
Thank you.
**Grace Lim** 52:38 Sounds good.
Okay, yeah, so I think my last question is then, like, if…
like, where I can find documentation on how to handle long-running spans, because my understanding, I think you guys were also discussing this, is that we're moving away from span events. So, like, it's either a span or an event, and for me, like, my very simple understanding is spans observations, and events don't, so…
it kind of throws me off when we start saying, like, make an event, but add a duration to it, or, like, a duration attribute. So I'm wondering, like, is that kind of the recommendation for long-running spans, to treat them as an event and just add the duration, or something else?
**Jason Plumb** 53:23 I think I… I think I've heard this come up, time and time again. Like, this is… this is not new, and I don't…
I don't… I don't know of a place right now that I can point to that has…
clear guidance on this. Like, yes, the span has duration, and the way I also think about spans is that they are kind of the base unit of a trace, and so if you're not tracing something, the span probably makes less sense.
When I say trace, I mostly mean distributed trace, but it doesn't necessarily have to be distributed trace. You can imagine a world in which a span is broken down into just a start event and an end event, and as long as there's correlation, you could build a span from that.
**Grace Lim** 54:04 Okay.
**Jason Plumb** 54:04 not always the best thing. I mean, clearly, if you're doing tracing, you want spans, you don't want events, but where the… where the line between those two types is sometimes is blurry, and I don't know of good guidance, but…
That's pretty cool. That just happens, like, randomly, I guess? It just wants to tell you stuff? Sorry.
Yeah, if anyone knows of a place or can find one, it would be good to have.
**Mustafa Haddara** 54:33 I mean, isn't…
**Cesar Munoz** 54:34 I'm…
**Mustafa Haddara** 54:34 Isn't our answer to long-running spans usually sessions?
**Jason Plumb** 54:39 On mobile, yeah.
But the session… the session's the entire user… user session, right? And so, yes, which we model as…
Both events for creation and turnover.
But also in a collection.
**Mustafa Haddara** 54:57 of traces.
**Jason Plumb** 54:58 Yeah.
**Cesar Munoz** 55:01 at least in Android, the problem with long spans is that we don't know if we're going to be able, you know, if the OS is going to allow us to end them, and if we don't end them, then the data never reaches the backend, so…
Events help in a way that if it's okay for you to at least know that something started to happen, and that's it, then, you know, it's probably helpful, but…
I do remember once I think it was Trask.
Where we were wondering about…
You know, kind of, like, mimic a spam behavior, spam-like behavior, using blog events.
And I think he didn't like that, or maybe it was not Trask, I'm not sure.
But I think it's like, if there's some overlapping.
To the point where we need to mimic a span-like behavior with logs.
there's probably… We're probably doing it wrong.
If that's… I mean, to use logs in that case.
That's my understanding, but this is a higher level topic, so… Not sure.
**Grace Lim** 56:05 Gotcha. Yeah, because to give context, like, it's much easier to build the, like, stitch together the beginning and end of whatever duration you want to calculate, like, client-side, than do a server-side, because at that point, like, there's so many…
like, scalability issues and, like, how do you know which one is the right, one to stitch it together with? So it's much easier on the client side,
But yeah, I think there's still, like, the question of the long-running spans.
To give context, like, I don't know if it was…
My understanding is that, Billy, who was also on my team, like, he made some proposals for sessions, and what I mean by that is the session end event. And so, like, session end, right?
that to…
it didn't fly being a long-running spin, now that I think about it, so what he did was propose an event
with the, like, session duration, so…
And my understanding is that had been approved in some hotel, repo. I don't know if it was, like, the implementation or the conventions themselves, I'll have to double check. But maybe we'll do something similar to that then, at least.
**Jason Plumb** 57:17 Probably in here.
And there are events.
**Grace Lim** 57:21 just…
**Jason Plumb** 57:22 Start event and a session end event.
The end does not have a duration, but, you know, every event has a timestamp, and so…
If you have the session ID, you should be able to query or do a correlation based on that to calculate the duration.
**Grace Lim** 57:37 No, no, for sure, like, it's…
Stitching together is possible, it's just, like, in terms of, like, doing it at scale, and efficiently,
like, we wanted to optimize our queries, and so having to do a lot of the stitching at runtime, we were wondering, like, how we can move this to server-side or a client side in the SDK. But yeah, I don't know where it is, but I'm pretty sure he had made some contribution to define, or, like, further enhance the session, and so let me look at that, and I'll link it also in the notes then.
**Jason Plumb** 58:12 Okay. We are basically at time, so I'm gonna have to play timekeeper here and call it.
I appreciate everyone showing up, thank you.
We have the, for those who aren't aware, the client SIG meeting, which is the combination of Android mobile and web, is happening every two weeks, it's only half an hour, and it happens right now, so…
I'll see some of you there.
**Grace Lim** 58:38 Thank you.
**Jason Plumb** 58:39 Have a great rest of your day.
**Cesar Munoz** 58:40 Thanks.
**Surbhi A** 58:41 Thank you. Bye-bye.
