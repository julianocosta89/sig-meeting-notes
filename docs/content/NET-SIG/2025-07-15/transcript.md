SIG: .NET SIG
Date: 2025-07-15
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Yevhenii Solomchenko** 00:11 Hmm.
**Martin Costello** 00:13 Hi.
**Alan West** 01:51 Hey! Friends.
**Yevhenii Solomchenko** 01:56 Right.
**Martin Costello** 01:58 Hey!
**Alan West** 02:18 As usual. You have anything for the agenda. Feel free to place it on there.
go ahead and share my screen.
Oh, somebody's got something we got something to talk about.
Oh, maybe we don't. You were just on your name. You have Henny.
**Yevhenii Solomchenko** 03:29 My name is Johanny.
**Alan West** 03:31 Okay.
I'll just move you up underneath the attendees if you don't mind.
Okay, so it doesn't seem like we've got anything in the way of agenda today. I was out last week, or I missed last week's meeting. I was also out a little bit last week.
so been catching up with things a little bit this week.
are there any Prs that people are aware of that are
worthy of discussing while we're all together?
I think most of the ones here are ones that have been sitting there for a little while. So.
and I've not had a chance to catch up on this particular one, Martin. This one looks like it's gotten some approval
performance tweak.
**Martin Costello** 04:48 Yeah, this one. This one's Matt's Matt's fault. He happened to point out that the library had its own
TLPC. O.
Protobuff thing, and I was curious, and looked at the code, and then thought, Oh, this could be improved!
**Alan West** 05:07 Cool. Okay, sounds good.
Take a look.
See if we can get emerged.
And then I think theater has been kind of on top of
this one. He's pinged me for a few of the Prs that he's opened, but otherwise
I think he's he's been commenting on a lot of these. Pr, so
we don't need to go into that here unless again, unless there's anything that people want to
want to discuss on the contribut side.
Okay.
**Yevhenii Solomchenko** 05:53 On a contribut. I want to discuss one issue about configuration. SDK.
**Alan West** 06:01 Oh, sure configuration! What do you mean?
**Yevhenii Solomchenko** 06:06 Yeah, we have in specification configuration.
It's creating. For example, file based configuration.
**Alan West** 06:14 Hmm, right.
**Yevhenii Solomchenko** 06:15 Yeah, I I think.
it's not only our team want to implement that. We also for now implementing that in the instrumentation.
But now, Rasmus and Robert from our team decide to maybe make it in the Contrip repository.
So
we're thinking, if we, if you guys want also to be part of that one trip.
It's a repository, open telemetry, configuration, another repository.
**Alan West** 07:06 Right? Yeah, there's a separate repository for that, too. I think eventually it's gonna the reason why I brought up the
Something like that. Probably.
I think there's
it's a it's it's going to become part of the proper specification, I believe, at some point.
See if this is it.
Yeah.
I'd almost be inclined to say that this is this is something that belongs in the main
repository. Given that, it's that it's spec driven rather than contribute.
It's it's not the
technically, it doesn't really matter where it belongs or or where where it resides. But but our general pattern has been that things that are
driven by the by, the spec, typically go into the main SDK.
**Yevhenii Solomchenko** 08:09 Okay.
**Alan West** 08:11 That's a minor point. But I think.
but I yeah, I think this is a great thing to to to kick off.
Have you have. You guys already started working on like a proof of concept or anything.
**Yevhenii Solomchenko** 08:27 We start working kid on that and auto instrumentation.
But now we decide to move it to country. Because I think guys from elastic also on that feature.
**Alan West** 08:43 Okay, cool. You know, I think, really.
**Yevhenii Solomchenko** 08:49 I want to say, how about Grafana guys? I I heard you also want that feature
am right, Martin.
**Martin Costello** 09:03 I think so so far, mainly someone else on our team who works primarily in Java has been working on it.
But I am. I imagine we'll probably come around to it in the.net space
at some point to, but he's like ploughing away at the moment on the Java side on that.
**Yevhenii Solomchenko** 09:29 Okay.
**Alan West** 09:34 I think, somewhat related to this and potentially
something that would make sense to leverage. Is Blanche a while back, I wanna say, like, I don't know.
Over a year ago, probably, Lance, you did that work to kind of automagically, Bootstrap the SDK
and this is effectively
oh, it's similar in my mind to that. You basically have a configuration file. And with minimal to maybe almost no code
you, just the SDK gets gets configured, based off the declarative configuration.
I don't know if you still have that on a branch, do you, bledge.
**Mike "Blanch" Blanchard** 10:27 It's out there somewhere, I would say. You know, if I was going to build this today.
what I would do is there is
now, in the main. SDK, you have the open telemetry builder Api.
which is where you would mount like cross cutting
concerns. So you could. Do you know.
if you're using the hosting package you call what is it? Services? Add open telemetry. It gives you a builder back.
There's also the sort of detached way where you can say like
open telemetry. SDK, dot create something like that. It gives you back a builder.
But the idea would be, you have a some package somewhere.
you know. Open telemetry configuration that just has an extension on that builder. So users have that package, and then they call, like, you know, add open telemetry dot with configuration.
and then it just goes and loads the file, and then orchestrates all the you know, set sampler and processor blah blah whatever it needs to do.
The key thing is that it's not
woven directly into the SDK. It's like an add on package.
There may be pushback trying to put it all into the SDK.
**Alan West** 12:04 You're saying that that hmm!
You think moving all of that into the SDK would be necessary for making that work.
**Mike "Blanch" Blanchard** 12:14 No, I would.
I would hope we don't do that
like you have all the builder Apis, so I don't think it needs to be part of the SDK. If we ran into things where there were gaps, I think it would be better just to, you know, extend the Apis and the SDK, and make this type of thing possible.
**Alan West** 12:38 Yeah, I think that's what I'd hope for as well. A separate package that you could take a dependency on. Say, you want this
and and provide your configuration file.
If I remember you opened up a Pr.
**Mike "Blanch" Blanchard** 13:04 Yeah, I had something way back.
I think that was all. Before we have that builder.
The builder just gives you a more elegant spot to kind of mount that extension.
**Alan West** 13:18 Right conceptually, though I wonder if your Pr. Would have.
I don't even know what to search for. SDK configuration.
**Mike "Blanch" Blanchard** 13:28 Search for the word like auto.
**Alan West** 13:31 I just see what I got here.
2023. That's probably that seems
seems like it was more recent than that auto.
**Mike "Blanch" Blanchard** 13:52 It was a long time ago.
Hmm!
Auto configurations start from the top.
**Alan West** 14:03 Oh, yep.
2022. Wow, okay, yeah, this was, this was quite some time ago. Though.
Again, yeah, you're right. This was this would have been, this would have been before
the pattern, the open telemetry builder pattern that you you implemented. But.
**Mike "Blanch" Blanchard** 14:29 Yeah. Cause. Conceptually, it's the same. It's just now we have a way to do things that are cross cutting, which
is great for this use case.
**Alan West** 14:39 Right, right.
**Mike "Blanch" Blanchard** 14:40 Before you would have had 3 extensions, and you would have had to attach it, you know, to tracing metrics and logs. But now you can do it in one shot.
and for these, you know, distros like elastic, has one.
I assume, like Grafana has one.
Those distros can stitch this up automatically. You know. I assume these distros have their own top level thing, like builder dot services dot add elastic, open telemetry or something.
It can just make that call. So it's transparent to the user when you use a distro.
But when you're setting up more manually, you know, when you're piecing in components, you'll have to add the configuration package and then stitch up that call.
Why is it?
Why should it not be part of the SDK?
Well, I think there's a number of reasons for that. The primary is that this configuration package
needs to be aware of all the the components that you can
turn on like Otlp exporter. I don't know if Zipkin still a thing, Prometheus.
we don't want all those dependencies in the SDK right? That would invert the whole tree.
So this
configuration package is itself sort of a distro, because it needs to have all the dependencies to all the things you want to turn on.
or it needs, like some massive reflection or plugin architecture, to like find those things automatically
seems a little bit problematic. But there's also this idea that
there's many different ways to configure things.
Open telemetry here is being very opinionated. I don't know if it's like a yaml or a json, but
I don't know if
it's standard across the.net ecosystem like in the SDK. We've tried to pick some standards like we support. I configuration.net native things.
It just makes more sense to me to keep this as an add on and not
force it. You know, into platforms that already have their own configuration, probably based on like I configuration provider and stuff like that.
You could try to parse like. If you look at eye configuration and Microsoft extensions.
you can plug in any number of sources. Right? You can do, Json, you can do, console. You can do environment variables. You can do cloud configuration.
This thing could mount itself into that.
It could parse this configuration file and convert it to I configuration style. And then
auto configuration could just use I configuration.
Why, that might be cool is
you could do these features in your app settings, Dot Json, if you wanted to. If you could mirror the same config structure, or you could use the hotel configuration file, it would just be abstracted away. I don't know if that's a necessary thing, but it's a possibility.
Does that make sense at all. So it's kind of sort of a 2 faced thing. So what this package could do is it could read this hotel configuration file plug itself into I configuration, and then the actual bootstrapping just runs off of I configuration.
So if you want to use the hotel config file, it'll all work if you want to use. I configuration environment variables or like command line switches. It would also work without any extra development having to be done.
**Matthew Hensley** 18:35 I was hoping
that this would land in I configuration land, if only because it's consistent with the existing instrumentation.
And
it's just one less thing to have to target, you know, if we wanna target eye options or options monitor and
can be pretty ignorant as far as where this stuff is populated, from
which has been pretty handy onnet framework, where.
**Mike "Blanch" Blanchard** 19:03 Settings can be fun.
That would be the very idiomatic.net way to do it.
It's sort of a very advanced thing, but
it would be cool for.net users to be able to generally use. I configuration.
**Martin Costello** 19:28 Yeah, it would definitely be nice if you could just add it on as like the last configuration source, because I think the specs a bit opinionated on. If you use this stuff, then it wins, no matter what.
So you'd put it in right at the end and then just go. But if there's anything in the hotel, config file, then override everything else. But if you didn't want that, you could put it earlier in the chain if you didn't want to strictly follow the spec yourself as a user.
**Mike "Blanch" Blanchard** 19:57 Yeah, we have. We sort of have that situation today. Like in the SDK,
we support the spec environment variables, not all of them, but a good set of them.
So what we do is
we just look in, I configuration for those keys. So we will populate the environment variables into I configuration. But you are free to override those environment variables via the command line or your app settings, dot Json.
So you can
put yourself in a situation where the environment variable is overwritten by something later. You own that
when you set up your I configuration order is very important.
So we have seen issues from people saying, like, Hey, the environment variable should always win.
We just don't follow that. And
there's not a lot of complaining.
So this would be
a similar situation, where, depending on how you register your sources. If you do the config file first, st and then you do your app settings, dot Json, and you override some stuff
the config file won't apply, so I call that a feature. Some users call that a a break.
**Martin Costello** 21:17 Yeah, I I think I agree with you on that one that that makes more sense because there was a Pr in the last week.
Well, many, many prs, many issues from a specific contributor. And he's essentially they've essentially got a they want to do configuration through a database, and they like wanna override loads of the detector stuff through config.
So they want a giant like Config object to like, populate with values and then give to to hotel, and it feels like that use case could be better served by just having these configuration overwrites, and you just plum them in because I think the thing they're trying to
ask for needs like an object that has like one to one of every possible configuration setting you could ever have. And you have to update the library if there's ever a new one
right? But then he's bank. He wants to bind it to some custom proprietary schema which doesn't feel like it really fits, and you could just set your own attributes.
But if what they want to do with that feels like it plugs in with this idea, which is just, you compose the configuration from an arbitrary place.
**Mike "Blanch" Blanchard** 22:34 Yeah.
**Alan West** 22:45 I'm curious. If any of you
Have you considered some of the things that we're talking about here
in the approach that you think you'd take like? What? What would have you thought about yet?
What you'd want that like Api surface area to look like? What's the entry point or way that someone basically
invokes auto configuration. Have you thought about like using? I configuration? Or have you thought about other options?
**Yevhenii Solomchenko** 23:16 I think we didn't think about that.
So deep. For now, because we just started to
at 1st in the auto implementation level. But now
we think about to move it to.
So I think both ways are can be used.
Think that build the services, and my configuration. I mean.
**Alan West** 23:58 Cool. Yeah. Does auto instrumentation, are you? You? Have you just been
doing? Are you in kind of proof of concept mode, or are you have, you do actually have an implementation for auto configuration at this point that leverages the the schema
from the configure from the specification.
**Yevhenii Solomchenko** 24:17 We just make a file based configuration.
So we parse file and set the settings and the at all.
I know.
**Alan West** 24:31 I see, but like a per like, not not the standard spec format you're just. You've just got your own format file for now.
**Yevhenii Solomchenko** 24:38 No, no, your specification file.
**Alan West** 24:41 Oh, okay, cool.
Well, yeah, I agree with, I think everybody here that this this would be valuable
even just for SDK consumers.
**Yevhenii Solomchenko** 25:02 Okay. It's great great news.
**Alan West** 25:04 Yeah, I just wanted to comment on one other thing that you, said Blanche, as you were talking
with respect to, I agree that it should.
I? I think it makes sense to me as something that is separate from the SDK, a separate package
but on the point of like
it, it taking dependencies on everything.
I've wondered if that's actually, I understand, that has benefits like maybe
in a like an aot kind of environment, or whatever but
some sort of a Plugin architecture, or, you know, probably using reflection, I think, if I remember right.
and anybody anybody chime in that has been tracking this more closely than I have. But if I remember right, I think that the vision
for
this was to support custom stuff, too. I don't know whether they have any.
**Yevhenii Solomchenko** 26:17 For now custom is not included.
For for version, one of the configuration.
**Alan West** 26:26 Gotcha.
**Yevhenii Solomchenko** 26:27 They will only standard what are standard and Xena.
They're okay. Then custom scenes.
**Alan West** 26:37 I see. Yeah, I know that they've talked about that. Yeah. But okay, so for version one.
though, we might want to consider, you know, even though maybe that's not going to make it in version one.
If it is something that they see on the horizon, it may make sense to at least had.
Consider what that might look like in the future.
Because I think at that point we'd have to. We'd have to entertain some sort of a some sort of a way to discover things at Runtime
and not just rely on on hard dependencies between things.
Anyways, another. Another design consideration as you as you start digging into this
cool. So what do you need from this group in in terms of getting going.
**Yevhenii Solomchenko** 27:46 We will count on you to review pairs and like, maybe help with implementation. Something like that.
because for now our country it's a bit bad for community.
**Alan West** 28:07 yeah, as far as implementation. I'm not one, that's gonna have a whole lot of bandwidth
other folks here, may so they can speak.
But from a review standpoint this is definitely something that I'd like to see for sure. So
I think we'll be able to support you with that.
**Yevhenii Solomchenko** 28:33 Okay. Thank you.
**Martin Costello** 28:35 Yeah, I think if there's like
issues with tasks and direction, then maybe we can help and pick out
pick up individual tasks to help contribute to getting it done, because at the moment it's just one big nebulous issue. So it'd be a bit tricky to tackle from multiple places.
**Alan West** 28:56 Yeah, I think that's a good point. Maybe starting with like a overarching plan.
do you want to open up an issue and start kind of start that conversation, if any.
**Yevhenii Solomchenko** 29:19 Could you repeat question.
**Alan West** 29:21 So the the point that Martin brings up is is a good one, right? In order to basically get
get more people working on it. I think it.
We need. We need to start getting concrete and kind of what the what the end goal is, what the guiding light is, where we're and where we're heading. So
would you like to open up an issue and start to kind of hash out
kind of an end to end? Plan
**Yevhenii Solomchenko** 29:49 Yeah, sure, I open, I think issue already opened a bit in the code trip.
**Alan West** 29:57 Oh, okay.
Contribut repo issue.
**Yevhenii Solomchenko** 30:06 And configuration. SDK 5 days ago.
**Alan West** 30:10 Oh, I do see that here.
I'm sorry you pinged me on it.
okay,
yeah. Great. So so then maybe I think I think the next step would just be to kind of start
playing around with some designs, you know, maybe expanding this issue with some potential potential designs, some like.
what would the Api look like? Maybe. What would the
ideal structure, from the standpoint of packaging this look like things like that?
So that we can kind of all agree on kind of like an overarching direction.
And then I think from there I think people will more clearly be able to identify kind of how they can step in and and lend a hand.
**Yevhenii Solomchenko** 31:16 Okay, we think to create another package for that in the country, I think, like.
name it configuration or something like that, and
I think the best, the best option that you'll be injecting from builder services.
Empower and pass the file.
**Alan West** 31:40 Okay. Again, I think I think from the standpoint of where it belongs, I think it. I think you might have.
I feel like given that it's a spec driven thing. I actually think it belongs in the opentelemetry.net project.
and it may.
**Yevhenii Solomchenko** 31:54 Actually make.
**Alan West** 31:55 Your life easier, because, as Blanche was saying, like, it might be beneficial to build something like this on top of the Apis that exist in that repository. So
you may actually find it easier from a development perspective to develop it over there
in case you need to touch anything across across the across those other packages that we already have.
**Yevhenii Solomchenko** 32:24 Okay.
**Alan West** 32:35 Cool anybody else have any other comments on on that.
**Zach Montoya** 32:44 I'll just add myself. I don't know if I met everyone here, but my name's Zach. I am on. I'm
regularly involved in the auto instrumentation side as well as a maintainer. But I'm also interested in in following this work, so happy to to provide reviews or anything I can do to support this as well.
**Yevhenii Solomchenko** 33:07 Hmm.
**Alan West** 33:11 Sounds good.
Alright! Y'all anything else on anyone's mind today.
or should we give some time back?
Sounds good talk to you all next week.
**Zach Montoya** 33:41 Thanks.
**Yevhenii Solomchenko** 33:42 Hi.
