SIG: Configuration WG
Date: 2025-09-29
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/NQW83wNbIXHkdZ-7LJMZaNigY_NVEUgPTZiajO__LxKxeCoK2j0p1fPtwORMtuWM.9EqQ-fyd7eLqk8nF
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:12 Hello!
**Tyler Yahn** 01:15 Hey, Gregor. How's it going?
**GZ Gregor Zeitlinger** 01:17 Hard?
**Tyler Yahn** 01:24 Greg, where are you based out of?
**GZ Gregor Zeitlinger** 01:28 Berlin.
**Tyler Yahn** 01:30 Len, so, I'm in the US, in Portland, Oregon.
**GZ Gregor Zeitlinger** 01:37 Oh, that's where you're trying to fend off… federal police.
**Tyler Yahn** 01:43 Yeah, I was downtown this weekend, I didn't see any, I don't… it's, it's a little weird.
**GZ Gregor Zeitlinger** 01:50 Let's hope it stays that way.
**Tyler Yahn** 01:53 Yeah.
Yeah, that's a whole thing.
You said, you said Lenda, is that in Switzerland?
**GZ Gregor Zeitlinger** 02:04 Berlin, Germany.
**Tyler Yahn** 02:05 Oh, Berlin. Oh, okay.
Oh, cool.
Yeah, yeah.
**GZ Gregor Zeitlinger** 02:11 We're just hoping that the Russian drones don't get near… anywhere near us.
**Tyler Yahn** 02:18 That's, I think I'd rather not have drones dropping bombs on my head.
Yeah.
Fair enough.
**GZ Gregor Zeitlinger** 02:29 Absolutely.
**Tyler Yahn** 02:30 Yeah.
I'm looking at the agenda, I don't… I see a bunch of things on there, I didn't put most of them on there.
I know Alex put one of those on there. I don't see Alex joining, though.
**GZ Gregor Zeitlinger** 02:51 I think I put… 1 on there.
**Tyler Yahn** 02:55 Okay.
**GZ Gregor Zeitlinger** 03:14 Right, the default value handling. But the good news is that the documentation has been published. I think I already mentioned it, but now it's published.
**Tyler Yahn** 03:23 Yeah, yeah, I saw that. I was pretty excited about that as well. So, yeah, thanks for getting that together, appreciate it.
Oh, there's Alex.
**Alex Boten** 03:36 Hello.
**Tyler Yahn** 03:37 Hey.
**GZ Gregor Zeitlinger** 03:38 Hello?
**Tyler Yahn** 03:47 Cool. Alright, I think with Alex here, we can probably jump in. If you haven't yet, go ahead and add your name to the attendees list. And, yeah, I can… Kick us off. So, Gregor, you wanted to talk about this PR for the default values of the declared configuration.
**GZ Gregor Zeitlinger** 04:06 Yep, I know that, Jack has answered something.
But to be honest, I… I still don't get how… Our contributors to declarative configuration should look up the value Was not a clear answer. Yes, look into this file.
**Tyler Yahn** 04:31 Hmm.
**GZ Gregor Zeitlinger** 04:34 from, my experience, I think… what the previous, users answered is correct, so you can either look into the kitchen sink configuration.
Or in the migration config, and they both should have the same value.
Because they are generated from the same sources.
As far as I understand.
**Tyler Yahn** 05:06 They should have the same… value… for… for a field, or… I feel like some of those… You're just saying, like, they should have the same value if it's present, but if it's not present, then…
**GZ Gregor Zeitlinger** 05:20 So, in the migration config, the default value is, in a part of the variable substitution syntax. So after, colon dash, you have the default value.
**Tyler Yahn** 05:38 Right. Oh, I see what you're saying. Yeah, that makes sense.
**GZ Gregor Zeitlinger** 05:42 And I think in the kitchen config example, it is a comment what the default value is. Oh, here it also says, if omitted or null .
**Tyler Yahn** 05:55 Yeah… I feel like, though, that… Isn't the default value just the thing that's the default for the OpenTelemetry, like, specification?
**GZ Gregor Zeitlinger** 06:10 Yeah, that is what Jack was saying, and I think he's right, but I don't understand where… Where you can look up this default value.
If we add this missing piece, just look there, then I think, it would be easier to understand.
**Tyler Yahn** 06:29 Mmm, I think I see what you're saying, because, like, the default value that is in, like, this migration… config is defined in the, like, the environment variable configuration for this specification.
And we don't have an equivalent for the declarative config, is what the problem is. Or we don't even say, like.
Well, it's actually not the default value, right? Because the default value is going to have to be up to… The implementers of this.
And I guess, yeah, I guess I hear what you're saying, like, it's not obvious that the environment variable Default value is the same for declarative config.
**GZ Gregor Zeitlinger** 07:08 Now, let me… let me try a different word. When you're implementing, declarative configuration for a language.
you're wondering, what should I put as the default value for batch spend processor delay if the user has omitted the explicit value? This is regardless of environment variables.
**Tyler Yahn** 07:34 Oh, sure, I gotcha, but, what I'm saying is just that, like, the environment variable configuration, or specification is the place that already has that definition, and then, like, I think, to Jack's point, like, we would want to use the same default, right?
Yeah, so let's, let's see, like… Yeah, so, like, all of this, this default information, like, I would just assume that the implementer would use that by default as well?
But what I'm saying is, like, your point is that, like, that's not obvious, right? Like, that's not… immediately clear that this is the same for declarative configuration, right? And so we should probably clarify that.
**GZ Gregor Zeitlinger** 08:17 I also did not, See that this is exactly the place where you should look.
**Tyler Yahn** 08:24 Oh, okay, yeah.
Yeah.
That's a good question, actually.
**GZ Gregor Zeitlinger** 08:34 I think it's not a question. If we just add this, piece, just look on that page, and it gives you the default, that's, That is probably a good answer.
**Tyler Yahn** 08:45 Yeah, I… .
**Alex Boten** 08:48 Assuming… assuming all the values are in here.
I'm…
**Tyler Yahn** 08:52 Yeah, yeah.
**Alex Boten** 08:53 That might be an optimistic view of it, but…
**GZ Gregor Zeitlinger** 08:56 It doesn't matter, we should say the values should be there, and if there's some missing, then we will add the missing.
**Alex Boten** 09:04 Yep.
**GZ Gregor Zeitlinger** 09:04 We will find the missing link, but this is a good starting point.
**Alex Boten** 09:09 Yep.
**Tyler Yahn** 09:11 Yeah, I mean, I think that the… yeah, that's a good point, because, like, this actually probably also has its own… Protocol details… yeah… there's, like, more configuration I know for the OTLP that's not included here, for some reason.
**GZ Gregor Zeitlinger** 09:28 Okay.
**Tyler Yahn** 09:29 To your point, I think 90% of it is. I… Yeah, maybe this is just a way, like, yeah, maybe you're right. Maybe this is a good way to answer your question, is just to say, use these defaults. I think in the long term, given that we want to just, like, discourage environment variables in the favor of declarative configuration, we may want to, like… restructure the specification, but maybe that's not, the point we're at at this point. Like, just pointing here and saying, like, the defaults here should be the defaults there.
I guess the thing is, though, that we need to, like… I guess we have this, right? We have a migration config.
It's a little confusing.
Cause then the problem is, is like, okay, cool, like, if… if you're just looking at, like, the kitchen sink, right?
And you have, like, this processor here, like, okay, what's the default here? Well, you have to know that the scheduled delay is migrated from something else. The schedule delay is migrated from the hotel BSP schedule delay, and then you have to go look that up, right?
So… That might be a little bit confusing. I wonder if we can make this a little bit easier to follow.
But, yeah.
These look pretty… I mean, I don't know, this looks like there is a one-to-one mapping, essentially, of all the defaults that we would want, so…
**GZ Gregor Zeitlinger** 10:50 Yeah, I mean, in the long run, if we are saying that declarative configuration It's the recommended way, then… We would probably update the specification that… so that they refer to the, path in the YAML file explicitly, so that you don't have to make this two-step process of… Environment variable, default value.
**Tyler Yahn** 11:17 Agreed. Yeah, I think that's… that's probably the way we want to do this in the long term.
Okay, so yeah, maybe both of those could be answers to that question. Are you, able to respond to the, the issue, Gregor?
**GZ Gregor Zeitlinger** 11:33 Yeah, just please include the page that you just had open so I don't have to look it up again in the.
**Tyler Yahn** 11:39 Yeah.
**GZ Gregor Zeitlinger** 11:39 Yeah, exactly, just in the meeting doc, and then I can put it there.
**Tyler Yahn** 11:44 Yep.
**GZ Gregor Zeitlinger** 11:45 Thanks.
**Tyler Yahn** 11:46 Easy to do. Perfect.
**GZ Gregor Zeitlinger** 11:48 Okay.
**Tyler Yahn** 11:50 Next up, Alex, you wanted to talk about Enable Disable Pretty Prints.
**Alex Boten** 11:54 Yeah, want to talk about it is maybe a strong statement. Someone… someone came up with this, issue, if you look at the linked related issue.
When, looking at the output from a console exporter, the current… SDK implementation in Go prints using PrettyPrint, you know, this… this is just the way it was implemented. I don't know that we have a consistent, standard for how the console exporter should behave. In fact, I think we, in the spec, we specifically say, don't rely on the output of the console exporter, so, you know, your mileage may vary, but that's not super helpful for end users. And so the… the suggestion here from Jurassi was, you know, is there a way to enable or disable pretty print?
And I thought it was a valid question, we don't have that today, do we want to have it? And that's… that's what the issue I opened was, to just… Put a decision on whether or not we want to enable it, and, that's it.
**Tyler Yahn** 13:06 Yeah, I think that's gonna be really problematic, actually.
Cause I, like, I think… Yeah, like, there is no standard for this, like, I mean, there's not even a standard that it is… I'll put it in JSON, like… Yeah. Like, there's… you can come up with literally your own standard, which we used to actually have here in the Go, pretty, like, outputter.
So to, like, just assume that, like, another language doesn't… or that also, like, pretty prints… they're not pretty prints… just puts things on new lines based on, like, you know, a JSON structure, like, that's, I think, not gonna… Always be the case.
**Alex Boten** 13:53 Yep.
**Tyler Yahn** 13:54 I also think that, like.
**GZ Gregor Zeitlinger** 13:58 There's another problem to this.
Which is, that, We probably don't want to guarantee that the console output is always going to stay that way, and we have an alternative, at least it's implemented in Java, but it's also in the spec, which is the, The OTLP file, or OTLP std out exporter, which explicitly says that it is OTLP.
Yep.
I think that would be the better answer, and having pretty print there also makes more sense, because it has a defined format.
**Tyler Yahn** 14:39 Right.
Yeah, I agree. I think that if you start looking at this as some sort of interchange format, like, that's just not gonna… Be a good… Assumption?
for exactly the reasons that Gregor just said, like, there's not even a stability guarantee on, like, the output format here, like, let alone, like, the consistency across languages, so you would want to use something that we do provide a guarantee on.
for an interchange format, like the OTLP exporter in whatever form, flavor you want that, right? Like, that's always been our response in the Go Siga as well.
Is, is that, like… That's kind of by design, like, you really should not be using this as something you can consume, and expect the format that you're consuming is gonna be, like, the same or stable.
I also like… Yeah, I mean, like, you could always… yeah.
Because, like, my first response is, like, well, why don't you just use JQ to, like, put this all in one line? And I'm like… but then, like, it's also, like, maybe that's even, like.
something that is gonna change in the future, like, there's really not a guarantee on the format here.
**Alex Boten** 15:54 Yeah, so, that's fine. I added a comment at the bottom, I think this can probably be closed. I'll open a separate issue to implement the OTLP file exporter in Go, because that's not… as far as I can tell right now, that's not currently supported.
Yeah. So, I'll just… I'll just follow that, follow that up.
**Tyler Yahn** 16:11 Yeah, I think… I think that's fair. I think another one is also, like, a third-party exporter would be great, if you can configure that.
Which is something we would need for some sort of, like, the pluggable ability of this configuration.
Because, like, if, you know, yeah, if you wanted to define your own exporter that does output JSON to standard out, and that, like, puts it all in one line, like, I think you should be able to do that. It's just, yeah, how you configure it, I think, is kind of the harder part.
**Alex Boten** 16:36 Yep.
Okay.
Cool. Do you want to close that issue, since I don't actually have the ability to close this issue?
**Tyler Yahn** 16:46 Yeah.
I can… I can close it.
**Alex Boten** 16:52 Okay.
**Tyler Yahn** 16:55 I can… yeah, okay.
We'll see if Jurassi's happy with that, but… okay.
**Alex Boten** 17:04 Cool. The next two issues are kind of related.
I suspect they're just maybe an oversight, but, if you open… if you open them up, they're just, there's some inconsistencies in the signals between the… tracing signal and the logs and metric signals. So for example, here, in the tracer provider config.
They're… is… If you scroll down just a little bit, yeah, so you can see the tracer provider definition has a required field, where the other ones don't.
And my question was just, which one is right, so I could make them consistent.
And this is true for the other issue as well, for 305. It's the same kind of thing, where… I was just trying to implement them in, Go, and… the output from the JSON generator is different for these two, so… for these three.
**Tyler Yahn** 18:11 Yeah, that is a little… odd.
Hmm.
**GZ Gregor Zeitlinger** 18:20 What is the difference there?
**Tyler Yahn** 18:23 The… this required fields, for disabled?
**GZ Gregor Zeitlinger** 18:27 Okay.
**Tyler Yahn** 18:28 In any of the other ones. So, you can provide disabled or not in these other ones, but…
**Alex Boten** 18:35 Yeah, yeah, yeah, so it's just… It's inconsistent.
I suspect we want them to be not required for all of them.
And somehow the tracer config just got accidentally put in there, but…
**Tyler Yahn** 18:50 Yeah, I think what it was is this was the first one, and so it was probably one of those things where we did that, and then maybe something changed, or maybe we just realized that that wasn't needed to be required, and so we didn't do it for the others, but… Yeah, I agree, I don't think it… Hmm.
I don't think it is required.
**GZ Gregor Zeitlinger** 19:12 I've never put that disabled there.
**Tyler Yahn** 19:17 In, in the… for the experimental tracer config?
**GZ Gregor Zeitlinger** 19:22 Is that different from the normal tracer?
**Tyler Yahn** 19:26 So it's the… it's a different type than the Tracer.
**GZ Gregor Zeitlinger** 19:30 Oh, okay, yeah, probably just used the regular trace, I got it, okay.
**Tyler Yahn** 19:34 Yeah.
**Alex Boten** 19:35 Yep.
**Tyler Yahn** 19:36 It may actually stem from the specification, too. I kind of wonder if that may be it.
**Alex Boten** 19:51 Yeah, it's all to do with the trace configurator, right?
**Tyler Yahn** 19:54 Yeah.
I don't see any requirement here either, so… maybe not, maybe it's just a mistake.
Yeah, I think… I think you're right, I think it's just maybe… The consistency wasn't there, so we could probably just remove it, yeah.
**Alex Boten** 20:18 That's fine. I'll, I'll remove it, and then I can… then I can, I guess… I can't remember if I did a release of RC2 last week, I think I did.
Didn't I?
**Tyler Yahn** 20:31 I saw it, but I didn't. Oops.
**Alex Boten** 20:33 I started it, but I haven't, so I'll include these changes in RSC2 as well.
**Tyler Yahn** 20:38 Okay.
**Alex Boten** 20:39 And then we'll… we won't need to do an RC3. Although, I guess it's experimental anyway, so it doesn't really matter if it's… If it's done before RC2 or not, but… It would make my life easier, so I'll just do it.
**Tyler Yahn** 20:55 Yeah, I mean, that sounds good to me.
Similar here is what you're saying also, though?
**Alex Boten** 21:01 Yeah, so again, if I… I guess I missed the other… there it is. The naming config is required on the Tracer config, but not on the, Meter and logger providers, so…
**Tyler Yahn** 21:16 Tracer matcher in config?
**Alex Boten** 21:19 Oh, okay, yeah, alright.
**Tyler Yahn** 21:22 Yeah, alright, yeah, I mean, I think that that makes sense.
**Alex Boten** 21:26 Cool, thank you.
**Tyler Yahn** 21:27 Cool. Alright.
Alright, last up, I've got just the triage of the project board. We can go, I think, maybe just review this.
A lot done, a lot in progress, tracking language implementations, this is still something we're working on.
Yeah, I think… I think there's a lot of great movement, especially in, like, JavaScript Alex is still working on the go.
So, yeah, I think this is still… Works in progress.
**GZ Gregor Zeitlinger** 21:58 Actually, I have a question there.
Is any of the languages ready to be used by users?
So… Should they be added to the documentation, or is it too early for them?
**Alex Boten** 22:15 I guess it depends on what you mean, ready to be used.
We've been using the Go implementation internally at Honeycomb As well as inside the collector for… months now. Actually, almost a year, I think.
**GZ Gregor Zeitlinger** 22:34 Yeah, well, it means more like, We are fine with end users using it.
still, giving the caution that it's experimental, like I pointed out for Java.
But, otherwise, happy to be used by anyone.
**Tyler Yahn** 22:59 I mean, I… Yeah, I… it's… it's an open source, non-stable like, thing, as long as they understand that, like, I think we want to promote that, like, because that's how you get feedback, right? Like, we definitely don't want to, like… Take down production, but we also don't want them to just shy away from it entirely.
How would.
**GZ Gregor Zeitlinger** 23:20 What do you mean by takedown production?
**Tyler Yahn** 23:23 Oh, I mean, I… I don't… I can see you've never worked operations.
I have. Just… oh, okay, alright, so just, like, somebody, like, you know, releasing something experimental, and then they upgrade, and the upgrade path is not… like, it causes breakages, and so, you know, it can cause code breakages. I don't, I don't know, I'm just more of a…
**GZ Gregor Zeitlinger** 23:43 Right, but code breakage doesn't mean it's not ready for production, this is something different.
**Tyler Yahn** 23:48 It, it does if you're not… I think… I think it does if you're not, careful in the operations space, right? Like, if you, if you cause breakages and you just blindly roll something out, like, you can cause issues, right? So, to those, to those users, yeah. But to… to the, to the Gregors out there who are careful and who are paying attention, like, yeah, I don't… I think you're right, like, I think you can start… You know, telling them to start using it, and that they'll be careful, and so it's not like, yeah.
It's the other user that goes and that does the things blindly, and then they blame OpenTelemetry for being a bad project, because they did, you know… Something that was a little reckless, I think is the only thing we want to prevent.
**GZ Gregor Zeitlinger** 24:27 That… that's why, we have the experimental, warning for Java. But, I mean, 3 months ago, Java was also RC1, or whatever the latest version was at the time, and I have spent roughly 3 months working on everything in Java that, I… new was not working, so some features that were working with system properties or environment variables, and not with declarative configuration, and that is what I have added before doing the documentation, so… For the other languages, I could imagine that there are also features that are available in environment variables.
And that are not working for declarative configuration.
And actually, I have not mapped all the features, but I have called out all the features that are not mapped, so that users are at least aware. And this is the level of, detail that I would expect from, from documentation, to be… to be ready for end users. Yeah, that's my take.
**Tyler Yahn** 25:48 Okay, so, I mean, like, to Alex's point, though, like, I think, like, in the Go space, it's a very… we definitely have encouraged people to use this, and we do see organic use of this. You're suggesting maybe we need to… document this in, like, the OpenTelemetry website?
**GZ Gregor Zeitlinger** 26:05 Exactly, I think otherwise it's quite hard to get organic growth.
Because otherwise, you are looking for expert users who are digging through the source code.
To find out that this exists, and this is,
**Tyler Yahn** 26:19 I think that's exactly who we're looking for, as the expert users, but, I, I, you know, if another language is looking for something else a little bit more universal, I think that that seems reasonable, too.
**GZ Gregor Zeitlinger** 26:32 that this might take for Java, yeah. I want also non-expert users. And if you're saying the other languages, it's only for expert users, then everything is good, and we should not document more.
**Tyler Yahn** 26:43 Well, I mean, I can't speak for all the languages, obviously, that are on here, but yeah, like, if you're… if you're interested in popularizing this prior to the 1.0, like, I don't… like, I'd be interested, too, to get feedback. It goes a little further behind, we're still working to get to that, RC.
But, I guess if you're suggesting to make a change to the docs website, I'm interested in reviewing it, like, that definitely sounds like a positive thing that I'd be open to adding, yeah.
Is that what you're suggesting, Gregor?
**GZ Gregor Zeitlinger** 27:19 I'm not… I'm not suggesting to work on it myself. My question was, does it first make sense to have it on the documentation website? And then the second question would be, how do we get people to work on it?
**Tyler Yahn** 27:33 Oh, yeah, I think to get people to work on it, you just have to do it. I think that's kind of the thing we would have to help include our services there.
And I don't think there's any opposition to it, it's just that, I guess maybe the point is you need to find somebody to do it.
**GZ Gregor Zeitlinger** 27:53 Okay, so what would be a good way, I mean, this meeting, I thought, would be a good place, but we're not many people here.
**Tyler Yahn** 28:03 Yeah, I mean, it's… yeah, I… I don't know what to say, like, I… I guess… Just going back to the… being an open source project, like, if… if you have an idea.
it's kind of on you at that point to implement that idea, so if you wanted to update the docs, I think that it would be on you or for you to find somebody to update the docs.
**GZ Gregor Zeitlinger** 28:27 What I'm trying to say is, are there… people for the other languages that I can ping.
just asking them, here, I have done this in Java, do you want to do an equivalent? This is all I'm offering.
**Tyler Yahn** 28:41 Hmm.
**GZ Gregor Zeitlinger** 28:42 Like, giving the right person a ping so that they can think about doing it. I don't have capacity for more, but this is something that I would do.
And if you know who is working on those, just putting a name here in the meeting doc, and then I can talk to the people That would already be something that might or might not work, but it's not a lot of work for me to try.
**Tyler Yahn** 29:05 I mean, I… I… Don't know specifically, I think JavaScript, that was, Marlio, right?
**GZ Gregor Zeitlinger** 29:14 Right, yeah, I know that.
**Tyler Yahn** 29:15 Yeah, I know, I know Go is Alex, I know Erlang is, Tristan.
**Alex Boten** 29:24 Yeah.
**GZ Gregor Zeitlinger** 29:26 Let me write that down, otherwise I'll forget.
**Tyler Yahn** 29:29 Okay.
Alex, do you know more…
**Alex Boten** 29:33 Yeah.
**Tyler Yahn** 29:33 developers?
**Alex Boten** 29:35 Yeah, I think, Mark was doing the C++ implementation.
And, Brett was doing the PHP one.
Can you write it, in our meeting?
**GZ Gregor Zeitlinger** 29:47 That would be great.
**Alex Boten** 29:48 to them.
**Tyler Yahn** 29:55 Yeah, I wonder… who was doing the Python one?
**Alex Boten** 29:59 Diego was doing the…
**Tyler Yahn** 30:00 Diego.
**Alex Boten** 30:01 But it's been… it's been left behind.
**Tyler Yahn** 30:04 Yeah, yeah.
**Alex Boten** 30:05 Yep.
**GZ Gregor Zeitlinger** 30:11 Who is, Brett and Mark? I…
**Alex Boten** 30:13 Yeah, let me just… Just find there. Ring a name?
**Tyler Yahn** 30:17 Mark is… I think he may even be on this issue.
**Alex Boten** 30:21 Here's Brett.
**Tyler Yahn** 30:23 from PHP.
Here's Tristan, from Erlang.
I don't see Mark on here. Here's Diego.
Oh, here's Mark. Mark Kals.
**Alex Boten** 30:34 Yeah, I put… I put the link to their, GitHub on…
**GZ Gregor Zeitlinger** 30:38 That's great, thanks.
**Alex Boten** 30:41 On the dock as well.
**Tyler Yahn** 30:47 Yeah.
**GZ Gregor Zeitlinger** 30:51 Cool, thanks. That's all the ones we have, right? I mean, except Java, that's me.
**Tyler Yahn** 30:56 Yeah, except for this Java one, yeah.
**GZ Gregor Zeitlinger** 31:00 Correct. Cool.
**Tyler Yahn** 31:01 So, next up… And the board is, tracking stabilization of declarative configuration. This is still something that's, active.
If I'm not mistaken, yes. And, I think this is still just waiting on implementations and feedback. Obviously, like, we have another RC coming out, so there's another cycle, coming up, so yeah.
Also on the in progress is the add HTTP node methods.
**GZ Gregor Zeitlinger** 31:37 Yeah, I have not found time to work on that.
For quite some time.
**Tyler Yahn** 31:44 Yeah. Okay.
So this just needs some… some feedback, or, some… More cycles on this one, then.
**GZ Gregor Zeitlinger** 31:55 Yeah, right.
**Tyler Yahn** 31:56 Perfect.
Okay, still SDK startup specification, declared config, default values, so the default values… I think this is in progress, I don't know if it's to-do… well, I guess it's… yeah, maybe it's still to-do, because we're trying to figure this out still. We… we were talking about it earlier.
And the SDK startup specification… Hmm, this looks like it's coming from the entity sig.
Yeah, I think this is just something… that needs to be, I think, worked in the implementations, but I don't think this is actually blocking the configuration format.
stabilization I don't know why I added it then.
Probably because I was asked by the entity SIG.
A little while ago.
Yeah, I don't know, I'd have to take, I think, a little more look at this. I think this is something that we can tackle in a post 1.0, but I'll have to take another look.
Okay.
The… also on here is requirements for distributions of configuration.
This is something, Gregor, you had opened?
**GZ Gregor Zeitlinger** 33:31 Yep, I have, created a prototype, for the Grafana distribution, But I was actually wondering what the goal of the ticket is.
I want to collect some use cases. What users do?
I guess I should have to summarize what I found out. Basically, my takeaway is, That it is possible, with a reasonable amount of effort.
To create a distribution that supports both Environment variables and declarative configuration.
Yeah, but I need to write it up better.
So it's… it's okay to leave it in progress.
**Tyler Yahn** 34:38 Should I put this in progress?
**GZ Gregor Zeitlinger** 34:40 Yeah, yeah, that's fair.
**Tyler Yahn** 34:42 And then I'll assign it to you.
**GZ Gregor Zeitlinger** 34:44 Yep.
**Tyler Yahn** 34:47 Okay.
Cool how to handle additional exporter config parameters.
Like, this is… yeah, it's a good question.
Yeah, this is exactly what we were talking about with the pretty print as well.
**GZ Gregor Zeitlinger** 35:10 I mean, pretty print is a special question. In general, we have.
An answer that… You can add subproperties under exporters.
**Tyler Yahn** 35:21 Yeah, right, exactly.
**GZ Gregor Zeitlinger** 35:27 And we have examples for that, I think something like Endpoint, isn't it?
**Tyler Yahn** 35:32 I think you're right.
Thought I saw that.
**GZ Gregor Zeitlinger** 35:58 Oh, this sounds like, In Go, you have a property for OTLP that is not covered by the general schema.
I'm just reading the last sentence.
And the suggestion is, if you have one with a different name, then you have all the liberty to use whatever properties you want to.
**Tyler Yahn** 36:25 Yeah, I… that's kind of what… I thought… This register component thing was what we would be using here, but…
**GZ Gregor Zeitlinger** 36:34 We do, but if you use one of the well-known exporters, then you're also limited to the properties of that exporter. This is, I think this was added to make sure That, all languages use the same properties for a well-defined exporter.
**Tyler Yahn** 36:56 Yeah, I mean, I think you're right.
I don't think that was their original intention. I think they were looking to have other… things per language defined, but I think you are right in that, like, I don't think they should be doing that. I think that if… If they want to go off and add new properties, every language should implement those properties, so… yeah.
**GZ Gregor Zeitlinger** 37:17 Exactly.
**Tyler Yahn** 37:18 Yeah, I don't…
**GZ Gregor Zeitlinger** 37:19 Like, the philosophy of declarative, or not just declarative configuration, of the hotel configuration in general, that you have cross-language portability.
**Tyler Yahn** 37:28 Right, 100%. Yeah, I agree with you.
I don't know why we would… Yeah, that would… exactly. I, I think… okay.
**GZ Gregor Zeitlinger** 37:41 I mean, I can understand that it's easier to add something just for one language, because you don't have to go through the process of The specification.
**Tyler Yahn** 37:51 Right, but it doesn't serve the community, so I agree, I don't know why they would… I don't think we'd want to move ahead with allowing Some languages to have additional fields for established… Yeah, okay, so this just probably needs some words.
Configuration SDK create to accept programmatic SDK options.
It currently returns the top-level OTL component.
I don't get it. I don't either.
I don't know, I will… I don't… I could ask Robert.
**GZ Gregor Zeitlinger** 39:03 I would have to look at the prototype implementation to understand what's going on.
**Tyler Yahn** 39:09 Oh, provider options.
Oof.
I don't know why we want to do this. So provider options are things for, like, the tracer provider, and setting things.
**GZ Gregor Zeitlinger** 39:25 Can you explain the use case? What…
**Tyler Yahn** 39:28 No, because I don't think that that's a great idea. I think what they want to do is they want to mix configuration. So they want to mix programmatic configuration with, yeah, file-based options.
**GZ Gregor Zeitlinger** 39:39 Oh, yeah, that is a muddy water, I think.
**Tyler Yahn** 39:43 Yeah, I really don't… oh, we merged this?
Yeah… I don't know why we merged this.
I don't… like, maybe there's just something that you can do with these provider options that… you can't do with the configuration, but I think that that's a problem for… what we just described, like, either those provider options are doing something outside the specification, which I… as the author of Go, I don't think that's the case, or… This is just… this just seems like it's gonna be very problematic.
**GZ Gregor Zeitlinger** 40:40 Hmm.
**Tyler Yahn** 40:43 Okay.
I… I might want to go take a look at this one again. I don't know if we should have merged this. This seems like a can of worms.
Okay.
Missing environment variable for cardinality limit.
I don't know why we'd want to add a…
**GZ Gregor Zeitlinger** 41:16 Maybe it was… Supported before?
**Tyler Yahn** 41:20 What's that?
**GZ Gregor Zeitlinger** 41:22 Maybe because there already is an environment variable?
**Tyler Yahn** 41:27 I don't… I don't think so. I don't… I think we ever wanted to define an environment variable for this. We just want to use The cardinality limit from… declarative config, and to not add more environment variables to the specification.
**GZ Gregor Zeitlinger** 41:43 Yeah, yeah, I thought it was a case where an environment variable exists, and someone wants to have it in declarative configuration, not the other way around.
**Tyler Yahn** 41:52 Yeah.
**GZ Gregor Zeitlinger** 42:00 Oh yeah, it says missing environment variable, never mind, yeah. No, I… There is no guarantee that, That will add environment variables for things in declarative configuration, even if it's possible.
**Tyler Yahn** 42:16 Yeah, I… I don't… I think, yeah, I think their request is to add some sort of… Exception here.
But I think that there's… I don't know.
**GZ Gregor Zeitlinger** 42:32 I can request an exception, but, don't… It's not because it's available in declarative configuration.
**Tyler Yahn** 42:40 No, it's.
**GZ Gregor Zeitlinger** 42:41 That'd be nice.
**Tyler Yahn** 42:41 Collaborative Config… this working group has been… the de facto, like, from the specification, they see us as the one that arbitrates whether we want to add another environment variable or just add it to the declarative configuration, because there's conflict between the two, and so I think that… My, my… My response is, like, I would rather we don't add another environment variable.
**GZ Gregor Zeitlinger** 43:04 Because then everyone has that support for it, or what is.
**Tyler Yahn** 43:08 Yeah, everyone has to add support for it. It's, again, something that we have to add compatibility into the, you know, our… Our path forward for users, whereas we want them to be using the configuration file going forward.
**GZ Gregor Zeitlinger** 43:21 Yeah, it takes brain cycles at the wrong place.
**Tyler Yahn** 43:25 Correct, yeah.
So, I… okay, this also needs some words.
Looks like there's a few of them.
Okay, and then the last one is the at MTLS, This one. Client key password and certification revocation configuration options for OTLP Exporter.
Whoa.
There's no way I want to do that.
That is not something I want to do.
Okay.
**GZ Gregor Zeitlinger** 44:04 You mean this is a case where you have an environment variable, but you still don't want to add it to declarative configuration?
**Tyler Yahn** 44:10 Yeah, no way.
**GZ Gregor Zeitlinger** 44:14 But what are you telling users who, want to migrate?
**Tyler Yahn** 44:21 No, I think they… this doesn't exist. This environment variable doesn't exist right now, and they want to add it.
And I, I think that's a really bad idea.
Yeah, plain text passwords like that in an environment where you are, like, ripe for security issues. Yeah.
Okay.
**GZ Gregor Zeitlinger** 44:44 I mean, you can encrypt them.
**Tyler Yahn** 44:47 Yeah, I would expect something, right? Like… The problem is, is if you encrypt them, you also need, like, a whole encryption scheme there.
**GZ Gregor Zeitlinger** 44:58 No, I mean, you can encrypt it on the… Kubernetes plane, and then, decrypted.
**Tyler Yahn** 45:04 Yes.
**GZ Gregor Zeitlinger** 45:05 The application, something like that.
**Tyler Yahn** 45:08 Yeah, something like that. I mean, there's definitely ways to get around, like, just having these plain text passwords. I just, like, it, like, provides a mechanism, I think, that would be… I don't know, I don't think that's a really good idea. I would like to understand, I think, the… the problem here.
**GZ Gregor Zeitlinger** 45:54 I had started work on a specification.
to allow pluggable exporters, but, didn't, get very far with it.
Maybe that would be a way where… You can, Solve this problem at the user space level, because you can provide your own pluggable exporter.
**Tyler Yahn** 46:22 Yeah, I think you're right. I think that that'd be helpful, especially if it's something that, like, you wanted to do in OTLP, you could just wrap that OTLP exporter in whatever Decryption methods you needed, and…
**GZ Gregor Zeitlinger** 46:36 That's essentially it, yes.
**Tyler Yahn** 46:37 Yeah.
Yeah, okay. I think that could be… That makes sense to me.
I would not want to…
**GZ Gregor Zeitlinger** 46:49 I don't know if you want to, reference this, Issue, because it's in a very early stage, it's not really clear Where and if this is going anywhere at all.
**Tyler Yahn** 47:03 Your, your pluggable exporters?
**GZ Gregor Zeitlinger** 47:05 Exactly.
**Tyler Yahn** 47:07 Yeah, I, We don't have to add it at this point, I don't think. We can… if we have a solution, we can come back. This is in the project board, so we'll probably touch base on this issue again.
**GZ Gregor Zeitlinger** 47:19 Okay.
**Tyler Yahn** 47:22 Yeah, that sounds good.
Okay. Well, I think that's the end of the issues that are in the project board, gone through them all.
Seems like Alex has dropped, yeah.
**GZ Gregor Zeitlinger** 47:38 we're not talking to yourself at the end.
**Tyler Yahn** 47:41 Yeah, I appreciate that. Thanks for hanging out.
**GZ Gregor Zeitlinger** 47:45 Alright, have a great day.
**Tyler Yahn** 47:48 See ya. Bye.
**GZ Gregor Zeitlinger** 47:49 Cheer?
