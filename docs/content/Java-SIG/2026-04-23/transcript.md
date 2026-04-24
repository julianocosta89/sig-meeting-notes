SIG: Java SIG
Date: 2026-04-23
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/iqSkKvm93sEJtP4MI04pNKTYqgwLmsLV6x0ud_tTsAmm4IOqCMteOkdrsfZmvJGB.yt7hGt1kluxegr4J
============================================================

## Zoom Recording Transcript

Jack Berg 00:00:47 Hey, John.
John Watson 00:00:51 Which one were you talking to?
Jack Berg 00:00:53 I was just about to correct myself. Hey, Johns.
John Watson 00:00:58 How's it going, Jack?
Jack Berg 00:01:01 Good, how are you?
John Watson 00:01:02 Oh, I'm hanging in there.
Two more weeks till I get to go to Europe for a couple weeks, so that'll be good.
Jack Berg 00:01:10 Where you headed?
John Watson 00:01:11 Going to visit my daughter in Athens, and then we're all going to Florence for… and actually, we're going to Sifnos Greek island for a couple days, and then we're going to Florence.
Jack Berg 00:01:24 That sounds great.
John Watson 00:01:26 Yeah, very excited.
Plum is back!
You were in Iceland, right?
Jason Plumb 00:01:43 Yeah.
John Watson 00:01:44 How was it?
Jason Plumb 00:01:46 Expensive?
John Watson 00:01:48 True.
Jason Plumb 00:01:49 It was great, it was, it was, it was lovely, like…
Jack Shirazi 00:01:51 No, no, I'm just getting a glass.
Jason Plumb 00:01:55 What's that?
Trask Stalnaker 00:01:57 Talking to somebody else, I think.
Jason Plumb 00:01:58 Oh, okay.
Jack Shirazi 00:01:59 Close both doors, this one and that one, till 6.
Jason Plumb 00:02:03 Yeah, I think you called it Drask. Yeah, Iceland was great, it was very beautiful.
I think it was a good time of year to go to, because even though there's Americans everywhere, it wasn't, like, peak summer, like, crowded time, so…
John Watson 00:02:15 Did you get some tomatoes?
Jason Plumb 00:02:17 didn't know.
John Watson 00:02:18 Did you get some, fermented shark?
Jason Plumb 00:02:21 No, sadly also didn't do the shark.
Jack Berg 00:02:26 What's the deal with the tomatoes?
John Watson 00:02:29 So, Iceland has basically infinite power, because they have geothermal power everywhere, and they… so they have huge, enormous greenhouses that grow tomatoes year-round.
And they're amazing. When I was there on our company off-site, we basically had tomatoes, fresh, delicious tomatoes with every meal in February.
Jason Plumb 00:02:49 Awesome.
Yeah, someone told… someone told me they grow bananas there, too.
John Watson 00:02:53 Oh, I believe it.
Jason Plumb 00:02:54 Yeah.
John Watson 00:02:56 Yeah, they basically just can have grow lights running year-round, because they have as much power as they could ever want. And they import bees from Denmark.
to… To fly around in the, in the greenhouses.
Jack Berg 00:03:09 That's cool.
Trask Stalnaker 00:03:10 importing… importing and exporting bees. That sounds like a good business.
Jack Berg 00:03:17 We have strict export controls on our bees.
We don't want Iceland to get a strategic advantage in pollination.
Trask Stalnaker 00:03:31 Alright, let's… whoa, okay.
That's… We've got agenda this week, alright. Jay, you wanna share and kick it off?
Jay DeLuca 00:03:42 Yes, please.
Alright, so I just wanted to give a quick update, for those who may not be aware, for the past year or so, I've been working on a project that we're calling the Ecosystem Explorer within OpenTelemetry, so that's… what we've been doing with the metadata that we've been curating within the Java instrumentation repo. Just wanted to give a quick update. Things are… it's not done by any means, it's still very much a work in progress, but it is usable. You can come in here and you can look at All the different instrumentation libraries, you can… look at the configuration. We're… I'm in the process of updating this to have the declarative configuration options as well, but it does have the system properties. You can see the telemetry enabled, both by default and with different configurations. You can also take a look at differences between versions. So, for example.
In the latest release, a new… attribute was added to, client spans and metrics when the database opt-in is set, so that's all there. But yeah, and you can, you know, look at different versions, see things that have changed.
So yeah, I just wanted to raise visibility about that. Like I said, it's not done, but next week we are gonna publish a blog post on the OpenTelemetry.io website, just kind of publicizing the project itself, and trying to get some additional contributors and start thinking about expanding it to other ecosystems. And yeah, so there's still a lot more work to do. The, the POC had some other options, like a standalone library READMEs rendered and stuff like that, so working on that and trying to get that out in the next week or so.
And we also have a, declarative configuration interactive builder UI in progress. I think I demoed that a couple weeks ago. But we've been rebuilding that, and trying to polish it up, so… So yeah, just wanted to let people know that it's there. If you find anything.
odd, if you use it, let me know. If you have any feature requests, also let me know, and if you're interested in playing with front-end code, come to the, the repo and grab an issue. But yeah, just wanted to raise awareness there.
John Watson 00:06:06 Yeah, my main feature request is, Go and JavaScript in here as well.
Jay DeLuca 00:06:12 Noted.
Jason Plumb 00:06:16 Yeah, is the schema for the metadata stuff, like, standardized somewhere that other… Teams can use.
Jay DeLuca 00:06:23 That's, so another thing is I'm also, submitting a LFX, project proposal, slash mentorship around the information architecture, and understanding how people want to use it, and understanding how other ecosystems are configured so that we can start to to standardize on that, but no, we don't have, strict schemas that are, like, cross-language. Like, the collector had its own. We've introduced this for the Java agent components. I'm gonna work on it for Java agent extensions as well.
And then, yeah, we have to figure out JavaScript, Python, Go, all those… all those other ones. That's what the blog post is kind of… Trying to pull in people from those other projects to start, kind of weighing in.
Jason Plumb 00:07:08 Cool.
Trask Stalnaker 00:07:15 Super nice. I really like the, that, I hadn't seen the configory, but, being able to swap the configuration yet. I like that. That's useful for me.
Jay DeLuca 00:07:30 Yeah, and I'm trying to work on a, kind of a macro view of that, too, so you could just say, like, given, two releases, what is the summary of the… Like, the attribute changes and things like that.
Trask Stalnaker 00:07:43 Yeah… Yeah, that's very nice. Cool!
Jason Plumb 00:07:48 The compass on the landing page is leading me to believe that I'm spinning in circles.
Jay DeLuca 00:07:54 Yeah, it's kind of a compass slash clock hybrid.
Jason Plumb 00:08:00 That's awesome.
Trask Stalnaker 00:08:03 Jack.
Jack Berg 00:08:06 Yeah, so, this came up in a PR, a while back. The contributor had, like, added some null checks on this new API that they had proposed.
And, you know, I was like, hey, let's not do this now. We don't have a standard convention around this. Instead, I opened an issue that said, hey, look, we need to make our stance clear on if slash when and why we add additional null checks, besides those that we get from Null away, right? When we're within the, like, our, you know, open telemetry ecosystem, everything is validated with Null ay, to avoid MPEs, but, you know, technically we have things like our APIs.
Where, you know, instrumentation can call them with no arguments, even though they're, you know, the contract is non- null able, there's nothing that enforces that, and so that would result in null pointer exceptions.
And then on the SDK side of things, when you're building up.
SDK components, like the providers or the exporters, you know, we have, you know, different behaviors there and different goals there, around the null checks around arguments. And so.
I want to get consistent with that, and what I recommend that we do, after thinking about this for a little bit, is adopting a stance where, at the configuration API boundaries, so the public API of anything that's configuration related, so, like, the builder for Tracer provider, or the builder for an exporter, we do, require not null .
checks that throw an exception right there, so they fail fast. And we do that in a bunch of places, but I want to, like, standardize on that and do that everywhere, instead of just in some places.
So, that's one kind of class of checks.
The other class is, for our API boundaries, and I call this, like, runtime boundaries. So this is things that people… people or instrumentation call at runtime, and, you know, we have different goals, because it's not at, like, initialization time. And so at runtime, we want to, we want to just continue to operate gracefully, and not throw exceptions, that can, you know, propagate up the stack and mess with the application's behavior. And so, for runtime boundaries, I propose that we do null checks.
And so we explicitly check if any non-primitive parameters are null , and we exit early or return a no-op or equivalent, whatever the equivalent of that is within the context of whatever that method is.
And, so, like, an example would be for, like, the span API. If you add an attribute to that, and your attribute is null , we should… we should log and return a null op. That's what I… I think we ought to do. And.
Trask Stalnaker 00:11:19 If the value is null or the key is null .
Jack Berg 00:11:22 Either. Well, I guess, no, the value, I think, we adjusted to be null able, so I wanted to ignore that, but if the.
Trask Stalnaker 00:11:28 We use that a lot in instrumentation.
Jack Berg 00:11:32 Right, so any non- null parameter, we would do this check on, right? Because we're just trying to make sure that people are using the API as we describe in our contract.
And a part of this is I… there's this class that we have floating around, and it's used in some places, but not all places. It's called API Usage Logger, and I want to make that part of our public API and use that in a lot more places, and essentially standardize the pattern for, you know, if you are one of these APIs, and you're trying to do a null check, I want to standardize how we log if a parameter is null that shouldn't be.
I want to say things like, well, I want it to be at, like, fine level, or debug level, not at, like, info level, because I don't want this to be noisy. So I want you to have to, like, turn on these logs.
And I want them to all go through one logger, though, so that you can turn on all these logs and get, like, you know, diagnostics about where you're misusing our APIs all at once if you want to, and you don't have to turn on a bunch of loggers to do so.
And I want to provide some breadcrumbs to allow you to find the problematic instrumentation.
Right? So I want to, like, include the method that was… the method… the class in the method, and the parameter that were null when they weren't supposed to be.
And then I want to include a throwable on there, so you can find the stack trace of where this occurred. And API usage logger just has, like, a little utility method that does all this.
So, yeah, that's the basic idea. There's one other sort of, like, edge case, which is, like, implementations of SDK extension plugins, like, implementations of span exporter. What should they do if you call the export method with, like, a null collection of spans?
like, what should we do in our OTLP exporters? That's, like, sort of in between. It's not configuration boundaries, and it's not, like, runtime boundaries, but those SDK plugin implementations are only invoked by the SDK normally, which already has non- null guarantees in it.
And so, you know, if they're given null arguments, they're either being used outside the SDK, or there's a programming error in the SDK itself. So, my recommendation for those is to throw, like, a null pointer exception, basically fail fast on those.
Because it shouldn't be possible.
so… Yeah, that's the guidance that I think we ought to do, and you know, in this PR, I kind of sketch that out. I, like, add new guidance to our knowledge base, and I have a PR, a draft PR, that demonstrates what it actually looks like to apply this guidance across the whole The whole repo, and yeah, you can kind of reference that to see if you love this or hate this, or something in between.
And there's…
Gregor Zeitlinger 00:14:36 It's possible.
Jack Berg 00:14:37 sorts of examples.
Gregor Zeitlinger 00:14:39 This… this looks like not a standard Java design pattern, to be defensive against Niles.
Is… is that the current state of the art? It seems a little odd, honestly.
Jack Berg 00:14:56 Well, so we do this in some places, but not all places. And so, I don't really care what we do, I just want to be consistent.
Gregor Zeitlinger 00:15:03 Right.
Trask Stalnaker 00:15:06 So the reasoning here, Gregor, is that, we've kind of said telemetry and instrumentation is a little bit more special.
In that we don't… whatever happened, like, people apply that, and they don't want their instrumentation to cause failures.
So that's why, historically at least, that's why we have been graceful on… people passing null s to the API specifically.
Gregor Zeitlinger 00:15:40 Okay, I understood it in a different way, that the Java agent should not crash your application, but if you, as the user, misuse the API, then I think there's a trade-off between, Getting to know that early, Versus having to turn on this logger.
Yeah, and .
John Watson 00:15:59 I think the problem is who's the user, because you might pull in somebody else's library instrumentation, and you didn't write that. And if it crashes your app, you're going to be very… I mean, that's not going to be good.
Gregor Zeitlinger 00:16:11 Anyway, that's always the case that… The call… caller can, be… several places away, but I mean, you could also say that the library author should have, early feedback that they are, not using the API correctly, and, Therefore, the… Null pointer exception would be better.
And this is the conventional wisdom, as far as I know, not what my opinion is.
Trask Stalnaker 00:16:45 Yeah, I don't think there's any disagreement, Gregor, that that is the standard practice.
It was just in this project way, way a long time ago.
That decision was made to, say, telemetry APIs are unique compared to other libraries.
In that they get layered in.
as John was mentioning, like, Sort of after the fact a lot.
Whether it's via the Java agent or via a library instrumentation.
And so, that's why it has, at least historically in this project, been treated differently.
Gregor Zeitlinger 00:17:29 Yeah, okay.
John Watson 00:17:30 I mean, it's not just this project. This is… I think most people who have been working on instrumentation have taken this approach. Like, we certainly at New Relic, we had this approach, where it was, like, the… the instrumentation can in no cases ever crash the app.
Even if it's being misused.
Jack Berg 00:17:51 A slight subtle difference, though, is that with, like, with New Relic, you know, there's always an agent involved, and I think we already make that guarantee that, like, if you have an agent, we're not gonna crash.
So, you know, I think the distinction here is that you can use these APIs for, you know, manual instrumentation, which makes it a little bit different.
John Watson 00:18:11 Well, it was not… it wasn't… with New Relic, it wasn't 100% the agent, because there was also, like, the Insights APIs and things like that, that also should never crash your app, which were not… those were just direct APIs that you used.
They were provided by the agent jar, but they were just APIs, not, not like bytecode instrumented.
Anyway, the first do no harm, I think, is a pretty common pattern in instrumentation world.
Jack Berg 00:18:53 So, part of the guidance that I recommended in terms of, like, this API usage logger, so, you know, it logs at find or debug.
Depending on what log system you're using, and you essentially have to, like, opt into it, right? Because we haven't chosen to do it at info or warn, which means you're not going to see it by default, and so I wanted to pair that with guidance that, like.
You always enable this logger at finder debug in, like, your dev environments, at testing time, in places like that, so you can discover this.
So, some sort of policy like that to encourage users to try to actively discover these outside of their production environments.
No.
Trask Stalnaker 00:19:35 hook it into the, the SDK stats?
Jack Berg 00:19:40 Not easily.
Trask Stalnaker 00:19:42 health metrics.
Because that would be a way to get it in front of people in production.
Gregor Zeitlinger 00:19:52 Or you could make a throttled logger, so you don't have to turn it on.
Jack Berg 00:19:59 Yeah, you could do throttled Logger. I considered that and initially decided not to because of the complexity with throttled Logger. There's… this is, like, a really core utility, and it's getting promoted all the way up the module hierarchy to the most central place possible, because everything has to be able to use this. And so, throttling Logger has a couple of issues, and one of them is that there's been… there's been disagreement about, like, what the appropriate frequency of throttled logs should be, and so, like, you know.
Should that be configurable? If yes, how do you configure it? Questions like that have come up.
Trask Stalnaker 00:20:41 I wouldn't be opposed to just a log once, approach.
It's like, at least you get something.
Gregor Zeitlinger 00:20:50 Yep.
Decreation.
Jack Berg 00:20:51 That requires some, additional state tracking, it's possible.
You know.
Trask Stalnaker 00:20:57 atomic Boolean, though. I mean, that… Pretty… simple.
Jack Berg 00:21:01 It's about 500 atomic booleans.
Because this.
John Watson 00:21:05 Like, one for calls.
Jack Berg 00:21:06 Used all over the place.
John Watson 00:21:07 Yeah, it's one bullet.
Trask Stalnaker 00:21:08 Oh, no, I mean, just even blanket, like, in API usage logger, have a single atomic Boolean.
Right. Not an atomic… not a log once per call site, but log once being like, hey, something is up with your app.
John Watson 00:21:29 I can imagine having, like, basically… That… And then also have the finest logging happening, or finer log… whatever the… whatever it has, for all of the cases, so you then would know, like, the message… the one message would be like, hey, turn this… turn this logging on, then you can see all the information about what the problems are.
Jack Berg 00:21:48 I like that, like, a top-level warn log, that happens exactly once, or at most once, and, you know, informs you on how to see more details.
It's discoverable without being noisy.
John Watson 00:22:02 Yeah, I think that's a good idea.
Jack Berg 00:22:08 I see… I see a lot of nodding all around. That's… that's good.
Trask Stalnaker 00:22:12 Not often do we come up with a good… A good consensus plan.
No, we always come up with a good consensus plan.
John Watson 00:22:21 Well, we always come up with a consensus plan.
Trask Stalnaker 00:22:23 You were too fair, This one is actually good. I like that distinction.
Yeah, otherwise, I love it, Jack. I think it's great, because, yeah, it's so confusing of which You know, in each PR, like, you have to decide what to do, and ends up, like.
Spending more… way more time than it's worth it than if we have just a… a kind of strict Guideline.
John Watson 00:22:59 So, Jack, could you talk a little bit about the… The reasoning behind making this a part of the public… API, and how you… I mean, I saw the comment, I saw the Java doc saying it was really only intended for OpenTelemetry Or for instrumentation authors or something, I don't remember exactly what it was. Some comment about that.
And not… So, like, what is the… what is the thought process on making it a part of the public API? Just because… It's something that everything in the world needs to call, not that we intend end users to be using it for anything.
Jack Berg 00:23:39 It's one of these examples of shared internal code.
John Watson 00:23:42 Yeah.
Jack Berg 00:23:43 And, I, I, I'm… I accept that we have shared internal code, and that we want to get rid of it, but, like.
like, if I'm serious about, you know, any sort of future where we get rid of shared internal code, that has to mean two things. It has to mean, like, no new instances of it.
and, like, adopting a posture where I'm actively trying to, like, fight against it slowly as time goes on. So, like, you know, this would be… this is, like, an example of, like, hey, we're greatly expanding the usage of this current, like, internal API, so let's just make it public, rather than, you know, creating, you know, hundreds of more usages of shared internal code.
Trask Stalnaker 00:24:28 Is there… could we do something in the middle where, like, it's common.internal, but we add it somehow to our stability guarantee, our JAPI diff, have, like.
Something smart there that ensures compatibility, but also makes it super clear that it's not for end users.
Jack Berg 00:24:51 Yeah, yeah, so that… that's something that I've thought about. There's some conversation on the, like, no shared internal code issue that talks about techniques to kind of go away from that. That's the one that I like the best. I think there's no way to not do that. Like, we have to, start adding more backwards compatibility guarantees using JAPI CMP around our internal code, but somehow qualify this code as, like, hey, don't use it.
And, you know, what does that qualification look like? It could be, standard Javadoc boilerplate at the class level.
It could be, putting it in a certain package convention. You're saying, like, an internal package, but with maybe some boilerplate that, indicates it's a candidate for JAPICMP, but, like, you know, still internal, something like that. Maybe there's, like, a new package convention. I think I suggested, like, having a convention where we have packages called util or something like that.
And, you know, just talk about that in our contributing guide, in our docs, that, you know, we have API-level guarantees for these, but these aren't meant for end users.
Trask Stalnaker 00:26:08 I think it would be good… yeah, I think I feel John's concern here… Also, it feels, think now would be the time to… Explore and pick one of those.
Yeah, I would be happy with Util, or… I'd be happy with pretty much any of those options, except for this one.
Jack Berg 00:26:32 Okay, I'll… I'll do that. I'll make that a blocker on this. So, yeah.
And then this can be, like, the first candidate for whatever that pattern is.
Trask Stalnaker 00:26:46 Cool.
Yeah, otherwise, I feel like somebody's gonna use it, and especially with the throttling, then they're gonna mess with our shared state of, like.
I don't know. Yeah.
Just feels a little weird.
John Watson 00:27:01 So would we… I guess one question I have is, let's say someone is writing a… They're writing their own… I don't know, I'm trying to think of a good example of something that would live in the API. Maybe, like, their own context storage.
Let's just use that as a potential example, so it's not something that we're providing.
It does seem like, in that case, it might be useful to let them… to give this… give this capability To people, so that they can also get the same logging mechanism about misuse.
Of things. Does that… is that… does that seem like a reasonable…
Jack Berg 00:27:48 To make your example concrete, so, like, right now, the places where we do this, where we add these checks, are in any implementations of the APIs, because the APIs are just interfaces, right? And so we can't add any logic to the interfaces, so it's in the implementations. And so, for example, like, in Tracer.
Like, we have to add these checks to both the no-op tracer implementation and the SDK tracer implementation. And I think this is where your example, like, really, like, resonates, because if you're implementing an alternative API, Would you want to add these same checks to your alternative implementation of those interfaces?
John Watson 00:28:30 Yeah.
And it seems to me… That… that is a… that would be a really good thing to provide to people.
Especially if there's vendors, like, you know, lots of people in this room, who want to be able to provide alternative implementations of whatever it might be.
So maybe this… I mean, I don't know if common is the right package for it, but this does seem like maybe there's a… there is a good potential use case that should make it a part of the public… API.
I don't know, Trask, what do you think?
Trask Stalnaker 00:29:10 Util package could work nicely in that case, because… I mean, it's… still pretty… it… we could have a con… I mean… It's more… I'm trying to think of how to have a distinction there between end-user API .
John Watson 00:29:34 and API Implementer API.
Trask Stalnaker 00:29:36 Yeah, yeah.
John Watson 00:29:38 I mean, what about, like, implementation util, or something like that, or util, or… I don't know.
I'm not exactly sure.
Trask Stalnaker 00:29:46 dot com.implementation.
John Watson 00:29:49 Yeah, or something like that. I don't know, But it does seem like there is a use case for making this just a purely a part of our public API, but it's not like the… to be used by instrumentation authors, it's to be used by API implementers.
Right.
Jack Berg 00:30:08 Yeah, which… So far, there's been few of.
John Watson 00:30:12 True, true.
Anyway, just thought, I think… so all I was saying is I think there actually is probably a good reason to have it be a part of some public API somewhere that is supported.
I'm not a… I… I… I'm not… clear precisely where I think it should live, but making a public API seems like a good idea.
Jack Berg 00:30:41 So, a question… Maybe just a comment to… steer is, like, so… can we effectively dissuade people with JavaDoc? Can we, like, say, like.
do we trust that if we have an API that's public, that we can say and defend, like, that, hey, you're not using this correctly, because look, our Java doc says you're not supposed to use it, except for if you're in this case, and you're using it anyways.
And if we can trust Javadoc, then, like, keeping it in the base package, I.O. OpenTelemetry Common, and just using Javadoc to say, like, hey, this is here, but only use it if you're, like, an implementer of the API, or maybe only use it if you're, if you're… if you're the SDK itself, like, something like that, that really restricts who we recommend using it, then that keeps the door open for, like, expanding our recommended usage later, but it, like, you know, it locks it down for now.
John Watson 00:31:46 That's only really a CYA, right? Because I will… I mean, I definitely know as soon as you make a public API, someone's gonna use it, they're gonna use it in a weird way, and they're gonna cause themselves pain.
Jack Berg 00:31:57 Isn't that true with internal, though?
John Watson 00:31:58 Sorry, what?
Jack Berg 00:31:59 Isn't that true with internal anyways, though?
John Watson 00:32:01 Yeah, yeah, of course.
Jack Berg 00:32:03 Yep.
John Watson 00:32:03 Agreed.
But internal doesn't… internal, we aren't enforcing backward compatibility.
And now we would start enforcing background availability, so… Yeah.
I mean, again, I guess if someone wants to use it.
Are they going to be harming anyone except themselves?
Gregor Zeitlinger 00:32:25 I want to… I would…
Trask Stalnaker 00:32:27 promo.
Gregor Zeitlinger 00:32:28 I would still like to have, something that makes it easier to recognize that this is a different flavor of internal, something that is… API… tracked, because just reading the Java doc is… is easy to miss.
I think, at least.
Jack Berg 00:32:54 I'm leaning towards UTIL, to be honest, and the only… the only thing I would kind of look at is, like, do we employ UTIL differently today, such that, like.
You know, trying to pick up util as the pattern would… wouldn't really work, because… We have prior art, which is in tension with it, but that's… that's kind of what I'm leaning towards.
John Watson 00:33:16 Yeah, I think the thing we would… we want to avoid… is putting stuff that's, like, truly general purpose into util, because then we would have to support it forever.
And those are the things, I think, that people will have a tendency to… just like, oh, there's an XYZ thingamajig in here, I'll just use that, because it pulled it in, and it isn't really something that we're intending to be general purpose, and we might, like, mess around with the internals and change it around, and… people would get… people would… you know, it would be easier to shoot themselves in the foot. But this… this kind of thing is so… Specific and not general purpose?
that it feels… it feels okay to me. But we would just… I think we just need to be careful not to, like, stick some map implementation or some… You know, some queue implementation or something like that into that public util package, and then be forced into maintaining it forever when we didn't really intend it to be end-user facing.
Jack Berg 00:34:17 Yeah, and that exactly is why, getting rid of shared internal code is going to be such a pain, because, like, every single case is going to be this conversation about, like, should we promote it to UTIL?
Or should we do the opposite, which is make a copy for each module that needs it? And we're gonna go around and around, in similar conversations.
But I don't think there's any way around that, because of the points you make.
The risk of over-promoting to UTIL is annoying.
Trask Stalnaker 00:34:48 Yeah, I… I think, though… I mean, with… and the thing I like about the, you know, having util or whatever this other package name is, is we could be more… While, yes, it means it's there forever, we can be more aggressive with deprecating things and evolving those APIs.
Yeah.
Jack Berg 00:35:13 APIs are API and API compatible, but, like, binary compatible and API compatible, but, like, but that's it.
Like, we might even be able to get away with changing the, the internals, the behaviors, but, you know, that's… that kind of… that's…
Trask Stalnaker 00:35:32 Yeah, based on… Yeah, I mean, I think that that is reasonable, as long as it doesn't affect any of… Our usages of it.
I mean, we can put that into our… kind of versioning…
Jack Berg 00:35:55 Wells… This has been a good discussion. I'm pretty happy with Util, and… I don't really see anybody that's… I haven't heard any comments that's, you know, completely opposed to that, so it's, you know, I'll sketch out a PR for what that looks like.
Peter Findeisen 00:36:14 is good, but it's probably a little bit too general. You might want to put some other stuff in there.
How about something like, common.audit that would pinpoint the purpose of these, of these loggers a little bit more?
Jack Berg 00:36:34 It's just, it's just one class and one module, so, I, you know… I don't wanna… I don't wanna just have, like, a… A one class per module pattern.
or one class per package pattern, if I can avoid it, because I want to pick up a pattern that we can use to Solve other generic problems and get rid of shared internal code.
Peter Findeisen 00:37:02 Okay.
Jack Berg 00:37:02 But util might not be the right word, like, I don't know what.
Trask Stalnaker 00:37:06 I don't know what the right word is, but… I've seen some people use .implementation for internal code. I know that the Azure SDKs use that convention.
Something… I'm a nude.
UTIL's fine with me, we could… Consider other options.
To make it look a little bit less attractive.
John Watson 00:37:41 We could totally obfuscate it by filling the name of it with all sorts of crazy characters and stuff.
Trask Stalnaker 00:37:47 UTF8.
John Watson 00:37:48 Yeah, make sure nobody would ever call it by accident unless they really intended to do it.
Jason, you probably remember the Unicode Snowman function in New Relic.
Jason Plumb 00:38:00 I do, yeah. I… I inherited that codebase, yeah.
John Watson 00:38:08 Well, you can't do that in Java, though. We could do it in Kotlin, but I don't think Java lets you do it.
Jason Plumb 00:38:16 We don't have anybody from New Relic anymore to go see if, see if that thing is still there.
John Watson 00:38:21 Do you need to go to Snowman is still there.
I have a feeling that was all ripped out.
Trask Stalnaker 00:38:31 Alright, let's hit our next topics. Check. Need approvals.
Jack Berg 00:38:40 These are low controversy PRs. The build has been suffering lately. The Growl native tests is just a perpetual pain in my ass. A couple new test flakes from different code, a couple long-standing test flakes.
They're all kind of conspiring together to make the build reliably unreliable.
Trask Stalnaker 00:39:05 Grawl is… yeah.
Laura did some… Laura did some magic to make the latest Grawl.
plug in… work, but… sorry, Laurie, I haven't approved it because, it makes… it makes me sad that we have to jump through all those hoops to make it work.
I wish there was… Something better.
Jack Berg 00:39:31 Lori approved a PR of mine that just wholesale disabled the configuration cache for the native test altogether, and it wasn't enough.
It wasn't a…
Lauri 00:39:46 I think I did the same, that I disabled, the configuration cache.
And it also wasn't enough.
Jack Berg 00:39:53 Yeah, exactly, like, I'm, like, I'm going back to the drawing board, like, what… what in the world do I do?
So if you, if you have any insights into that, Lori, yeah, please, please share.
Lauri 00:40:07 Actually, Trask did something that I think solved most of those.
Trask Stalnaker 00:40:14 Oh, that…
Lauri 00:40:15 just that I locally had with, with Krall.
Trask Stalnaker 00:40:20 Jack, if you, if you run into those, open an issue in the… in the repo, paste in the, you know, what year and what you got, and I'll peek.
at them.
Jack Berg 00:40:35 it seems like everyone is slightly different. They're like this lock contention thing, and, you know, it fails in a myriad different ways. And so, like, you know.
Yeah, and I don't think… I don't think it's actually tracked via Devlocity for some reason, so it's not like we can go see in one place a collection of all the test flakes, but, yeah, I'll do that. I'll start aggregating the list.
Trask Stalnaker 00:41:00 Or just one of them, like, that has that… Cause that actually rings a bell. I think I… I think we were having that locked issue… if it was the same thing. But anyway…
Jack Berg 00:41:11 black and white.
Trask Stalnaker 00:41:12 Oh, yeah, yeah.
Jack Berg 00:41:15 I'm, like, I'm, like, getting close to disabling the native tests altogether, because I just… this just seems like we're jumping through so many hoops, and I'm not even sure if anybody depends on this.
Gregor Zeitlinger 00:41:31 Well, that's not true. It was very much helping, for, getting the Spring Starter to work.
So the question is, is anyone using Growl Native from our end users?
Jack Berg 00:41:46 Yes, and… I don't know, just, like, is that… it's like the dev tooling isn't quite there. It's just, like, somehow the Growl Gradle plugin and Gradle are just conspiring to make it unusable.
Gregor Zeitlinger 00:42:03 Yeah, I also found it very frustrating to work with it, It's both, the tooling that is hard to use, and it's also that, it's… it's creeping everywhere, like.
All of the libraries that you use have to have excellent support for it, otherwise, it just fails, and then you have to… Go through all the classes, and you can add manual rules to avoid it, but In many cases, it just doesn't seem to be worth it.
Jack Berg 00:42:39 It's like OSGI.
OSGI is going to be a different flavor of that same class.
Something.
Trask Stalnaker 00:42:47 But do we have any tests that will…
Jack Berg 00:42:51 Well, I have tests for… in my OSGI branch, I don't know if they're gonna.
Trask Stalnaker 00:42:55 Oh,
Jack Berg 00:42:55 Perpetually flaky.
Unknown unknowns.
Trask Stalnaker 00:43:04 Alright, jason wants a… PR…
Jason Plumb 00:43:12 Yeah, this is for Jack Shirazi. Just in context, like, I don't know, I think you were using the op-amp client in your distro as well, but we had someone point the thing at an invalid URL, and it just, like, completely failed silently, like, it was just… happily not working, and so I wanted to make that a little bit nicer.
Trask Stalnaker 00:43:34 Cool. Sounds like we've got a plan for.
Jason Plumb 00:43:37 But also, if it's gonna take more than a few days and we need to do the contrib release, that's also not the end of the world, so it's… it can wait… if need be.
Trask Stalnaker 00:43:47 Fine, let's… let's… Give it a… Day or two.
Jason Plumb 00:43:52 Does that work for EJ? Okay, good. Yeah.
Trask Stalnaker 00:43:55 Thanks, Jay, for staying on top of that.
Jason Plumb 00:43:57 Yep.
Jay DeLuca 00:43:59 No problem.
Trask Stalnaker 00:44:02 Alright.
Jack, planning to merge… Okay, extension…
Jack Berg 00:44:16 The thing that matters here is I'm ripping out declarative config from the SDK incubator and putting it in its own module.
And the new module is OpenTelemetry SDK Extension Declarative Config, and the package within that module is chosen, very intentionally, so that if we later decide to merge this new module into the auto-configure module, the package will remain the same.
So, like, users would not be exposed to future churn if we decide to merge this into auto-configure.
Trask Stalnaker 00:44:58 And so, it's still…
Jack Berg 00:45:03 Still alpha.
Trask Stalnaker 00:45:04 Alpha.
But this is… The path to marking its stable.
Jack Berg 00:45:10 Correct.
Trask Stalnaker 00:45:12 Anything else to mark it stable after this?
Jack Berg 00:45:17 Just, like, a careful pruning of the actual APIs that we want to be stable. Like, the key user interface is, you know, you want to be able to parse a file to the data model and create components from that data model.
So what's the minimal API surface area to support those? And then, the data model itself, like, right now, we auto-generate that.
from the schema, from the JSON schema, to, to POJOs that are, you know, annotated with these Jackson annotations that allow us to, you know, parse YAML into it.
And, that… stabilizing the API will require stabilizing those generated classes, and so we need to take a hard look at what that generation code is doing, and decide if we like all the idioms.
If that makes sense.
Trask Stalnaker 00:46:18 Cool.
And… hey, we've got time for your… Topic for now.
Right.
Pranav Sharma 00:46:28 Thanks.
Trask Stalnaker 00:46:31 And I think I realized after the meeting, when I saw your Slack message, that, I was thinking when you… I was thinking batching in the span… batch span processor, last week when you mentioned it, which is where I… Anyway, that's a different can of worms.
So yeah, what's up with this?
Pranav Sharma 00:46:57 Yeah, so I had this, PR for implementing the recently added spec around, patching metric reader. So, the batching is based on the points in a collection of… total number of points in the collection of metric data.
So, there was some confusion about whether it should be sequential or concurrent. I think we decided to do it sequential, because that's what the That's what the spec suggested. So, I have this PR, it's implemented. I think Gregor reviewed it, he proposed a change to it, and I just wanted to get everybody's views.
on the sequential… Stuff done here for export.
Jack Berg 00:47:44 So, the one thing that I was interested in is… so, first of all, sequential is the way that we have to do it, because the spec has language that says that the SDK must not call exporters concurrently.
Pranav Sharma 00:47:55 Yep.
Jack Berg 00:47:55 So we can't call them concurrently, so it's sequential. And so the question for me is, like, what happens when a, a series of sequential exports start to bump into the next collection?
Pranav Sharma 00:48:10 Right.
Jack Berg 00:48:11 So, and so, I guess, what decisions did you make on that?
Pranav Sharma 00:48:15 So, yeah, I was looking into that, and I looked at the code. There is this atomic Boolean which sets the, exporter ready for the next, export, right? The periodic metric reader collection, the do… the collect plus export cycle ready for the next export. It is not marked as true until all the current sequential exports are done.
So, my understanding was that, let's say you are sequentially exporting and it's taking more than 30 seconds, right?
So, you know, let's say it takes 40 seconds, so the atomic Boolean will not be marked as true until the 40th second, so the periodic batch export that gets triggered at the 30th second will just not happen. And so the collect plus export cycle will automatically happen at the next one.
Jack Berg 00:49:06 At the 60-second mark, instead of the 30-second mark.
Pranav Sharma 00:49:09 Exactly. So that's… that's what I thought.
Jack Berg 00:49:11 Okay, that's reasonable to me. We were talking about this in Slack, and saying, like, hey, if the sequential batches are starting to bump into the next collection, because they're taking a long time, there's basically server issues, then it's not like the next collection is likely to, you know, succeed.
Trask Stalnaker 00:49:33 Better.
Jack Berg 00:49:34 Exactly, right. So, we were saying in Slack that this is underspecified, like, what the behavior should be for here, but, like, I think that's a reasonable take on what the behavior should be, and you're opting into this right now, because we have to make this parameter experimental to begin with.
Right? So, you know, you'll have to opt in to using this and getting this, you know, behavior, so there's still room to change the behavior if the spec comes back and decides something other than what we've done.
Pranav Sharma 00:50:04 Right, so right now, yeah, you… unless you explicitly set the max, export size, the behavior will fall back to what we have currently.
So, yeah.
Trask Stalnaker 00:50:17 I have a question, because this does tie to my… my issue with the batch span processor. With the, batch… When you're doing multiple batches to the metric exporter, and, right, you're saying, we're doing it sequentially, and, because we can't call it concurrently.
I'm… But a lot of the exporters are asynchronous.
Right, so they do part of it synchronously to build up the protobuf payload.
Then they send the… send the request, and then they immediately return back to the loop.
Jack Berg 00:51:00 Do that?
Pranav Sharma 00:51:01 Hmm?
Trask Stalnaker 00:51:03 I don't think they join on that… yeah, because they return a completable result code, right, that gets resolved asynchronously.
Jack Berg 00:51:12 But doesn't the batch… doesn't the periodic metric reader wait for that to… to resolve? That completable result code?
Trask Stalnaker 00:51:20 Yes, and that's what I disagree with.
Jack Berg 00:51:23 Yeah.
No, I…
Trask Stalnaker 00:51:25 The batch… for the batch span processor, But I think it's the same thing, and I feel like I agree with the… I don't feel like the spec language means that we have to wait on that, right?
Jack Berg 00:51:40 I see what you're saying. Okay, so, okay, so… The exporters, we're not calling them synchronously.
we are calling them sequentially, and, you know, by them returning completable result codes that are not immediately resolved, they're kind of informing the caller that, like, hey, I'm gonna take care of this. You can call me…
Trask Stalnaker 00:52:06 Again, right away.
Jack Berg 00:52:07 Call me again, exactly. So, yeah, that's… that's where the spec is… I guess, not entirely applicable to Java, because, you know, the spec doesn't say that the export method should have a completable result code which can resolve asynchronously. It kind of, like, assumes that, export Is, is synchronous, right?
Pranav Sharma 00:52:31 Y… yes.
Trask Stalnaker 00:52:34 There's a lot of wiggle room there.
Jack Berg 00:52:37 Right, there's wiggle room, that's the point, though, and like, yeah, so, I see your argument now, Trask.
Pranav Sharma 00:52:44 One question here, just so that I understand correctly. So, we are saying when the call to the exporter goes, the exporter returns an incompletable result code, which means that I'll take care of this batch.
you can go ahead further. But we are debating whether should we wait for that completable result to complete, or can we move on to the next batch? That's what we are debating, right?
Jack Berg 00:53:08 Yep.
Pranav Sharma 00:53:08 In this case, I feel, if batching is enabled, we might have to wait, for the completable result code to succeed or fail, because you are splitting up the points.
in the metric data. So, let's say you split up points, and the first 10 points are exported after the next 10 points, because you did not wait for the first 10 points to complete, then won't the points be out of order?
Jack Berg 00:53:41 The points should be, like, completely, you know, independent of each other. They should be self-describing such that the server doesn't have to receive them in order.
Pranav Sharma 00:53:51 Oh, okay. I see, sorry. Hmm.
Jack Berg 00:53:55 So, like, Trask, I don't disagree with that, but there is somebody that opened an issue the other day that, like, was defensively adding limits to the thread pool executors that the OTLP exporters use under the covers. Currently, they're unbounded.
So, like, if you didn't take the behavior that our backspan processor did, and you just call them over and over again, you know, you'll create an unbounded number of threads, and you'll get UOM killed. And so we fixed that for one, one of these thread pool executors, and we gotta fix it in a few more places.
And so, like, while… I'm coming around to what you're saying, because of this wiggle room in the spec. I think we should solve it, you know, separately from this issue. So, like, here, carry on the pattern of what we're doing for logs and spans, and then all at once.
adjust the behavior for spans, metrics, and logs to have this new interpretation.
Trask Stalnaker 00:54:53 Makes sense, yeah, it's a long-standing span.
Issue.
for what it's worth, in our distro, we, we have our copy of the backspan exporter to do exactly this.
Jack Berg 00:55:09 You maintain your own copy, okay.
Trask Stalnaker 00:55:11 Yeah, because, it just… the throughput… I mean, if you're… if you're not using a local collector.
You just can't meet… you just can't get… Great throughput.
Jack Berg 00:55:23 And then, so, you know, just because we have a few more minutes, and Pranav, I think you have your question answered, right? So, if you have additional questions, I'll table this, but I have one more comment to Trask.
Pranav Sharma 00:55:33 Yeah, I think all of them are resolved now. Thank you.
Jack Berg 00:55:37 Cool. So, Trask, if we were to adjust this behavior, say, in, like, batch fan processor, batch log record processor, and, you know, we could simultaneously make all the… like, ensure that the OTLP exporters were always safe against this. They didn't, like, have, like, unbounded thread pool growth, things like that.
You know, in my head, there should minimally be a way to revert to the old behavior.
Like, where… but…
Trask Stalnaker 00:56:04 If you, if you, like, kind of like some… if you're using… If you're sort of benefiting from sort of… some sort of throttling aspect and dropping stuff.
I could see that.
Jack Berg 00:56:16 Yeah, and so, like, I think… you know, let's say there's a property, a config property, that dictates what the behavior is here. Like, whether it waits for the completable result code to, you know, resolve, or doesn't, before it, you know, considers the.
Trask Stalnaker 00:56:34 And you do need some kind of bounding there, probably, for… from a memory perspective.
I mean, like you said, the thread… the thread bounding, or number of… Number of these concurrent.
completable futures that you're waiting on, you might want to have a cap on that.
Jack Berg 00:56:53 Right, because, like, what we did when we put a bound on this, thread pool executor in this recent PR is, like, so if you exceed the cap on the thread pool, it's gonna do a rejected execution exception, and it's going to… It's gonna cause the, the export to fail.
And so, like, you know, basically, we have to rethink the throttling mechanism, because right now.
the throttling mechanism is, like, we're gonna drop spans. If you are producing spans faster than you can sequentially export them. And so, in your new world, like, you know, the throttle will become the size of this thread pool, and we have to decide what, like, the correct semantics are there.
And, you know… Making a connection.
Trask Stalnaker 00:57:46 Indeed.
Jack Berg 00:57:47 That's pending next.
Trask Stalnaker 00:57:48 sports.
Jack Berg 00:57:49 That's a… that's… okay.
Trask Stalnaker 00:57:51 Here's my PR for this.
Jack Berg 00:57:52 Keep it simple, just…
Trask Stalnaker 00:57:54 yeah, from 2022.
Jack Berg 00:57:58 I'm guessing you would align the default max pending exports with the thread pool size of the OTLP exporter, something like that?
Trask Stalnaker 00:58:07 That's a good idea.
I mean, the thread pool max sizing is a little more, like, as long as it's bigger.
Like, it's just… It takes a big thread pool to, like, boom just because of thread pooling.
sitting around, it's more critical how many in-flight requests that you have.
Jack Berg 00:58:30 I definitely have.
I have nightmares about that, because I had a really hard-to-track-down bug that was the result of Unbounded thread pools.
But yeah, they're like a megabyte each or something like that, and they don't contribute to the heap, so it doesn't even look like you're.
Trask Stalnaker 00:58:50 Yeah.
Jack Berg 00:58:50 In the traditional way.
Trask Stalnaker 00:58:52 I hate native memory.
Jason Plumb 00:58:55 I'm gonna ask a, hopefully 60-second, simple question. In the instrumentation repo, we have this, mes.toml?
Trask Stalnaker 00:59:04 Yes, Gregor.
Jason Plumb 00:59:06 Can we pull that up real fast? I just wanted to make sure that the versions that are in there at the top will get updated by Renovate.
Gregor Zeitlinger 00:59:16 Pretty… And I even have a linter that is not enabled here that makes sure that it is, because I have, Stumbled across that issue a couple of times.
Jason Plumb 00:59:28 Okay, yeah, yeah, there it is, okay, good, good, good.
Trask Stalnaker 00:59:30 Yeah, look at that.
Jason Plumb 00:59:32 Do we know if this is, like, weekly, or, like… We have that weekly job that updates a bunch of versions, right?
Trask Stalnaker 00:59:39 Yeah, I've been trying to tune the Renovate PRs down.
So let's see what it's currently set at… Yeah, weekly.
Jason Plumb 00:59:50 Beauty. Okay, thank you.
Gregor Zeitlinger 00:59:52 And for this one in particular, I am actually also working on making that weekly, so that aligns.
Jason Plumb 01:00:02 Cool.
That's all.
Trask Stalnaker 01:00:05 The… this should, use our renovate config.
Right, and…
Gregor Zeitlinger 01:00:13 Yeah, yeah. What I'm trying to say is, if you opt in to use my extension, which you don't have to, then you will get this weekly rhythm.
Trask Stalnaker 01:00:26 Okay.
Cool.
Jason Plumb 01:00:28 Cool.
Trask Stalnaker 01:00:32 Alright, we've got, like, 20 seconds to spare.
Get outta here.
Jason Plumb 01:00:38 Thanks, everyone.
Jack Berg 01:00:39 See ya, thanks.
Gregor Zeitlinger 01:00:40 Yeah.
Trask Stalnaker 01:00:40 Bye.
Pranav Sharma 01:00:43 Thank you.
