SIG: Go SIG
Date: 2025-10-23
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:20 Hey, Alex.
**Alex Boten** 01:23 Hello.
**Tyler Yahn** 01:24 How's it going?
**Alex Boten** 01:26 It is going. How are you?
**Tyler Yahn** 01:28 Yeah, it is going as well.
**Alex Boten** 01:30 Excellent.
**Tyler Yahn** 01:31 Yeah.
I doubt we're gonna have much, attendance today. It seems like these off weeks, it's pretty sparse. By that, I mean it's just me normally hanging out.
**Alex Boten** 01:44 Alright. Well, that's okay. We can hang out and talk about… One… one issue I have.
**Tyler Yahn** 01:50 Yeah, sounds good.
**Alex Boten** 01:51 Or whatever.
**Tyler Yahn** 01:53 Also, just, I don't know if your issue is that PR, for… JSON and YAML unmarshalling.
But… Yeah, I don't know if you saw, I also, like, it looks good to go. I just made one comment on the error, tag, so yeah, if we wanted to… Yeah, merchant, I…
**Alex Boten** 02:11 I… I applied it to.
**Tyler Yahn** 02:14 Oh, you did.
**Alex Boten** 02:15 suggestion, and it's rebuilding now, so…
**Tyler Yahn** 02:16 Okay, perfect, yeah. Yeah, I just, yeah, it looked… I didn't want to hit the button myself, but it looked minor enough where I was like, But yeah.
Cool. Yeah, okay, well, we'll get that merged. But yeah, let's talk about, the issue.
**Alex Boten** 02:29 Yeah, let me… Just gonna bring the meeting notes and put the issue in the calendar.
Put my name in there, too. There we go.
Okay. It's this issue.
Mostly, I'm looking for recommendation or advice.
On how to add support for this environment variable.
Oh, that got crazy.
Yeah.
**Tyler Yahn** 03:06 Yeah, just looking at this as well, So what, so what is the… Encarin parable, too.
**Alex Boten** 03:15 It… If it's present, it should… load the file, and configure the SDK for end users.
So the idea is that… As an end user, you don't even have to write any code, all you have to do is pass in this hotel experimental config file.
Variable, into whatever your code that's already loading the… OpenTelemetry SDK.
And all the configuration of the SDK should be done via this.
Via whatever you've, specified in your config file.
And, Yeah, so right now, you know, I think JavaScript is implementing this. I… I don't know, there's a… in the matrix… For the spec, it shows us who is implementing it. Let's see… spec compliance.
**Tyler Yahn** 04:17 No, that's not it.
**Alex Boten** 04:20 PHP has implemented it. They're the only ones who've recorded implementing it.
**Tyler Yahn** 04:24 Okay.
**Alex Boten** 04:25 It's… it's a… yeah, yeah, it's right there.
N… Yeah, so I just… I don't really have a good idea of how to implement this in Go. I… I don't know if there's any suggestions, or if we're just going to say not… like, we're not going to implement it, which is also a fine option.
Like, I think most people are… Pretty used to… doing things a little bit more programmatically in Go anyways, but… yeah, I don't know if this is needed for, like, the auto-instrumentation stuff in Go, or whatever, or…
**Tyler Yahn** 05:05 Yeah, I mean, that's a good question, actually.
So definitely, I think, like, the auto instrumentation project would be interested in this, speaking as a maintainer there.
Yeah, I think that'd be interesting to help set up the SDK there. That would be… yeah, I think that'd be pretty neat.
I do think, I do think there's a possibility here. I'm trying to think of how this would work, though.
Because I think it's actually going to cause the import cycle.
Unfortunately.
But, One of the things is, like, we could use, like, the experimental packages to define this environment variable, which is not really that hard, like, Might be a little hard, because it's not going to follow, like, the prefix of OTELGO, but we can… we can work at that. That's not… that's an engineering challenge.
Let me see…
**Alex Boten** 06:05 You mean the experimental package, and you mean inside the SDK, or…
**Tyler Yahn** 06:09 Yeah, so we have them in… no, we have them in, like, the main repo, so what we do is, like.
We have these, like… ability to turn on experimental features through, like, these feature flags, essentially.
there… it's… it's not, like, yeah, one of the challenges is, like, in doing this, like, you don't want to expose experimental features in a, like, stable API, so we have these, like, X packages in this internal.
And what we do here is, you can stop me if you already know what I'm talking about, but, like, we essentially are providing documentation here for all of the experimental features that we provide.
So, like, here, like, this HotelGo X resource, you know, you can set this environment variable, and it will parse this, and wherever in the SDK it needs to… Excuse me. It needs to use this.
it'll, you know, start to take this, and it will take a dependency on this internal X package, because it can do that. And that's not really, like, a problem, because, you know, there's already, like, compatibility… we're pretty explicit on, like, this is not stable, don't depend on it. Obviously, like, things with an X in the name are gonna… change, or things with experimental in the name are gonna change. Yeah. And, like, we try to provide for facing compatibility, but it's not, like… It's not a guarantee it'll always be there, but essentially, this is how we've continued to do this. This is one example. They're littered all throughout this, structure. Essentially, like, we try to have it, like, one X package in a module, not at a package level, but, like, at a module level, would be how we do it. So… Here, I would see it going in this package here, although I'm also kind of surprised, I thought we can… Oh, Yeah, there is another one. Okay, so we didn't document this. There's also, like, this observability feature here. I don't know why we forgot to update the README, but it should contain something for that in the README as well, but essentially, like, you know, there's two different features here, and we would add a feature, and then wherever you use this, you just, like, import this package and say, like, hey, is this enabled or not? Like, a feature flag. It's really, like, straightforward.
But what that means is that… so, this would be for, like, the trace, package, because the trace is in, like, this SDK module. The metrics and logs are not, so… just a heads up, like, you need 3 different versions of this, but I would start with one.
And so the thing is, is then, essentially, like, what I would expect is that, like, the tracer.
**Alex Boten** 08:33 provider…
**Tyler Yahn** 08:35 here… Yeah, like, somewhere, like, here, you could, you could look at that environment variable and see if it's enabled. And if it's enabled, then you can do the setup here. Essentially, like… Yeah, then you have to ask the question of, like, how do you, how do you migrate, or how do you work with, like, provided options? Like, do you… do you ignore them? Do you try to merge them? Do you try to… anyways, that's… that's like a… I think that's another question to answer, but essentially here is where you would say, like, so if somebody in their code had, like, new trace provider, and they had, like, this environment variable defined to point to the config, it should, you know, in that setup process, go to that, config and set it up from there.
Obviously there's a little bit of a… Yeah, actually, maybe that's how I would do it. So, so, yeah, okay, so I would, I would do that. I would probably ignore these past options, But that's, like… I haven't thought all the way through that, but, like, let's just say… let's just say for the sake of this argument, it's easier to think about it this way, like, you just ignore these options.
And what I would do is I would say, like, maybe have, like, an internal package that would set up this, this tracer provider that gets returned based on that config.
And I would say put it in an internal package, because if you put it here in this package, I'm almost positive that the OTelConf package imports this package, so there's going to be a dependency cycle. I think if you put it in an internal package, you should be able to, like, avoid that. There will be a little bit of a dependency.
On that one, by little, I mean there will be one, so I… yeah, that's… this is the thing I'd have to think through a little bit more.
But I… anyways, like… That may not be the end of the world, for this experimental phase, at least. So… Yeah, that's probably how I would go about this, is… so, essentially, then this whole, like, this would get, you know, bypassed, and it would go through that OTelConf setup there. And then, you know, similar for the metrics and the, the logging, providers as well.
**Alex Boten** 10:44 Yeah, I wonder if… Thank you, that was really helpful context. I wonder if it would be helpful to have… so… I guess, as a user… If I set this hotel experimental config file variable… Like, would I Would I still… would I just use the global… tracer provider that's already configured, and assumed that it would be an SDK provider, rather than, like, the default NOAP provider.
And if that's the case, then would… would the experimental package… Be able to set that global… Provider, and have it… I don't know. I, like, I don't know if as a user I would still expect that I would want to call a new tracer provider, or just start tracing in my code, or whatever.
**Tyler Yahn** 11:40 Yeah, I mean, that's actually gonna be, like, the harder part, right, is, like.
where… yeah, where's the entry point? Because, like, it could be either. There's, like, so it's actually a little bit of a… There's a subtlety with the global, like, the OTEL package, because it actually is its own SDK.
Believe it or not, because you have to, you know, there's, like, you can't really depend on one versus the other to, like, build that, and, like, it's got its own logic on how it passes, you know, context and that kind of thing.
So I would see, like, if you're gonna do that, you may… you may just want to have it in both places, to be honest.
**Alex Boten** 12:20 Yep.
**Tyler Yahn** 12:21 Yeah, cause I, like, I… Yeah, because the problem is also, like, Go is an explicit, like, language in how that gets set up, so… whether somebody's passing in a tracer provider from this new tracer provider function, or from, like, the hotel, you know, Git, and so then they can register it at a later point, like, I think that that's kind of up to, like, how they want to write their instrumentation.
**Alex Boten** 12:45 Yeah. But then it's… this is more in the context of, like, the operator of how they want to, like, configure that SDK, so, like, how that gets passed in is kind of…
**Tyler Yahn** 12:54 you know, there's something, like, beyond that. I think that that's kind of, like, the harder part, to answer.
**Alex Boten** 13:00 I don't know, I don't really have a great answer for you there, like, I think it may just be that you may want to do.
**Tyler Yahn** 13:07 Both. I think the global one, you're gonna run into some more complications, though.
for, like, cyclic dependencies there. I haven't thought through that entirely.
But, yeah, that might be a little bit more of a challenge, actually.
**Alex Boten** 13:24 How… I guess, how are other… or, now that I'm looking at the matrix for support of environment variables in Go, like.
Hotel Trace's exporter is not supported.
Or, at least according to this.
document.
Should… I guess the question I have is, should this config file… be supported, or… or… You know, alternatively, is there a good argument for not supporting it?
That's al- it's always an option.
**Tyler Yahn** 13:56 Yeah, I mean, that's also… yeah, maybe that's a good point, really, because, like, Because, like, you could just use the OTelConf package, and it will… it'll build your tracer.
provider there, right? And so, instead of just calling NewTracer from the SDK package to try to shim in this whole thing, it could just be like, well, if you want to do that, like, just call the OTelConf New Tracer provider, and then you can do a.
**Alex Boten** 14:22 he came.
**Tyler Yahn** 14:23 Yeah, yeah, it'll give you the SDK, and, like, you can do whatever environment variables you want at that point. If you wanted to add the support there, we could add the support, I think, to the hotelConf as well, like, maybe…
**Alex Boten** 14:31 you know, some sort of functional, like, implementation there, and it just doesn't even, like, interact with the SDK. I mean, I think that's reasonable as well.
Yep.
Yeah, because, I mean, you look at, you know, our… I guess our close language, you know, C++, and they've specifically called out they're not gonna… support, the config file and bar, as they also don't support a bunch of the other ones, so… So maybe that's okay, maybe that's the real answer, is, you know, in the short term, there's no plan to support it, and… Like, if someone wanted to provide some kind of, like, auto… auto… configure package where you can put the loading of the NVAR Inside, like, an init call.
That would then set the global for you, like, that's… Like, we can always provide even that package in the contribib rep repo and just say, like, if you want to use this environment variable, use this, like, package that's over here, and… This is the way that you would do it, and…
**Tyler Yahn** 15:30 Yeah, and I think… I think we already have that package, right? Like, I think we could just do that in OTelConf, honestly. We could add, like, another function that just says, like.
**Alex Boten** 15:39 Yeah, I don't know. Yeah, you could add, like, a… an, you know, I guess, syntactic sugar function that just does this.
Yeah, or, like, I guess…
**Tyler Yahn** 15:51 you could even add it as, like, a side effect. Like, if it imported the OTelConf package, it could, you know, on init, set up an SDK for you in the global.
Yeah, that's a little… side effects are always a little…
**Alex Boten** 16:05 I love that. I don't love that, but at the same time, you know, maybe it…
**Tyler Yahn** 16:08 Yeah.
**Alex Boten** 16:09 Maybe it fulfills enough of this experimental phase that we can get feedback from users on whether or not they want us, and if people are using it and they're finding weird edge cases, then we can always just turn it off.
**Tyler Yahn** 16:19 Yeah, yeah, that's also true. Yeah, and then you can make it more explicit, like you're saying, like, you know, if you wanted to do this, put this in your own init function, and call this, and it will set it up for you, but otherwise, like, yeah, we don't do that for you.
**Alex Boten** 16:32 And then, you know, very quickly exit out of the init if you don't have that environment variable.
**Tyler Yahn** 16:36 Yeah, yeah, exactly, yeah.
So, yeah, I think at the…
**Alex Boten** 16:40 I like this a lot, actually. That makes everything simpler for both the implementation and the, I guess, end user in the short term.
**Tyler Yahn** 16:48 Yeah, and it isolates it a little bit easier, so it's not all over the place, but yeah.
Yeah.
**Alex Boten** 16:53 Yeah, and if we get feedback that this is so useful that it should be in the baseline SDK, then we can focus on that in a future version of us, so…
**Tyler Yahn** 17:01 Yeah, I agree. I think that's… that's fair.
But, yeah, I also, like… Now, having walked through it, I'd be skeptical to say, like, well, it'd be more useful if it was in the default, because then I could use the default function instead of the hotel conf function. It's like, I don't know if that's, like, really that helpful, but, maybe. Maybe users are really into that, so, yeah.
**Alex Boten** 17:21 Yep.
Yeah, cool. Thank you.
**Tyler Yahn** 17:23 Yeah, yeah Hey, David.
I don't think we have much of an agenda, I was just looking. Yeah, Alex just joined, asking about, some hotel conf stuff, and so… yeah, Pretty light today.
**David Ashpole (dashpole)** 17:42 I spent all week on this frickin' exponential histogram thing.
**Tyler Yahn** 17:46 Oh, right.
**David Ashpole (dashpole)** 17:47 I'm so close, I just… there's one issue that I am trying to figure out how to work around.
**Tyler Yahn** 17:53 Oh, nice. Yeah, that's… that's impressive, yeah, I'm interested to… To see.
**David Ashpole (dashpole)** 17:58 It's The only disappointment is it's not… It's, like, faster, but it's not that much faster. I was hoping… It's like 150 nanoseconds.
I was hoping for closer to, like, 1, 120, like, the histogram, the fixed bucket histogram was, so I'm not sure what… What, what's making itself? Maybe just the calculation.
**Tyler Yahn** 18:23 Yeah, I mean, we're talking 30 nanoseconds, right?
**David Ashpole (dashpole)** 18:27 Yeah, I'll figure it out.
**Tyler Yahn** 18:28 Hopefully I can resolve this race condition.
**David Ashpole (dashpole)** 18:32 It's… It's one of those, like.
Something else is running concurrently and messing up my state.
I can't figure out what it is, so…
**Tyler Yahn** 18:42 Yeah.
**David Ashpole (dashpole)** 18:44 Like, another test is running, maybe? No, no, no, not another test.
**Tyler Yahn** 18:48 Okay.
I see.
Just another part of the SDK, yeah.
Yeah.
Fair enough.
Yeah, I think… I think I still am on the hook for reviewing the existing PRs for optimizations for the metrics pipeline, but… Yeah, I haven't… haven't followed through on that one. I was looking at the histogram one a little bit.
I'm just trying to think through it a little more, because it looks like it's just moving the lock from the top level down into, like, per bucket locks, right?
**David Ashpole (dashpole)** 19:22 There's no lock per bucket.
**Tyler Yahn** 19:26 Really?
**David Ashpole (dashpole)** 19:27 Yep. It's… it's using the hot-cold thing, right? So there's two different…
**Tyler Yahn** 19:32 For the exemplars?
**David Ashpole (dashpole)** 19:34 Oh, exemplars… oh, no, no, no, the… yeah, that one is trivial, like… Okay, just… Yeah.
**Tyler Yahn** 19:40 Yeah.
**David Ashpole (dashpole)** 19:42 I don't even remember it anymore. But I, yeah, I think it just moves the lock in one layer. It's very simple.
I thought you were.
**Tyler Yahn** 19:48 No, yeah, the other… no, yeah, the other one is… yeah, right, yeah, yeah.
**David Ashpole (dashpole)** 19:53 Yep.
**Tyler Yahn** 19:55 Yeah, again, it's Heaven.
Haven't timed yet for that one.
Well, cool. Any other topics y'all wanted to talk about?
**David Ashpole (dashpole)** 20:07 Okay.
**Tyler Yahn** 20:08 Well, cool, we can probably end it here. Thanks for all for joining. I'll see y'all next week.
**Alex Boten** 20:14 Yeah, thank you.
