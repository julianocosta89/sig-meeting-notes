SIG: Android SIG
Date: 2025-12-16
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:17 Hey, good morning!
**Mustafa Haddara** 00:20 Morning!
**Jason Plumb** 00:29 I am pulling up the meeting notes.
**Mustafa Haddara** 00:55 Happy last day of the year. That's how this works, right?
**Jason Plumb** 00:58 I mean, technically, Technically, yesterday was my last day of the year.
I'm like, I could do Sig… I could do SIG this morning, that'll be fine.
**Mustafa Haddara** 01:09 Well, enjoy the rest of your break.
**Jason Plumb** 01:12 Yeah, does this, start for you?
**Mustafa Haddara** 01:14 I'm working till Thursday.
**Jason Plumb** 01:18 Okay.
**Mustafa Haddara** 01:18 But, yeah, close enough.
**Jason Plumb** 01:25 Let's get this going… Yeah, I'm taking 3 days to do volunteering. It's actually pretty nice.
**Mustafa Haddara** 01:37 That's great.
**Jason Plumb** 01:39 Okay, I do have a couple of topics that I want to add. One is related to the resource PR. Did I merge that already? I don't know. There's another one asking about,
client TLS, and there's another one that I'm just… this is from memory.
Oh, the, yes, the Gradle, convention thinger. Okay.
Let's give it… let's give it, like, one more minute to see if anyone's gonna show up, this holiday season. Also, hello, Serbi, it's been a minute.
**Surbhi A** 02:18 Hello, thanks for adding that agenda item.
**Jason Plumb** 02:21 I figured you were going to do that anyway.
**Surbhi A** 02:25 Yeah, I finally got a chance to work on it, and looking for reviews.
**Jason Plumb** 02:31 Yep.
You are not alone, you are in good company of all of the other people who also want to get reviews. We are a little bit behind, right now, it's kind of a slow season.
**Surbhi A** 02:45 Yo.
**Jason Plumb** 02:46 Speaking of that, the other thing that needs to be mentioned Okay. So it is…
The… which one is it?
**Surbhi A** 03:00 like, my PR?
**Jason Plumb** 03:02 Yeah.
**Surbhi A** 03:03 I created the PR First in OpenTelemetry Java Instrumentation Repo.
**Jason Plumb** 03:08 It's upstream.
**Surbhi A** 03:10 Yeah… Once that is approved, I'll create a similar PR here.
**Jason Plumb** 03:16 Okay.
**Surbhi A** 03:17 I did… get some… Review comments from Laurit.
**Jason Plumb** 03:24 Yep. Lori? I will let go.
**Surbhi A** 03:26 Yeah.
**Jason Plumb** 03:32 Okay, and so yeah, the idea is to be able to have, these, specific timings around, like, connection setup, and TLS connection setup, and, the time it takes to send the request, and the time it takes to get the headers back, and, like, all that little subtle… I haven't looked at this at all yet, but that's what this is, right?
**Surbhi A** 03:50 Yeah. Okay. Yeah. All the network phases, the timings, timestamp for all those callbacks, and the backend will calculate the durations.
And I kept the existing APIs clean and added a new API.
Like, here you can request a call factory in this manual OKHTTP instrumentation, so now a new method has been added, so you can request the call factory with the network event listener added to it.
That's how I gated it for now.
**Jason Plumb** 04:22 Looking forward.
**Surbhi A** 04:23 For everybody's opinion on that, how they think about… what they think about it.
**Jason Plumb** 04:28 Okay.
So you're mostly… you're specifically looking for additional review feedback around the API?
**Surbhi A** 04:40 the ape, overall everything.
**Jason Plumb** 04:45 Okay.
That's cool, we'll try and take a look.
Awesome.
Anything else to say about that one before we move on?
I guess the next step would be, once that gets merged and they do a release, then start to incorporate it into the Android instrumentation.
**Surbhi A** 05:04 Right? Yes. And parallelly, I'll try to define the semantic convention YAML file also around it.
**Jason Plumb** 05:11 Oh yeah, I didn't even think about that. So are there any semantic conventions for some of this, maybe?
**Surbhi A** 05:17 They directed me to first create an example implementation, and then now, in parallel, I'll create a semantic convention PR with the semantic conventions around it.
**Jason Plumb** 05:29 Is it open? Is it open yet?
**Surbhi A** 05:32 It's not open yet.
**Jason Plumb** 05:33 Okay.
Okay.
**Surbhi A** 05:36 Just to give them some confidence that, yeah, this is something, everyone is good with.
**Jason Plumb** 05:43 I don't know about other vendors, but this comes up all the time, like, we get asked for this stuff.
**Surbhi A** 05:48 Yo.
**Jason Plumb** 05:56 So that's my next big question, is, like, would we want to…
have this level of granularity enabled in the instrumentation by default. OKHTTP being one that we think that most users are probably using.
**Surbhi A** 06:09 Do we want that level of fidelity turned on by default?
**Jason Plumb** 06:13 I guess we can answer that question when it comes up, but… Yeah.
**Surbhi A** 06:19 So right now, it is not turned on by default, if you think about it. In manual instrumentation, you are calling the old API, which doesn't add the listener. So if you want… and also, via this, you can only have it for certain requests.
And not have it for other requests. You can have different call factories.
**Jason Plumb** 06:38 Oh, interesting, okay.
**Surbhi A** 06:42 Yeah.
We'll have to figure out a way of how we will do it for our auto instrumentation. We'd need some kind of
Configuration in our repo.
To get this feature.
**Jason Plumb** 07:00 Yeah.
**Surbhi A** 07:03 Yo.
**Jason Plumb** 07:04 Okay.
That's cool.
Seems like it could be configuration for the instrumentation.
Which is fine.
**Surbhi A** 07:12 Yo.
**Jason Plumb** 07:13 Okay.
Alright, Lynn, moving on, unless anybody has anything else they want to say about that topic of getting network phase timestamps on OKHTP?
The thing I had next is,
Jamie's PR about resources. Did I already merge that one? Did I merge that yesterday, late, maybe?
**Jamie Lynch** 07:35 Don't think it's me much.
**Jason Plumb** 07:37 this one.
Yeah.
So I… the reason I didn't merge is because I was just hoping to get a little bit more review on it. I think it's great, and I'm… I'm inclined to merge it. It's just, like, we're in this weirdly slow time, and I don't want something that's, like.
you know, this is… this is expanding the footprint, right? So, I think…
Other people giving a thumbs up would be helpful here. So, I want to merge this, but I also want…
other people's opinions on it. So, this PR, for context, for those of you who don't refresh the repo every 2 minutes,
Was there… there was a comment that was asking in the developer feedback thing about, being able to override parts of the resource. I think this was something that folks were used to doing with the OpenTelemetry Realm Builder, and then there were some recent changes that… I don't want to say broke, but made that more difficult, or changed it.
And,
So the ask was to be able to customize the resource and be able to set, like, a service name, an app name, whatever sort of bespoke resource attributes people want to put on there.
And so Jamie implemented that, and I've reviewed it, and I'm looking for other reviews. So I'm gonna say, please review. Let me link… let me link to it.
**Hanson Ho** 08:52 We'll take a look today.
**Jason Plumb** 09:10 Okay, cool, it doesn't sound like, there's any immediate pushback on that, so… Great. Love it.
Alright, the next thing, and these are just ones that I threw in last minute. As people were joining the call, I was like, what have I been thinking about? It's like, these are just the things that were in my memory, so…
There is an issue about client TLS.
This one.
So it was kind of just, like, phrased as an open question, but really, I labeled it as an enhancement, because it is.
So they're using the initializer, and they are wondering how to configure client TLS, right?
And I scratched around for a while, and I couldn't find a way of doing that through the initializer at all.
And I was like, yeah, you can do it with the Rum Builder, but it's, like, considerably more work.
And so, I think that this is a reasonable feature request. I think it's something that folks will almost certainly want to have.
And, of course, we get the immediate, like, yeah, when will you build that for me and have it in the thing I want? So, I haven't responded to that yet. But I have a, I have a partial implementation started for this.
I…
My schedule's really wonky. I'm supposed to be off today, basically, through the end of the year, but I'm trying to at least give community stuff a little attention.
I'll see if I can get a PR submitted, like, right after this meeting, but, you know, it may… it may just wait until the new year, honestly. And I'll respond to this.
But, where I'm coming from, let me link to this PR as well…
The reason I think this is a reasonable feature is because, I mean, I haven't seen this…
up close, but I would expect,
I would expect,
vendors to provide certs that are allow… or allow their user base to generate certs that are… that can be used for ingest, because an open ingest endpoint
Either has, like, some sort of token or something that you have to, like, validate at ingest.
To ensure that the data that's being sent to you is both… that is authorized to send data to you.
And a client cert could be a very good way of doing that. In fact, probably, like, better than most of the things, which I think most vendors do, and that's just have an insecure token, right? So using a client cert could be really nice, as a way of doing that.
Any other thoughts about this?
**Mustafa Haddara** 11:58 Does it actually…
**Jason Plumb** 12:00 We agree with you.
**Mustafa Haddara** 12:02 The cert's gonna… does it actually matter what… how you do it? Because it's gonna end up on the device… the…
client… the… Customer's user's device, at the end of the day.
And so, like, whether it's an insecure token or some… TLS cert, like, that…
Gets out of your control very quickly, lands in an untrusted client.
**Jason Plumb** 12:25 Oh, totally, yeah, that problem still exists, but to be able to…
to be able to ship a cert, I think, might provide an additional level of security that a token doesn't.
But it's also only 8.15 in the morning, so… I keep having coffee.
Keep me honest about that.
**Hanson Ho** 12:47 Wouldn't you configure certs at the network client level?
**Jason Plumb** 12:54 Yes, but it needs to be tied into the exporters, right?
So it's the data that… it's… the ask is for a client's… The client that is used by the exporters to be able to configure client certs and that.
**Hanson Ho** 13:11 Okay, like the network client used by the exporter.
**Jason Plumb** 13:13 Yeah, yeah.
**Hanson Ho** 13:14 And the… that is opaque.
So basically, you set up the OTLP exporter, and that takes care of the network client setup?
**Jason Plumb** 13:25 Yeah.
**Hanson Ho** 13:26 Okay.
**Jason Plumb** 13:28 Sorry, it's not opaque, there's a method on the… on the builder for those… Senders?
Let's see if we can find it.
**Hanson Ho** 13:38 But the senders are basically handle the networking. It's not like, hey, here's your…
**Jason Plumb** 13:43 Yes.
**Hanson Ho** 13:44 instance, and… and… Off you go. Interest… okay, yeah.
**Jason Plumb** 13:49 I think it's in the sender, it's in one of the… but it's like a sender builder, it's in one of the builders.
**Hanson Ho** 13:55 Oh, what network?
Library does it use?
**Jason Plumb** 14:01 Okay.
**Hanson Ho** 14:05 And it's… and you can't pass it…
an instance. It creates one, so you can't have a shared instance, between your app. It's a brand new instance that's configured with its own settings, and…
**Jason Plumb** 14:18 Yeah.
**Hanson Ho** 14:19 Hmm…
**Jason Plumb** 14:20 Not the right place, let's see…
TLS config helper.
Let's see, usages of the TLS config helper.
So it's gonna be a microbe… One of that last time.
**Mustafa Haddara** 14:41 one.
**Jason Plumb** 14:42 Yeah, this one.
**Mustafa Haddara** 14:43 Probuilder.
**Hanson Ho** 14:56 What pulls it out?
**Jason Plumb** 14:58 Yeah, so… exactly. So when you're building the HTTP exporter, there's methods on there, like, their footprint, their API surface has stuff for setting up.
The trust manager, the key manager…
This is the one I think that matters.
**Hanson Ho** 15:14 So basically, the exporter is… a network client. You configure the network client from it.
Which means this has to be exposed if it's… if it's…
**Jason Plumb** 15:26 That's right.
I wanna say that way back when…
Or maybe it was a different exporter, but there was…
This is, like, 5 years ago. There was a way to, like.
I know what you're getting at, Hanson. There was a way to, like, tell the client to use your own…
network client or something, and I forget how that wasn't. The expectation was that you could configure it there, but…
**Hanson Ho** 15:51 Well, I think this is the problem.
**Jason Plumb** 15:53 Admittedly.
**Hanson Ho** 15:53 This is what we get into when we basically say, hey, here's a handy way to configure this external API that we don't own, and we'll give you a subset of settings.
So, now we're basically surfacing whatever settings that we think are good, you know, in our.
**Jason Plumb** 16:12 Cool.
**Hanson Ho** 16:13 some down API, so… That's the…
**Jason Plumb** 16:16 I see this.
**Hanson Ho** 16:18 being able to configure this, like, they should be able to configure an instance of the exporter and add it to our, you know, to use, but I guess that would… we'd have to restructure a lot of stuff.
I think this was initially a convenient thing to say, hey, let's just… Do this, but…
If we're gonna say, hey, take the whole builder, we might as well say, pass us an entire builder, or, or, an exporter, and we will…
**Jason Plumb** 16:46 So, yeah, so right now in the initializer, and they specifically were asking about the initializer, which is great, that means people are starting to use it.
We hide the creation of this completely, and we just have, like, these kind of three small.
configuration things that allow customization through the DSL.
The endpoints, the headers, and the compression.
And my partial implementation that I have started, just has another method here, which is, like, setTLS, because that is that method that we saw.
On the exporter builder.
So what I'm exposing is, I think… I think it's this one.
**Hanson Ho** 17:28 interface.
Yeah.
**Jason Plumb** 17:30 except this… it's a different… it's a different method, but it's very close to this. Anyway, I'll have to…
Is it… is TLS in this?
**Hanson Ho** 17:41 But basically, we would have to expose… we would have to… to take.
**Jason Plumb** 17:45 Yeah, there's an…
**Hanson Ho** 17:46 Yeah, yeah. As in… Wait, wait.
**Jason Plumb** 17:50 I was gonna put another… I was gonna have another method on here that references something from the span's endpoint.
**Hanson Ho** 17:55 So the span standpoint will have a way to configure TLS.
Oh, okay.
**Jason Plumb** 18:00 Client TLS.
**Hanson Ho** 18:01 Okay.
**Jason Plumb** 18:02 Which is a little bit misplaced, like, that doesn't seem like the perfect place for that. Like, the endpoint to me in my head is, like, the remote thing.
**Hanson Ho** 18:10 Yep.
**Jason Plumb** 18:10 So configuring client stuff into it is a little bit weird, but I think I can kind of squint and reason about it by saying it's the client's connection to that remote thing, so…
I don't know, I don't think it's that important.
**Hanson Ho** 18:24 I mean, this is… this is… we're whacking moles right now, and I think this, this, this, this mallet down will whack this particular mole, but I think there'll be additional, very reasonable requests, that ask us to expose additional configuration options here. So,
Probably… probably saying… here's an API that is…
making it easier to use our more complex API, that's reasonable, because we own both of those APIs. When we say, here's a less complex way to configure a third-party API, or third-party as in that, you know, outside of this
it becomes a… it becomes a, what is important, and we don't get to determine either API, or we don't get to determine what's important and the base API. So,
I think to solve this problem, exposing it is fine, but, I think we should examine…
The types of things that we configure opaquely.
In the, in the initializer.
**Jason Plumb** 19:34 Yeah, I mean, that is reasonable. I see… I see your concern with this. I… so, this is really the method that I'm targeting, which is…
TLS, and if we do a blame, can we do a blame on this? Like, I don't… I doubt you.
But this has changed much.
**Hanson Ho** 19:50 Like, retry policy will also be reasonable, like, you take a look at all this.
Ahead of…
**Jason Plumb** 19:57 Look at this… look at this shady character adding stuff about.
**Hanson Ho** 19:59 Who the hell is that? Glasses? I mean, come on, that's… ugh, I don't know.
**Jason Plumb** 20:04 So this method, has been there for, like, 2-3 years, like, untouched, you know?
**Hanson Ho** 20:09 Yep.
**Jason Plumb** 20:10 So, it feels pretty stable to me. I think that ex… like, how… like, using that…
In our initializer doesn't seem like a huge liability to me.
**Hanson Ho** 20:20 No, but…
You could say, you know, trusted certs… like, there's a whole bunch of things that are very reasonable to expose from this, is…
Yeah. Retry instance, like, I doubt the default retry is any good.
**Jason Plumb** 20:35 Right.
Yeah, and at some point, you're like, well, just… why don't you just give me the builder that you want configured instead of us micromanaging it? Yeah, I get it.
Alright, that's probably all I want to say about that one. Anyway, that exists. I think it's an interesting idea. I think it's useful.
I wanted to give room, though, for people to say, we shouldn't do that, and I'm not hearing that.
**Hanson Ho** 21:02 I'm saying you have… I think I'm saying we have to kind of do this, but we should…
**Jason Plumb** 21:06 Yeah.
**Hanson Ho** 21:07 Probably think about whether the overall strategy of having to do this is a good idea.
Yeah, I mean, at some point, there are going to have to be requests like this one that we just say no.
**Jason Plumb** 21:19 Like, use… use the… use the OpenTelempty Run Builder if you need that level of customization.
You know, but the basic stuff, and I think this is basic enough to.
**Hanson Ho** 21:28 This is basic. This is basic. Like, retry… configuring network stuff is very, very basic. Yeah. I can't believe they're actually not configuring their own retry policy.
Yeah.
**Jason Plumb** 21:42 Alright, there was another issue, another was a PR that came up.
that I know that Jamie has commented on about some Gradle stuff that I put a block on.
Although, maybe they've closed it in the meantime.
Got that one…
**Hanson Ho** 22:09 Let's see… is it Devosity stuff?
**Jason Plumb** 22:11 No.
**Hanson Ho** 22:14 Because that's Gradle seems like.
**Jason Plumb** 22:15 this one.
**Hanson Ho** 22:17 Oh, okay.
**Jason Plumb** 22:19 Yeah, let me link to this.
Right, so the idea was to consolidate our declared alpha dependency on… it's not OTEL Alpha, it's our BOM dependency, it's the highest level platform BOM declaration that we have.
And they wanted to consolidate it in one place, which is, I think, actually a pretty good idea, but it did change from API, so let me show you what that looks like.
**Hanson Ho** 22:53 This is the one that we tried to… I tried to do in the refactoring that you had to put back in, right?
**Jason Plumb** 22:59 Exactly.
Exactly, so…
Yeah, without this…
Even though it can… even though the compiler can resolve the version at compile time, Sonatype wants that to be an explicit declaration that it can propagate into its palm.
And… That fails validation during the release process.
Like, you find out about it super-duper late. So that's why I'm hesitant, especially while 1-0 is still a little in flux, if we were at, like.
1.13 or something, I might not… I'd be like, yeah, let's try it again, like, it's been a while, but right now, I'm like… this has bit me, like, I think two releases in a row, and so I'm hesitant to move forward with it.
What do people know about this approach that I don't know?
I know you're probably just seeing it for the first time.
But basically, every one of these modules has a dependency, let's just pick one, on the BOM, right? It's saying, here's a platform dependency on the BOM, and that constrains all of the OpenTelemetry dependencies
And so that they're… they're versioned in lockstep, and we're getting matched versions of everything, so the… the alpha bomb, depends on the regular bomb, depends on the core bomb.
And so from that, everything is, like, kind of nice and unified version-wise.
declaring that as an API dependency means that anyone who's using this module directly
Can also… it means that we expose these components…
by declaring it as an API dependency, we also allow users of this module to use it. Is that correct? Do I have that right?
**Hanson Ho** 24:55 Yeah, without having to specify the, the bomb itself.
**Jason Plumb** 24:59 Right, right. And so this… Go ahead.
**Jamie Lynch** 25:04 Yeah, I was just gonna say, my comment on Miss PR was basically, I think the approach of putting it into the conventions
Build script was okay.
If we make it API rather than implementation.
But, obviously, I don't have a context on why it's failing on Sonodope, when you remove stuff.
**Hanson Ho** 25:29 Yeah, I think if it has to go into every single one, doing it at the conventions allows us to declare it in one place. I think, you were suggesting that, too. But I thought BOMs would have to be API,
Because you're basically saying, if you consume this project, you are also taking these versions as depend… these versions defined in the BOM as dependencies. So…
So, yeah, like Jamie said, that… that would be… that would be a reasonable approach to do this. It's a good cosmetic…
**Jason Plumb** 26:03 having it in the conventions, but not the way they've currently done it, which is as implementation, but as API.
Right, so they have it here as they make a platform variable, and then if this said API, we think we could get away with it.
**Hanson Ho** 26:17 Yeah, but at the end… but then, effectively, the things that… the artifacts that are generated will have the same dependence. It will have an API dependency to that. So, if their issue is having… having that specified in there anyway, this wouldn't really help them.
**Jason Plumb** 26:34 I don't think that's their issue, I think they're just doing cleanup.
**Hanson Ho** 26:37 Okay.
**Jason Plumb** 26:37 Helpful.
**Hanson Ho** 26:38 then that's great. That's… we should've done… we should do this then.
**Jason Plumb** 26:42 Yeah, okay.
**Surbhi A** 26:43 One thing is… We also faced the same issue in Splunk Hotel Android.
The issue was, like.
some places, the platform dependency was missing, so some modules were failing sonar-type validation because the POM was not getting the BOM added to it.
**Jason Plumb** 27:02 Right.
**Surbhi A** 27:02 And other thing was, we did not need API dependency to the platform. We added implementation dependency to the bombs at the places where we didn't want to expose those modules to the customer.
**Jason Plumb** 27:15 Okay.
**Surbhi A** 27:15 where we wanted to expose the upcoming OpenTelemetry libraries to the customer, there only we added the API dependency to the platform BOM.
Because with BOMs, they are not transitive. The customer will anyway have to add the relevant BOM.
Right? So API dependency probably doesn't make sense.
**Hanson Ho** 27:37 Well, API dependency makes it transitive.
**Surbhi A** 27:41 But, no, bombs are not transitive. Berms need to be added explicitly.
**Jason Plumb** 27:47 So even if… even… you're saying… you're suggesting that even if this was API platform, this kind of conceals that it's platform, but whatever, if this was still API platform, that it's still not transitive, meaning a user of…
pick any of these. This session was what we were looking at before. A user of the sessions module who's using that directly would still need to declare, even if this were API,
they would still need to declare a dependency on the OpenTelemetry components that they need. Is that true?
**Surbhi A** 28:18 That's what… yeah. Okay.
**Hanson Ho** 28:21 If they use it in their own, module, they would have to declare it, because that's… that's their version. Like, you're not gonna
Okay, I guess, okay, you're right, but then…
by transitive, I guess I don't mean… I don't mean… Okay.
**Surbhi A** 28:44 like, our SDK would function properly, but if they use the similar APIs, they would need to declare it themselves.
**Hanson Ho** 28:53 Right.
But it ensures… so if we have implementation, and the user, like…
I guess I don't… I don't know enough about Gradle dependencies and BOMs. Like, if they… if they include a newer version, the BOM, and our module,
has API or implementation, does that make a difference between what versions we, our module uses?
**Jason Plumb** 29:23 It shouldn't.
But I think they can't override it.
**Hanson Ho** 29:26 then I'm… I'm wondering why everything…
that… well, I think I just don't know… listen, I've always used API dependencies when consuming bombs, so I just don't… I don't… I don't know what…
I don't know why, I guess. Maybe I'm just copy-pasting, so… I will… I will not… oh, wait, I'll stop commenting that. I'll take a look myself.
**Surbhi A** 29:47 I also forgot, yeah, I'll also share any knowledge, refresh my knowledge and share.
what I, learned about it, yeah.
**Jason Plumb** 29:57 Yeah, I appreciate that. This stuff is confusing, so I pulled up the fix that we had to get in place to do… to complete the release, and this is what the failure looks like. So this is during the release process.
It's like, failed. So, it goes all the way through building and publishing. The staging… the way that song type works is, like, all of your…
cool, hot new artifacts go into a staging repository, and then the staging repository is closed, and then the release happens? Like, it's like…
make the stage, close the stage, release the stage, and the close the stage is what failed, and it's like, failed because all of these modules are saying it's missing dependency information, and it was always on OpenTelemetry, like, core and instrumentation packages.
**Hanson Ho** 30:45 So by… previously, we basically said, these modules got their bomb from something that exported the bomb.
**Jason Plumb** 30:56 transitively, which is why… so I think that's why it… I think that's why it compiles.
One of these, I don't know which one it is, but one of these has this dependency already.
**Hanson Ho** 31:06 And that basically makes it almost implementation.
**Jason Plumb** 31:10 Okay.
**Hanson Ho** 31:12 So, there's a chance that if you try to build it as it is, with a PR like that, it's gonna fail in a similar way, because before…
**Jason Plumb** 31:22 Yeah, yeah, so I think… I think you're right. I think we can't do this.
Because I think that's basically what we had. So this is the PR that, we put in to fix the release process. Yeah. And so all of these modules, or many of these modules, have… they take a dependency.
on the agent API, and the agent API, BuildGradle, has that declared already, and so that's why it compiles, right? That's why the versions can be resolved.
But then at Sonotype time, they're like, you didn't declare version information. We were assuming that it was, like, or I… maybe I had falsely assumed that it was transitive, like, because we depend on this thing, and this thing depends on the platform. But I think to Serbi's point, it's not transitive. It has to be local, is what it feels like.
**Hanson Ho** 32:09 it's transitive just by one step. It basically reduces the transitivity, the second step. You get in. It's similar to implement… well, I guess, I guess it would… yeah, you wouldn't call it transitivity. So, Serbi, for the projects where you include a BOM with implementation.
Do you upload that to Sonotype, or do you just build it locally?
**Surbhi A** 32:32 there are… they are separate artifacts uploaded to SonarType.
**Hanson Ho** 32:36 Okay, so the ones… the module that has a implementation dependency on the BOM, that artifact is created, on so-and-set properly, and there isn't an API dependency, from that to it, because I think…
**Surbhi A** 32:56 No, like, implementation BOM is there as a dependency, and it is able to publish it to SonaType.
**Hanson Ho** 33:03 Okay.
I mean…
**Surbhi A** 33:09 It is also… like, at runtime it works, right? The transitive dependency thing, but Sonata type probably has a weird rule. It doesn't…
or maybe the POM generation is faulty, it doesn't add it to the POM, transitively looks and adds it to the POM, so it needs to be in the same module to be added to the POM, and SonaType just looks at the POM.
**Hanson Ho** 33:34 Okay.
**Jason Plumb** 33:35 Totally, that's my understanding as well. So if we look at our last release, for example, like, if we go to…
Oh, how do you get there?
**Hanson Ho** 33:45 So Sonotype resolves dependencies differently, is basically TLDR, and implementation should still work.
But… Why are people using… API exclusively. I guess not everybody, then.
**Jason Plumb** 33:59 So, like, we were just, like, picking, like, one of these modules, like, sessions, right? So if you go into Sessions, and you look at…
Why do we not have the RC in there?
That's weird.
There's no release candidate for this stuff, is it?
Sorry, this is surprising to me.
Okay, the API has 10 alpha.
The agent has 1O alpha RC. Common has it…
Core has it, but is the instrumentation screwed up?
Services.
Has it.
Session.
Has it? Okay, so I was looking at the instrumentation sessions.
And it does not. So where's our instrumentation?
Is there another package component?
Yeah, that's what it is, I think.
Okay, phew.
The… the… group is different.
Okay, whatever. So what I wanted to show you, the reason why I was clicking around on this junk at all, was to show you how it gets resolved. I'm gonna not do… I'll do core, right? So if you dive into here and look at the palm…
There's two dependencies sections, I believe. So this is all of its direct ones here, there's…
This… yeah, so it's this thing.
And the rest of these are, like, scope compile, scope runtime. This is scope import, right? And I think it's the gen… I think it's the generation, or I suspect it's the generation of this block during the release, or the close process, this thing.
That's causing it to fail.
Because it's looking in… Whatever the generated artifacts are, and not finding this version.
That's my take on it.
Anyway, so that's why I wanted to put a block on this. I think it's confusing, and I don't want to have to do this release
Problem again right now?
I would love to have it consolidated, I think everyone else would too.
**Hanson Ho** 36:41 I think changing it to API would effectively do the same thing as
what it is doing before. And changing its implementation would be an additional, kind of, interesting flip that… that may or may not benefit.
So… If we don't want… if we want to deal with this in January, I think that's… that's reasonable.
But this is probably a good change.
This is a good change. It's whether or not it's API versus implementation. And right now, I can't find information to say API has to be API, so…
The example, the first example, is using the platform. It says API. But then…
importing a platform, which is, I don't know what the difference between importing and using is, is,
well, I guess if by API you're exporting the versions, too, and importing, you're just using the versions within that module.
So, which is why it was weird that it's not transitive, because I thought the API is…
what's the point if it's not transitive, so… Yeah.
**Jason Plumb** 37:49 Well, okay, so we, last month, released the, first release candidate.
Applause.
Good work, everyone. And, the intention, I think, was to get the RC dropped and have 1.0 released this month.
We're, we typically release after instrumentation. It wasn't clear to me if we wanted to, like, wait.
But regardless, I'm probably out of time for the year, and I can't really run it, so I think I'm just gonna bump it till January, and hopefully that doesn't make anybody extremely sad.
**Hanson Ho** 38:27 Oh, hopefully not a lot of people are looking to upgrade, .
**Jason Plumb** 38:32 What that also means we'll push out… so, the way I expect this then to work is we will…
do a… we will do the 1.0 release off of the release candidate, and we'll call that 1.0, and there will be… unless something comes up between now and then, there will be no changes to what's currently the RC, because we haven't backported or patched anything.
Let's expect that to release the first week-ish of January.
I think the first is toward the end of the week, and I'm taking another day off, so I think my first day back is the 5th.
So I don't want to say week, it's, like, approximately the first week.
**Hanson Ho** 39:11 The first full week. The first full week.
**Jason Plumb** 39:13 Sure. The first full week of January.
So let's expect the one to drop then, and then we will be behind a full version of instrumentation upstream, and we could… we could consider releasing 1-1 then.
Very shortly after that, like, within a week or two.
And then we're kind of back on track. Then we'll release 1, 2, 1, 3, 1.4.
And then we'll just have our cadence.
Paying extra special attention now not to break… break things.
I mean, and that time will also be nice, because Cesar will be back, and he might have some opinions on stuff, so…
Okay, does anybody have concerns about that plan? Is that… is that cool? Are we all going into holiday mode anyway?
Okay.
That 1.1 is gonna have a bunch of changes in it. Like, we've already stacked kind of a lot of changes already.
Okay?
And then my last topic, no one's adding any other agenda items, so I'm gonna bring up my last topic, which is…
I want to know what people think about this idea of not meeting next week.
**Hanson Ho** 40:51 Oh, yeah, I'm… I'm not there, so… feel free to meet, and I won't be there.
**Jason Plumb** 40:55 Yeah, what do people think? Do you want to meet next week?
I can do it if you want to. I don't want to.
**Hanson Ho** 41:05 I don't want to either.
**Mustafa Haddara** 41:06 Is anyone around next week?
**Jason Plumb** 41:08 I mean, I could make myself available, I don't want to.
**Hanson Ho** 41:13 No, I think it's illegal in Portland to work on the 23rd. It's, anti-labor.
**Mustafa Haddara** 41:17 That's right.
**Jason Plumb** 41:18 And then that raises the question about the 30th.
**Hanson Ho** 41:23 I am actually technically working in the morning, so… but, I think we should also not…
I feel like there's… There's always slack if there's something that needs to be talked about, so…
**Mustafa Haddara** 41:40 I agree.
**Jason Plumb** 41:43 So… I'm hearing no meeting?
**Hanson Ho** 41:47 No meeting.
**Jason Plumb** 41:48 Alright, what comes after that?
6th, so we're definitely meeting then, okay.
**Hanson Ho** 41:52 Meeting on the 6th.
It's always… Nope, I'm not gonna say it.
**Jason Plumb** 42:05 2026.
Okay.
Sounds like we will be meeting then.
**Hanson Ho** 42:18 Jamie, is there anything you want to bring up about anything?
**Jamie Lynch** 42:25 I don't think, I don't think.
**Hanson Ho** 42:27 Okay, alright.
**Jason Plumb** 42:29 How's the… how's the Kotlin donation going?
**Jamie Lynch** 42:33 Oh yeah.
**Jason Plumb** 42:37 We didn't plan that, by the way, that was just… Maybe think of it.
**Jamie Lynch** 42:41 Yeah, so that's been accepted by the TC, by the technical committee, so we just got some acceptance requirements to hit, and then hopefully things will start moving on that, and…
It'll be an OpenTelemetry repo, and…
Probably a project, and then sequel startup.
**Jason Plumb** 43:07 Cool. Awesome.
Sounds like it's really close. I know it's a long… it's a long, sloggy process, but it sounds good. Yeah, yeah.
That's awesome.
**Hanson Ho** 43:18 It's more waiting than… than tons of back and forth, back and forth, back and forth, so… at least, at least it's, it's,
Not super… continuously time-consuming, hopefully, Jamie.
**Jason Plumb** 43:29 Yeah, yeah. Have you identified, maintainers?
**Jamie Lynch** 43:36 So, I think we know who's gonna be maintainers from a base
point of view, I think me and Fan are probably gonna be nominated. We're not…
100% sure on who will be nominated from outside of Embrace, but we've had lots of folks kind of chime in.
And if anyone here does have interest, and, like…
maintainer or approver status, we can… Kind of consider that.
**Hanson Ho** 44:06 Or just join, because, I'm not going to be a maintainer, I might be an approver, but, but, I think ideas are good, especially at this stage, where, you know, we're gonna try to say it's not Android only. Well, no, it is not Android only, but we are trying not to be.
2-2A Android, so I think… something like the Metrics API,
we'll probably need to do it. Whether the implementation will be done by someone who actually uses it in the backend, that'll probably likely gonna happen. So if there's folks who are interested, you know, in contributing to various aspects of it, you know, I think, you know, when the sig starts out, we're definitely gonna spam this, and
get as many people interested as possible, which, you know, it's a double-edged sword. We want ideas, but then that creates a lot more,
velocity and also overhead. But that's good. That means it's active, so…
**Jason Plumb** 45:07 Cool, yeah, I think I'm in a similar boat, like, I want to join the SIG, and I want to stay abreast of changes, and I help out in some small way. I certainly don't have cycles to maintain.
Cool.
Well, I think that's it for today, then. We somehow got 45 minutes worth of content, because I talk a lot, probably.
It's nice seeing everyone. Happy holidays!
**Hanson Ho** 45:36 Yeah. Happy holidays, Merry Christmas, Happy Kwanza, happy holiday.
**Jason Plumb** 45:41 Yeah, next year!
**Hanson Ho** 45:42 See you next year.
**Jason Plumb** 45:43 - by…
**Surbhi A** 45:44 Bye. Bye-bye.
