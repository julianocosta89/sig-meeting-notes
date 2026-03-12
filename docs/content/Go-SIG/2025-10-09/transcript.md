SIG: Go SIG
Date: 2025-10-09
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:27 Hey, David.
**David Ashpole (dashpole)** 01:31 Hey, Tyler.
**Tyler Yahn** 01:32 How's it going?
**David Ashpole (dashpole)** 01:33 It's going great.
**Tyler Yahn** 01:35 Nice.
Are you, you're headed to KubeCon, in, like, a month, right?
Oh.
**David Ashpole (dashpole)** 01:43 I need to book all my travel and stuff. I have a talk I'm supposed to give.
**Tyler Yahn** 01:48 Oh, okay. I thought I was behind, so you're making me feel good.
**David Ashpole (dashpole)** 01:51 Okay.
I'll keep making you feel good, then.
**Tyler Yahn** 01:54 Yeah. We.
**David Ashpole (dashpole)** 01:56 Three more weeks.
**Tyler Yahn** 01:59 Yeah, I think it's… I think it's the November… 8th or something like that? Or 8th or 9th, I think, is the Maintainer Summit, yeah, and so…
**David Ashpole (dashpole)** 02:11 I'm having a lot of fun with this, optimization work. It's been, like, the most fun thing I've done for a while.
**Tyler Yahn** 02:18 Yeah, I know, right? That's always, like… it's always kind of a blast to find something that's, like, you know, just grabs your attention like that, yeah, it's always good. Yeah.
**David Ashpole (dashpole)** 02:28 I have, like, I'm implementing a lockless exponential histogram now, which is gonna be super fun.
**Tyler Yahn** 02:35 Yeah, that was the one I was like, this is gonna be… this is gonna be something. The other two, I was like, okay, yeah.
**David Ashpole (dashpole)** 02:41 I've got it figured out, I think.
But… The fun part will be… whether anyone can review it.
**Tyler Yahn** 02:50 Yeah, I mean, I remember the exponential histogram itself was already, like, took a long time to review that one, so, yeah.
**David Ashpole (dashpole)** 02:56 Yes, yeah.
But…
**Tyler Yahn** 03:00 Should be good.
Hey, Brian.
Let's see… See, I don't think most of the European cohort are going to be able to show up today outside of Bryan, I guess.
But, yeah, so I guess we could probably start. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, please go ahead and add them there as well.
Yeah, we can jump in here. So, first up, I just wanted to talk about our milestone, just to check in on progress here. So, maybe just go through what's actually included here. We have… 17's still open?
Yeah, let's see, okay, so, jumping in. So, expose the temporality selector functions, I don't know what's going on here, I… I thought this got split off, and it looked like this was, like, not quite understood, that this kind of stuff is not something we're looking at adding here.
Yeah, I don't know what's going on with this one. I, like, I think it needs to get closed if that's gonna be the case, because I think this is already, like… All the functional elements that we were going to accept are included.
**David Ashpole (dashpole)** 04:41 The OTelConf one would be a different repository where the pull request would be added, so I'm not exactly sure what is left here. I think… I think we should just make sure that those instructions are clear, that, like, we would accept this if this was added in OTELConf.
Potentially.
Is that something we actually agree on, though? Like, that if this is added there, then those, like…
**Tyler Yahn** 05:04 Actually, I'm not even sure we need it there, to be honest.
Cause, like… Because if you're passing in a configure… like, if you're passing in, like, temporality, you're gonna pass it in as, like, a JSON file or a YAML file, right? You're not going to pass it in as a programmatic… enum.
**David Ashpole (dashpole)** 05:26 I guess the question… the question I have is, like.
There's parsing the whole JSON file, or YAML file, right, that OTelConf definitely supports.
My question would be more like.
How much of the smaller bits?
Because people have their own configs, right? And they may want to embed pieces of, like, let's say that they only support tracing, and they just want to support, like, the tracer provider portion of the hotel config file.
Is that… is, like, parse this YAML as a tracer provider.
A thing that we would expose?
Does that make sense?
**Tyler Yahn** 06:06 Yeah, I don't think that's something that we plan to expose. Like, we have a high-level, like, parse the OpenTelemetry standard.
**David Ashpole (dashpole)** 06:13 Across the entire thing.
**Tyler Yahn** 06:14 Yeah, and like… Obviously, like, if certain elements are missing, like, it is… actually, if certain elements are missing, like, it doesn't matter, like, it'll just give you back what you're looking for. I think we actually already have, like… meter provider, like, a specific meter provider function. So maybe, maybe I'm kind of misspeaking here,
**David Ashpole (dashpole)** 06:33 I guess, like, it seems like what he's asking for is… I have a… a teeny tiny piece of YAML, right, which is just a key and a value.
Like, can you parse that into a temporality preference selector, right?
**Tyler Yahn** 06:48 Yeah, but the thing is, is like, why… go do that. Like, go write that code. Like, if you want it to be in this particular format, like, we have the functions where you can do that mapping on your own.
Like, why… why does this need.
**David Ashpole (dashpole)** 07:03 I get it, I get it. It's just, if someone… I've encountered this a little bit, where I've been like, it would be nice if I could have, a Kubernetes… Kubernetes has its own, like, configure OTel file format that I introduced.
A few years ago, because we needed it.
But it would be nice if I could just… throw it out and use the OTEL one, but I can't use the entire OTEL one, because we only do tracing.
Right, so it doesn't… Make as much sense to… Parse the whole thing, but… That doesn't mean we need to do it today. But I see why people are like, I need part of your… I need part of OTelconf.
And this is him asking for this particular part. I don't know why he only wants the temporality preference thing.
I think he's just adding it directly to their… config API for OTEL.
And was hoping that this would be, like.
Something upstream, so that if a new temporality preference thing came along, he wouldn't have to care.
**Tyler Yahn** 08:16 Yeah, I… so… I mean, I think it sounds like what he's looking for is, like, an auto package that we have for, like, the auto propagator, or the auto-exporter, or something like that.
But, like, that doesn't really make sense here.
**David Ashpole (dashpole)** 08:35 No, I don't think it's quite the auto package.
Because that's all… the auto package is basically, like, Use environment variables.
to get… An exporter, or, like, a thing, right?
But this is… use… Use a snippet of… or, like, use… Structured config or something to get That piece, right?
**Tyler Yahn** 08:59 Yeah, but, like, that… but still, like, I'm saying, like, the mapping there is, like.
Like, what are you gonna get out of this?
Because, like, okay, so, like, at its core, like, get structured config to map this to a temporality selector function.
Right? So it's like… What are you gonna do with that fun shirt?
**David Ashpole (dashpole)** 09:21 When they parse their config, and they look at the value.
They'll… the string value that somebody put?
They'll throw that at… are… mapping function, and then construct a tracer provider or whatever, with whatever, or I guess.
**Tyler Yahn** 09:38 Yeah, but that's.
**David Ashpole (dashpole)** 09:39 provider. That's what I'm saying, right? Like, if you're gonna… I could write that function, too.
**Tyler Yahn** 09:42 Well, yeah, but, like, because, like, we already provide the meter provider thing, so, like, if you want to just provide just this little snippet, like, to configure the temporality of a meter provider, then, like, configure the meter provider with the Opitel telemetry configuration.
But, like, if you just want to just pass the temporality preference to get a temporality selector, like, you're going to get a go function back.
**David Ashpole (dashpole)** 10:06 Yes, that's what they… I think that's what they want.
**Tyler Yahn** 10:10 then go write it, like, go write some… because, like, you're gonna need to do something with that go function, so… go write the parsing there.
**David Ashpole (dashpole)** 10:19 Yep, I… I think that's… I think that's reasonable, like, but we wouldn't… If someone wanted to expose these constants and the mapping of these constants to the functions, in a hotelConf, we would say.
Sorry, no thank you, right?
**Tyler Yahn** 10:35 Yeah, I don't… yeah, because I don't, like, I don't see the function, like, I don't see… when I see that as, like, a secondary, like, configuration method, it's like… yeah, like, which is fine, like, if you want to go do that, but, like, I think that that's on you to go handle that at that point.
Like, I think we want to standardize on, like, our OpenTelemetry configuration file format to configure meter providers the way that, like, it's defined in the OTelConf.
And I think, like, these… Values here aren't specified anywhere.
As far as I can tell.
**David Ashpole (dashpole)** 11:10 in the OpenTelemetry configuration.
repo, right?
Like, that this key means.
**Tyler Yahn** 11:19 So, yeah, I mean, like, in the context of an OpenTelemetry configuration, I think that that makes sense.
But, like I'm saying, like, generically allowing some sort of enum here, like, I… like, that's a little bit… beyond what that specification includes, is what I'm saying.
**David Ashpole (dashpole)** 11:35 Yeah, I don't think we're required to accept this.
Right? Like, we're just required to parse.
a full config file. It's more a question of, like.
like, one, it's not going to… like, these… I'm sure these enums exist in the OTELConf package somewhere already, right?
And the mapping function from the enum to the thing already exists.
I, like, I guarantee it, like, search for low memory in, not in configuration, but in…
**Tyler Yahn** 12:03 Why not here?
**David Ashpole (dashpole)** 12:04 in Otalkov.
This is.
**Tyler Yahn** 12:13 I… okay. I mean, I don't… why wouldn't it be here?
**David Ashpole (dashpole)** 12:16 This is where that's from.
Sorry, let me… let me paste it. Where should I paste it? In the Zoom chat?
**Tyler Yahn** 12:30 Oh, I guess it's… oh, see, I mean, it's low underscore memory.
Which is already… Yeah.
So, I mean, I, I, like, I think if that's… Yeah.
like, I think this having this here defined here is, like, where I'd want this to be, and parsing it in… the OTL config package, I think, makes sense.
Exposing it, I don't think makes sense, though.
**David Ashpole (dashpole)** 13:03 It would almost be like… It'd almost be like making this function here public.
If you can share that.
**Tyler Yahn** 13:17 Yeah, sorry, let me see if we can find… Yeah, I mean… I'm still not, like, understanding the use case here. Like, why would you need this, and why do we want to, like, expose this?
And why wouldn't, like, we want an end user to do this on their own?
**David Ashpole (dashpole)** 14:13 Hmm.
**Tyler Yahn** 14:18 I mean, it's like, I get the case where it's like, first off, like, say this needs to get fixed, right? Which it does.
Like, but the user wants it to be… this. This form.
It's like, okay, then I think they should be the ones that parse that.
And they should… she should handle that appropriately, because, like, this mapping is kind of my question, is, like, if you need this switch statement somewhere, like, that's great, but, like, you're gonna get, like, some sort of option here, and, like, what you do with that option then is up to you, I guess.
So, like, defining canonically a new type to, like, map here, seems… like, overkill. That I don't think there's a lot of use, and I think it's just gonna pollute the API.
**David Ashpole (dashpole)** 15:05 Yep.
I see that.
I think… I think you're probably right. I understand why people are doing it, because The config file format isn't stable yet.
And… They want to be able to put little bits… like, people are making their own config file formats?
And… like… I think that's where this is coming from, is that, like, Knative or whatever project this is.
Is adding their own config, and they're throwing in, like.
Two or three of the options that… Like, they're not supporting as much stuff as we are.
But they're like, oh yeah, like, let's throw in compression and temporality selector, and like, that'll be it. And the rest we're gonna lock down.
**Tyler Yahn** 15:52 But, I mean, I think that that's, like.
**David Ashpole (dashpole)** 15:54 Then they can just re-implement that, is what you're saying.
**Tyler Yahn** 15:56 Well, I think they can re-implement that, and I think that, like, it serves us better to not provide this in that case, because we really don't want these bespoke configuration file formats, we do want to try to standardize.
on the OTEL configuration file format.
So, like, I… I think that, like.
it's not like it's completely blocked in their ability to handle this, but I do think that, like.
Making it easy to define your own is, like.
**David Ashpole (dashpole)** 16:24 I'm just not, like, I'm not, like, opposed to doing that, but it's also just, like.
**Tyler Yahn** 16:28 promoting other file formats, I think, is something that we don't really want to be, like, working on and building our APIs around.
**David Ashpole (dashpole)** 16:36 I think that's fine.
**Tyler Yahn** 16:39 Yeah, okay. So maybe… yeah.
Okay, I don't know what, I guess, else to say on this one, then.
Is this, hmm.
I mean, we can try to… I can try to capture this and just say that, like, that's our standardization, like, we want… standardization on the OpenTelemetry configuration file format.
**David Ashpole (dashpole)** 17:02 If there's a… if there's a…
**Tyler Yahn** 17:04 Use case we're missing, like, happy to better understand that.
**David Ashpole (dashpole)** 17:17 Yeah, you can ask more about the use case, but I think… If we're not gonna support… It's like, if it existed anywhere, it would… it would be an OTELConf, but it sounds like we're not interested in that.
**Tyler Yahn** 17:41 Yeah, or, I mean, or a third-party package. Like, there's nothing… like, if you wanted to make a…
**David Ashpole (dashpole)** 17:47 it's… if it's a third party, I think the… the goal is that it's, like, shared and used by everything, so it's like, if HotelConf and other places that we pay attention to.
**Tyler Yahn** 17:59 aren't gonna use it.
That's the thing, is like, if it's shared by everything, like, it needs to be the hotel configuration file format. That… that's what we want to promote. Like, if somebody else wants to say, like, I'm gonna do an alternate, like, configuration file format, and I'm gonna support this temporality preference, like, selector thing.
**David Ashpole (dashpole)** 18:14 Yep.
**Tyler Yahn** 18:15 But, sure.
**David Ashpole (dashpole)** 18:16 No, no, I don't think they're trying to deviate. My point was always that they… they want… essentially a small snippet of the OTEL config file format. They just don't want the whole YAML, right?
**Tyler Yahn** 18:34 And why, like…
**David Ashpole (dashpole)** 18:38 Because they're exposing a more limited set of the OTL SDK to their users.
**Tyler Yahn** 18:46 And, like, so, is it not possible for them to, like, compose that YAML file based on, like, their translation? So… If they have, like, a specific set of… values, and one of them is, like, temporality preference.
Can they take it?
**David Ashpole (dashpole)** 19:04 They assume that they're using the OTLP gRPC trace exporter, right? So they're not doing anything with metrics, they're using… like, this is the case for Kubernetes, right? We're using the OTLP trace… gRPC exporter, and the only thing you can configure is the endpoint.
**Tyler Yahn** 19:24 Yeah, so…
**David Ashpole (dashpole)** 19:25 So, say…
**Tyler Yahn** 19:25 So, okay.
**David Ashpole (dashpole)** 19:26 fields.
**Tyler Yahn** 19:27 there's two fields in, like, some sort of, like, YAML object that you received, right? Like, so then can you take that YAML object and translate that into a… Hotel Konf, like, definition that has.
**David Ashpole (dashpole)** 19:38 Like, inflate it?
**Tyler Yahn** 19:39 Yeah, yeah, yeah. But it's just restricted to that, yeah.
**David Ashpole (dashpole)** 19:43 Right, so you could take your… format.
That has, like, two fields in it.
But it would be kind of… it would be a little bit tricky to try and, like, recreate a whole OTEL config file format.
With just those two fields set, right?
**Tyler Yahn** 20:01 Well, it's not a whole, because it's, like, just the tracing portion that you need is, like, what you're saying, right?
**David Ashpole (dashpole)** 20:09 So…
**Tyler Yahn** 20:17 So, I mean, like, you're gonna…
**David Ashpole (dashpole)** 20:24 I'm saying that's what I would like to encourage people to do, is if they need a subset.
Then they can come to OTELConf.
And it kind of like auto-export lets you get just an exporter.
Like, it would be nice… it would be cool if there was, like.
config file parsing, but only from some nested layer, like, give me an OTLP HTTP exporter from file.
And it just contains the OTLP HTTP.
the stuff inside that, in the YAML, right? Because then, a different project that knows they're only supporting the OTLP HTTP exporter could embed that in their config.
And be done.
Yeah. And then parse from there, right?
**Tyler Yahn** 21:11 Yeah, I mean, I could see that. That seems reasonable.
**David Ashpole (dashpole)** 21:14 So, And I… I was viewing this… request as, like, a subset of that, where they don't even just want the OTLB HTTP selector, they just want the… parsing of… I can't see it, but.
**Tyler Yahn** 21:29 Yeah, it's not just the trace one, but, like, this is…
**David Ashpole (dashpole)** 21:32 This is, like, an option, right?
But you're right, it doesn't even give you… The temporality preference option here is actually specific to the exporter, though, right? Like, it's…
**Tyler Yahn** 21:47 Yeah.
**David Ashpole (dashpole)** 21:47 there's gonna be a different one per OTLP HTTP, or, like, per OTLP exporter.
**Tyler Yahn** 21:53 Yeah, versus, like, a Prometheus exporter or a.
**David Ashpole (dashpole)** 21:57 common one for OTLP and gRPC?
**Tyler Yahn** 22:00 Yeah, I mean, it's… it uses the both. OTLP in general uses these temporality selection, like, fields the same way.
**David Ashpole (dashpole)** 22:07 But the option… no, I mean the option is the same. Like, our actual…
**Tyler Yahn** 22:11 Oh.
**David Ashpole (dashpole)** 22:12 turns.
**Tyler Yahn** 22:13 No, it's specific to the package. Like, in code, yeah. Like, the configuration is not specific, but what you get out of it to configure something, like, in code is, yeah.
**David Ashpole (dashpole)** 22:23 So then I don't think this makes as much sense. I think we could offer… We could offer, like.
Exporter level parsing.
you know, give me an OTLPHDP exporter from this YAML or something, but it feels like this… is… Smaller than we'd like.
**Tyler Yahn** 22:44 Yeah, I agree.
**David Ashpole (dashpole)** 22:46 Okay.
**Tyler Yahn** 22:47 Yeah.
That makes sense to me.
I mean, I, I…
**David Ashpole (dashpole)** 22:56 Anyways, I think we've talked enough about it.
**Tyler Yahn** 23:01 Okay.
Yeah, because I definitely, like, the way it's currently structured, though, is, like, it's kind of a non-starter. Like, it definitely does not need to get added here. Like, that's… it's never gonna make sense.
So I think that, like.
Yeah, better understanding the use case of what they're trying to accomplish may help structure the OTELConf package, but, like.
I don't think this is the approach that we want to accept, so maybe it's something like that in our response here.
**David Ashpole (dashpole)** 23:31 Okay.
**Tyler Yahn** 23:33 Okay.
Next up, exporters, Prometheus, migrate to the new configuration option. This is, I think, done? Or the portion of it, part of this is done, right?
**David Ashpole (dashpole)** 23:49 Yeah, yeah, we need to decide… you can remove this from the milestone. We need to decide if we're gonna deprecate the existing ones.
**Tyler Yahn** 23:55 Yeah, okay.
I'm all about deprecating the existing ones, I just, like, people were, in the Prometheus world, hesitant to do that.
I mean, there's definitely no way I'd want to release this Prometheus Exporter as stable without Removing this first, so…
**David Ashpole (dashpole)** 24:12 Yep.
**Tyler Yahn** 24:14 Whether that goes through the deprecation cycle or not, like… I think that it'd be ideal, because we probably have users that are expecting this to be stable already, but yeah.
Anyways, that's in the next milestone. Also here, improved error handling for Prometheus.
**David Ashpole (dashpole)** 24:29 We can remove… or, like, that's fine to have in, or find a… like, somebody's working on it, but they… I don't think they've responded in a while.
**Tyler Yahn** 24:37 Okay.
It looks like there's a PR for it.
**David Ashpole (dashpole)** 24:40 Yes.
**Tyler Yahn** 24:46 Yeah.
Is this just looking for more reviews, actually?
**David Ashpole (dashpole)** 25:00 Oh, is it?
**Tyler Yahn** 25:02 Yeah, and I think.
**David Ashpole (dashpole)** 25:04 Okay, then… then they did res… they must have fixed it, and .
**Tyler Yahn** 25:09 Okay.
Well, I mean, so you still have these internal, error errors, create errors.
**David Ashpole (dashpole)** 25:16 I think they just didn't resolve any of the conversations.
**Tyler Yahn** 25:19 Okay.
**David Ashpole (dashpole)** 25:20 Alright, well, I can… I can take a look afterwards, then. This might… this might be ready to merge, then. Yeah.
**Tyler Yahn** 25:26 Okay, also, high heatux contention in metric sums. I think this is resolved. Yep. Yeah, okay.
Do you know the PR number?
**David Ashpole (dashpole)** 25:43 I can find it quick.
**Tyler Yahn** 25:44 Okay.
**David Ashpole (dashpole)** 25:45 Or you can probably find it faster.
**Tyler Yahn** 25:47 Mmm… we'll see.
I think it's this one right here, 7427, right?
**David Ashpole (dashpole)** 26:03 Yep, 7427.
Okay.
**Tyler Yahn** 26:18 Okay, awesome. Alright, so, on these other ones, the SDK trace observability… I did ping people on these this past week.
I think if they didn't respond of, like, Or if they don't have a PR open, I think I was double-checking on this, but I think everything is up to date.
Obviously, nothing's blocking, we could release without these PRs, but, Yeah, because they're all, like, single unified PR, so it's not like… getting in the way of anything, but yeah, I think these should be up to date. If somebody's working on it, I ping them. If they aren't working on it, I've also unassigned it or moved it out of the milestone, so… Yeah, I think that the PRs, these are the issues. We have PRs here, here, here… There, there's the error handling one we need to review on.
So I think that's it for those. There's obviously these as well for this hotel HTTP, but there's actually reviews for all of these as well. So those are done. So the only thing left, I think, is this.
PR here… Looks like there's one review fixed attribute. This is the… yes.
This is speeding up the algorithm to actually do the deduplications. Taking a look at this, it looks like I think it needs another review.
Yeah.
It does need another review. So, it also is on me to take another review, or other people on the call to take another,
**David Ashpole (dashpole)** 27:57 Yep.
**Tyler Yahn** 27:58 Other, another, other, other tech look, but otherwise, yeah.
Okay, so it looks like we're pretty good. These, There's nothing really blocking here that we want to get out.
No. It's just about getting things done, so yeah, alright.
Jump into the contribib milestone… Cannot record error for spins when producing new semantic conventions.
Checker tape.
Never returns an empty attribute.
This looks like just cleanup, I don't know if this is bug.
Error type attribute.
Yeah, I think this is… Oh… hmm.
I think this actually might be resolved by that new error type function that I had added. I think this is asking if… the error type is, like, going to be just, like, a built-in type, then maybe record it as an exception, but I don't know if that's the right behavior. But if it is gonna be, like, an error type attribute itself, then record it as an error type attribute.
I think… I think that makes sense, cause, like, if this is gonna be, like, a canonical… like, HTTP error type, which I hope we can do, actually. So, essentially, like, the goal here is, like, if it's a response, like, I don't know, 400 or something like that, record this as, like, error type 400, or error type, you know, bad gateway, or bad request, something like that.
And if it's not that, like, say it's like a, I don't know, an internal error or something like that, then record it as an exception, I think is the idea, and you wouldn't record it with, like, this error type value. Our logic here assumes that, but I think that this is correct, like, this isn't right. But we'd have to refactor a lot of the error parsing here, which is something…
**David Ashpole (dashpole)** 30:16 I'm actually looking at…
**Tyler Yahn** 30:19 And another PR for the exporters, so that might be something I could pick up. I don't think this is a blocking thing for this next milestone, but yeah.
This definitely looks related to something I've looked at, so, yeah.
Wow, there's a lot of conversation here.
Okay.
So, yeah, I think there's just maybe some ideas to look into, nothing to actually block on, but yeah.
Okay.
That's the end of the milestones, I can stop… sharing here… any other topics y'all wanted to talk about or discuss? Top of mind?
**David Ashpole (dashpole)** 30:59 Happy to discuss anything to do with… the PRs I have open, if you have… and there's just 3 of us on the call, and I'm sure… Bride wouldn't hate us if we talked about.
**Tyler Yahn** 31:10 optimizing.
**David Ashpole (dashpole)** 31:11 exemplar reservoirs or something, so I don't know if there's any questions you had or, like, stuff you wanted to talk through, but…
**Tyler Yahn** 31:16 Which, yeah, maybe I could take a look at what you have open, because I, I haven't… Looked back at the… histogram optimization one yet?
**David Ashpole (dashpole)** 31:26 reservoir that's open and actionable, and then there's the histogram itself, that's now open.
But that one's pretty… Yeah, I think… Yeah.
That one's a little bit more involved. It'll probably take some time.
**Tyler Yahn** 31:44 Yeah, well, we got time.
**David Ashpole (dashpole)** 31:46 Yep.
**Tyler Yahn** 31:54 Yeah, this one, I think I've already approved. It's more just looking for another approver, right? Yeah, so…
**David Ashpole (dashpole)** 32:03 We'll have to find someone.
**Tyler Yahn** 32:04 That's awesome.
**David Ashpole (dashpole)** 32:04 Probably not that important, because it doesn't do anything until the… Histogram PR is in.
**Tyler Yahn** 32:10 Right, right. Cool. And then, yeah, maybe take a look at this again.
I… I left that comment, that was, like, as far as I got into reviewing. I… not… I'm guessing you might not.
Yeah.
**David Ashpole (dashpole)** 32:25 This is actually fun, but I can add a comment explaining it if it's helpful.
**Tyler Yahn** 32:33 So, I… yeah, I think you're… I mean, I… I was thinking about this afterwards as well. There's a few things I think we might want to think about here.
So… I don't think there's, like, a data race in the sense that it's gonna panic, but I do think that there is, like, a, maybe more of an inefficiency here? Like, obviously, if, there's, like, a partial update, it's not gonna really matter, because there's a comparison going on here. So if, like, there's two things trying to update, you know, the min and the max at the same time.
and one updates it, and then the other updates it, like, if the other is still less, it'll still update it, right? So, like, that kind of thing isn't really, I think, more… That really isn't an issue. This is set as a little odd, That seems like there might be an issue there.
**David Ashpole (dashpole)** 33:25 The, the, like, wide we have is set?
**Tyler Yahn** 33:28 Well, I'm guessing we have it set because we can't distinguish between the zero… In the non-set, yeah. And so that's… that's more, I think, what I was trying to also accomplish in this, like, pointer, atomic pointer thing, is, like, you can distinguish the tri-state where you have set, unset, and then a zero value.
Yeah, that was kind of one of the ones where I was like, huh, that's kind of interesting, because, like, if you're… Like, if you both go in at the same time, and you get this value, and it's not set, but then one of them sets this, and it sets it to zero, like, isn't that gonna be a problem?
**David Ashpole (dashpole)** 34:02 Yeah, yeah, so… if… If… if it's set to zero, Let's see… You might be right.
If we set… if we set it to zero, then both min and And there's a bug that I can see, because I used min-loaded equals 0.
**Tyler Yahn** 34:30 Oh, yeah. For the second statement, but… Yeah. But, yeah. Good catch.
**David Ashpole (dashpole)** 35:00 I think you're right. I think there is an issue here.
Because if men… The isSet doesn't work, basically, where something can write isSet after we've… Read the false value, and then… Then we respect the zero.
**Tyler Yahn** 35:16 Right. That was loaded.
Yeah, and so I think, I was thinking about it, I don't think you need this full min-max Extrema, but I do think that if you had, like, a, you know, one value.
**David Ashpole (dashpole)** 35:31 Here that has a set flag as well, so you could load the set and the value at the same time.
**Tyler Yahn** 35:36 And then the compare swap can actually, like, validate that, like, you're doing, you know…
**David Ashpole (dashpole)** 35:40 That is correct, yeah.
**Tyler Yahn** 35:43 So I think this… this could get updated. I also don't know if we want to…
**David Ashpole (dashpole)** 35:48 the full UN64 range for this, right? Because… Or is this an N64 instrument?
**Tyler Yahn** 35:56 It's only… we only support N64 and Float64s.
**David Ashpole (dashpole)** 36:01 But we need the full in 64, right? We can't do a… We can't steal one of the bits for… is it set, right?
**Tyler Yahn** 36:09 Oh, oh, I see what you're saying. Yeah, correct. Yeah, we can't do that.
**David Ashpole (dashpole)** 36:12 Yeah.
**Tyler Yahn** 36:13 I mean.
**David Ashpole (dashpole)** 36:14 Are you suggesting something different?
**Tyler Yahn** 36:16 Yeah, I mean, you just have a type like this.
**David Ashpole (dashpole)** 36:18 Yeah. So instead of the type…
**Tyler Yahn** 36:20 including both the min and max, just have, like, it being the value, N, and then set flag.
And then, sorry, let me take a look at this.
**David Ashpole (dashpole)** 36:32 I did actually have this as the initial implementation.
**Tyler Yahn** 36:35 Yeah. Essentially what you…
**David Ashpole (dashpole)** 36:37 Showed, and it was… it was a pretty… it was a bit slower.
For sure.
**Tyler Yahn** 36:49 Interesting. I… yeah.
**David Ashpole (dashpole)** 36:50 I think maybe because I was using atomic.value and not atomic.pointer.
**Tyler Yahn** 36:56 Yeah… That's… that's also the other thing, is I'd want to look at the allocation space and see if that would affect it.
If we're allocating a new pointer every time that we're trying to, like.
override or something like that, then it might be something… this is something I wanted to take a look at. I was also going to take a look at the value as well, but…
**David Ashpole (dashpole)** 37:14 Yeah.
**Tyler Yahn** 37:14 I haven't… like I said, I haven't gone back to this, but… but I do think that, like, storing this in some… like, the set value needs to be somehow included in this field here, in some sort of atomic way, I think.
Yeah, I'd have to take a look and think again. But I see what you're saying.
Hmm.
Yeah, I'd have to look. Yeah, but I don't know, like, I'd be interested to know why the value didn't… took longer.
I mean, obviously, you're gonna have to do some, like, not typecasting, but typecasting. Usually it's, you know, nanoseconds, though. Like… Anyways, I can take another look at that. But yeah, I haven't, like, I got there, I looked at this briefly, like, how it was used in extremas, but the actual inter… like… algorithm for the rest of this, like, I didn't.
**David Ashpole (dashpole)** 38:12 Yes.
**Tyler Yahn** 38:13 Yeah, I haven't gone through all that yet.
**David Ashpole (dashpole)** 38:15 That's fine. Okay.
**Tyler Yahn** 38:17 But yeah, I could take another look at this as well, My plan was taking a look at this, I just haven't got back to it yet.
**David Ashpole (dashpole)** 38:23 That's fine. Yeah.
**Tyler Yahn** 38:26 Okay.
**David Ashpole (dashpole)** 38:28 But, I think I've also, got your…
**Tyler Yahn** 38:31 Yours turning over there to try to figure it out as well, so… I might… might look at an update first, yeah.
Okay, well, cool.
Brian, I don't know if you're able to get a review going, as well, but those two PRs would be, I think, ideal if you want to take a look.
**Bryan Boreham** 38:52 So… 7474, was it?
**Tyler Yahn** 38:58 7474? Yeah, and, let me see… 7443, yeah.
Okay. They should look… pretty familiar to you, I'm guessing, but yeah.
You're muted as well, David.
**David Ashpole (dashpole)** 39:28 Yeah, it should look kind of familiar. It would be like if you took the Prometheus SDK and then did the same thing, but for deltas as well.
**Bryan Boreham** 39:38 Alright, I'll, I'll… yeah, I'm not actually not familiar with the Prometheus client library so much.
But I'll take a look.
**Tyler Yahn** 39:48 Cool.
Okay, awesome.
Well, I guess, any other topics?
If not, that's a lot, so, yeah.
Cool. Well, we can end here. Good seeing y'all. Good talk, good discussion. I will see you all in a week's time, or acute nursing.
**David Ashpole (dashpole)** 40:11 Yep, bye.
**Bryan Boreham** 40:13 Yeah.
