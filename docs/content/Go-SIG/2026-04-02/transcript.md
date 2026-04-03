SIG: Go SIG
Date: 2026-04-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 01:08 Hey.
**Damien Mathieu** 01:14 Hey, good evening!
**Tyler** 01:26 How y'all doin'?
**Damien Mathieu** 01:31 Good.
**Tyler** 01:34 Nice. I'm looking at the agenda, I don't… I don't think David's gonna make it, I think he might have copied in the notes in thinking it was a 10 AM?
Here in our time?
meeting… I'm looking… sorry, I'm looking at the Slack, see if there's something there. I know Robert's not going to be able to make it today.
Hmm.
Okay… Yeah, I don't see… I don't see anything. Okay, well, he has David as two of the first two items.
We could probably just jump in, maybe just take a look at them really quick, and then, yeah, I did wanna… Ask about the next release as well.
Cool, I'll start sharing my screen here in just a second.
Okay.
Let's jump in here. So… David wanted to discuss how timeouts are applied when batching. This is, I think, something coming from the specification we were talking, I think, maybe… At a higher level here, but Experimentally go… There's David.
Actually.
Hey, perfect.
Hey, we were wondering if you, thought it was a 10 a.m. call today, but yeah.
**David Ashpole (dashpole)** 03:48 Okay. No, just… Just always running late.
**Tyler** 03:53 No worries.
**David Ashpole (dashpole)** 03:53 Cool.
So I… I know this is a big PR, so I don't, blame anyone for not having, looked at it yet. The one thing I wanted to discuss, maybe in person, is the changes to, how timeout handling works.
So… to give a summary of the feature, right now.
metrics collection. We'll collect metrics from the SDK.
And then we'll call… we'll form a batch of metrics, right? And then… Calls export on that batch.
and returns the error if there's an error, right? So it's, It's just a single batch. And one of the features I'm trying to add that's now experimental in the spec, is being able to split that up into batches of… with a max size. So, you know, I want X number of metric data points per batch.
And I can send those in smaller batches if I want.
the… the one tricky bit is that right now, our… The way we apply the export timeout.
Is that we apply it to collect.
and to export together. So at the beginning of our… reader loop.
We set the timeout on the context, so if you said 10 seconds, we set a 10-second timeout. We pass that context to collect.
And then… we… once collect returns, we pass the same timeout, or we pass the same context to the exporter. So, if the total collect… And export time exceeds your, like, 10-second timeout, then it'll trigger a timeout.
This gets weird.
When we want to have multiple export calls, Because… I'd like to be able to apply the timeout separately to each export call.
And so then the question is, well, what do we do with collect?
So, options potentially are that Collect, and the first export call, share a timeout, and then it gets reset after each one.
Or we can have what I've done here is that collect Has the timeout applied to it separately from each of the export calls?
But I wanted to discuss and see if people, like, usually collect doesn't hit timeouts, you would hope.
But I wanted to see if there were thoughts on… Like, how we should handle that.
**Tyler** 06:32 Yeah, I mean, I think from a user's perspective, I don't, I don't think I'd prefer this.
Right? Because, like, as a user, I just want to, like, say, like, if something takes more than 2 minutes, just… that's the end of it, like, stop.
However you want to, like, parse that up.
that's fine, but I think they're more interested in, like, the global timeout?
**David Ashpole (dashpole)** 06:53 Okay, so you don't… you don't think we should be applying the timeout to each export call?
You think we should apply the timeout to the total… Like… Collect.
**Tyler** 07:04 Yeah.
**David Ashpole (dashpole)** 07:04 Actually, okay.
**Tyler** 07:05 Yeah, because, like, as a user, if I'm… if I'm exporting this, and I say, like, hey, give me, like, a 2-minute timeout, and then, like, it times out after, like, 6 minutes, because, like, there's, you know, 10 export calls, and they all get their own 2-minute timer.
I'd be a little bit confused why that was the case.
**David Ashpole (dashpole)** 07:21 Okay, that… the way I… the reason why I had implemented it this way.
Is this is how the collector's timeouts work?
Which is that, like, you set a timeout. The collector's doing a whole bunch of, like, stuff in parallel, and it has workers and stuff like that, so maybe it makes more sense. Like, it's… it's just handling a stream of data, so it's hard to say, like.
There's no, like, single global operation that you could, like, point to?
**Tyler** 07:53 Is there a state where we add a new option for, like, export timeout as well?
**David Ashpole (dashpole)** 07:59 So, export timeout is already a… Option.
I think that's part of the problem. It's like, there's no… Currently, there's, like, a timeout that says the timeout for… that's applied to an export call.
So…
**Tyler** 08:16 And then, is there not an option that, is for collect data?
**David Ashpole (dashpole)** 08:21 Collect has… the spec for Collect doesn't have anything about timeouts.
the timeout is, at least according to the specification, is just for export. But… I think, like, the thing we've done here is better.
Like, I think applying it came out to collect is good.
**Tyler** 08:43 Yeah, yeah, yeah, I agree.
Hmm… I think I might… Yeah, I might actually… reverse what I just said, then, based on this documentation.
what I'm reading here, like, I, like… Yeah, I mean, we're pretty explicit about this as, like, the timeout for an export, so, like, applying it to each one of those exports seems… seems applicable to me now.
But I do think that, like, from an end user's perspective, like, maybe we've… we're… Maybe our configuration is just missing.
Missing the mark here, I guess.
Yeah, I mean, I guess, actually… 30 seconds is used, yeah.
Yeah, I don't know, I think we're pretty explicit about this being an export timeout, right? So then I think that, like, as long as…
**David Ashpole (dashpole)** 09:48 I think this language comes from the spec, right? So the…
**Tyler** 09:51 Oh, does it?
**David Ashpole (dashpole)** 09:52 Like, the spec says… the option is actually, I think, supposed to be called, like, with export timeout.
But, like.
**Tyler** 10:05 Yeah, I mean, Yeah, I think… I think maybe… I think this is pretty clear as to, like, what it is, and, like, what you've done is probably the correct solution then, based on… based on my understanding of this as well.
I think that my… issues more at the spec level than I think, at our implementation level. I think… I think based on what the spec has said and what you've done here, this is the correct approach, yeah.
**David Ashpole (dashpole)** 10:31 Okay, I don't remember anymore. Can you look at Periodic Reader? I think I tried to preserve? No, I didn't.
No, I just deleted it. So… If people want, while this is experimental, I can try and preserve the existing behavior when the feature is not enabled. Like, I… I can keep the… With timeout cause thing that has collect and export timeout?
Or I can make the switch now.
It's just up to… and we can do that later, if and when this feature stabilizes.
**Tyler** 11:08 Yeah, I think leaving the existing behavior for now, and then when it stabilizes, just reverting that, if that makes sense.
**David Ashpole (dashpole)** 11:15 Okay.
**Tyler** 11:16 Yeah.
But this, yeah, I mean, otherwise, I think this looks… this looks great, yeah.
How hard was this part?
Yeah, that's about right.
Okay.
**David Ashpole (dashpole)** 11:31 doesn't… it wasn't that hard. It… it was hard to make it readable.
Like, the first pass had a single function, because you get into weird scenarios where you're, like, halfway through A scope metric, and halfway through.
A set of metric data points, and you need to do a split, and so there's no… I don't actually think this is… particularly efficient.
But it is readable.
Like, having, split X, split Y, split Z.
So, and it's on the collection path, so I don't think it's as big of a deal.
**Tyler** 12:10 Yeah, that was kind of my take as well, it's Collection Path, right? So… Yeah. Yeah. Yeah, I agree. Okay.
Yeah, I totally missed this PR, sorry, I haven't taken a look at it yet, though, but, like, this seems reasonable to me, Yeah, I think this looks great. Thanks for putting this together.
**David Ashpole (dashpole)** 12:29 Yeah, well, I will admit to needing this very badly for customers, so… Oh.
Yeah, it's one of those.
**Tyler** 12:37 It's a great motivator. Yeah.
Yeah.
Okay, cool.
If you want, we can move on to the next PR, David, unless you wanted to talk a little more about this.
**David Ashpole (dashpole)** 12:49 Nope, that's good.
**Tyler** 12:50 Okay, cool.
Next up is experimental options.
This is a… this has to do with, like, the… the metric options, right, that we talked about prior.
**David Ashpole (dashpole)** 13:00 yeah, yeah, so I… I… Right… right now, I think our guidance… or… so I have a second PR that maybe people haven't seen yet, but it basically just takes the previous discussions that we'd had and puts it in contributing.
it doesn't… make this change.
Yeah, so we had talked about this, we had gotten some agreement with, how we were going to do enabled, right, because that was the big question at the time.
And we kind of punted on most of the other… Things, and said, yeah, like, do a feature branch.
And now, of course, I have a concrete case where I would like to be able to define an option outside of the package.
And feature branches… wouldn't really work, right? Because we can't have hotel gRPC depending on a feature branch.
So, I started looking for alternatives, and this, to me seemed like potentially the least bad one.
So… Yeah, we can look at it. If the answer is no, that's okay.
Yeah, so if you look at X.go here.
And actually, I realized that this shouldn't be inside of metric, internal X, this should just be in internal slash X, because we can define this once for the entire repository, and then use it whenever we need it.
So essentially, this… This would just be an indicator that we could use, but no one else can use, because it's in an internal directory.
That an option is defined outside of a package.
And so… we can change all of our APIs that accept options.
To check if it's one of these experimental options and ignore it if it is.
And that basically… Let's you define an option outside of a stable package.
You embed this experimental option type on it.
And then users that use it Users are able to use it.
and SDKs that want to be able to support the experimental option.
Are able to… are able to consume it without it being part of the stable API.
**Tyler** 15:29 So… Why do you need this to be supported by multiple SDKs?
**David Ashpole (dashpole)** 15:34 I don't need it to be supported by multiple SDKs.
**Tyler** 15:36 Right, you just need it to be supported by, like, the default one, right?
**David Ashpole (dashpole)** 15:45 When you say it, do you mean the, the, like, default attributes thing?
**Tyler** 15:51 Yeah, yeah.
**David Ashpole (dashpole)** 15:53 No, I don't need it to be supported by multiple SDKs.
Yeah, so if you look at the full thing, maybe this will be more…
**Tyler** 16:00 Yeah.
**David Ashpole (dashpole)** 16:01 Like, it kind of illustrate it better.
**Tyler** 16:03 It's kind of hard to… but I… yeah, I was taking a look at this.
**David Ashpole (dashpole)** 16:08 It's massive.
**Tyler** 16:12 Yeah.
**David Ashpole (dashpole)** 16:13 That is, yup.
So what you end up doing is, like, I can define this… With default attributes option.
And it is an instrument option.
And if somebody uses it, And, like, let's say… the LightStep SDK or something.
receives this option.
And calls the… stable, new instrument option, or, like, new N64 config function on it, it won't panic, right? So that's the important part, is that… Like, it won't panic if someone uses this with The existing option builders.
But then, If you're… if you're our SDK, and you receive this option in your list of options.
You can just iterate over the options, and look for it, and do whatever you want with it.
And I've… Does that make… Are people following?
**Tyler** 17:17 I think I see… I think I see the problem.
So the issue I was wondering about is, like, why couldn't you just put this in, like, the SDK? This, like, X option pattern here? Or, like, this experimental option pattern?
And then… and then have it work there, but the problem is, is then if, like, so… if gRPC like, instrumentation uses this option, and then some other SDK backs it, it's gonna panic, because it's actually gonna call, like, the… the… okay.
**David Ashpole (dashpole)** 17:47 Yeah, cause it's gonna call the apply… It's gonna call the apply function, and it won't… we can't implement that, because we've embedded it here. So this is a way for… this is sort of a way for us to… only for our experimental options.
un-make private the instrument option interface, right? Because we've, like, we've sealed the instrument option interfaces.
So this is a way for us to selectively unseal them.
For our own, needs.
**Tyler** 18:24 Yeah, I mean, I'm just… I'm super hesitant about… these, like, cross-module internal dependencies, because, like, it's, like.
it's de facto, like you point out, it's, like, de facto stable by default, right? And, like, any… Any change to that package, like, as an import, can just break transitive dependencies, yeah.
Yeah.
I don't know…
**David Ashpole (dashpole)** 18:59 And you're… Sorry, go ahead. This is the only way I found. The idea would be that we would define this, and that we would just never touch it, and treat it as stable.
**Tyler** 19:09 Yeah.
**David Ashpole (dashpole)** 19:10 And we would only have to do it once.
But…
**Tyler** 19:14 Well, yeah, I mean, like, it can never actually be removed either, is the other thing.
Yeah.
**David Ashpole (dashpole)** 19:20 So we would have to keep it around. It wouldn't be visible to users or anything.
We would have to keep it around, and we would use it for all future Experimental options that we want to introduce.
**Tyler** 19:31 So what you're saying is, like, we could also, if we put this at, like, the top level, not in the metrics package, but in just, like, the internal, then this could also be used in traces in other places as well?
**David Ashpole (dashpole)** 19:40 Yep, so we can use this as a way to tell all of our Config builders that they… Should ignore an option, or that they should, yeah, that they should ignore an option.
**Tyler** 19:55 I feel like we already kind of have a cross-module internal dependency, don't we? I think there is one in the internal with, like, the, the aerial handler stuff.
If I remember… I don't know. I think that actually might already exist, so this might actually already have some prior art, if I remember correctly.
**David Ashpole (dashpole)** 20:14 I mean, yeah, there are two exceptions listed in the contributing guide, I don't.
**Tyler** 20:18 Oh, there are.
**David Ashpole (dashpole)** 20:19 Right.
**Tyler** 20:20 Okay.
**David Ashpole (dashpole)** 20:21 But, but… That's not to say, like… I think the important… It… there's nothing worse, I suppose, about putting it in an internal directory versus putting it in the main metrics package. It's just that I think it's non-obvious to people who are working in internal directories that something Is actually stable in the internal directory, because of.
**Tyler** 20:43 Well…
**David Ashpole (dashpole)** 20:44 Across multiple dependencies, right?
**Tyler** 20:46 Yeah. Can I ask kind of a dumb question, though? Like…
**David Ashpole (dashpole)** 20:49 Yeah, yeah.
**Tyler** 20:50 Why… Why, like, hide this?
**David Ashpole (dashpole)** 20:55 So I thought about that.
**Tyler** 20:57 Yeah.
**David Ashpole (dashpole)** 20:58 And… my… so at first, I had it as part of the public package.
Because it was, like… Well, I thought that that would… I thought that that would make the cross-module dependencies better, and it… I suppose it does. The main thing is, like.
Then, in theory, someone else outside of the repo can define an experimental option.
And use it with their own SDK, which… Seems potentially useful.
The only reason I came up with was, like.
It then becomes part of the package definition for the metrics package, and we already have a bunch of stuff in there that's not really user-facing, like all the config builders.
**Tyler** 21:42 But, like, there's actually… so, there's nothing stopping us from switching this method to be, you know, public.
and then maybe not even, like, defining… like, I mean, we could define this here in the code, but, like, you don't actually have to export this, this option, or this interface, right? You could just say, like.
hey, if your option implements something that's, like, has an experimental thing, we're literally gonna ignore it here, and we assume that you're gonna, like, parse this, like, in your SDK.
Like, we don't have to actually export the interface, right? We could just say, like…
**David Ashpole (dashpole)** 22:18 Wait, wait, you just need to have a function, and then we'll assert on it.
I think that would work as… I think that would work as well, and then there's no explicit… Dependency between anything, because it's all implicitly implemented, right?
**Tyler** 22:29 Yeah, yeah, yeah.
**David Ashpole (dashpole)** 22:32 Okay, I, I think…
**Tyler** 22:33 And then, it would also allow, like, other SDKs to start, you know.
you know, obviously, I think we probably want to document this a little further, because… From an SDK perspective, you shouldn't, like, rely on, like, you know, return values from this. You should have, like, this interface to say, like, don't ignore it, but then another, like, private method that you're gonna, like, actually parse or something like that, right?
**David Ashpole (dashpole)** 22:56 Right, right, so you need to… the main thing is, you know, you need two things. You need the actual API not to panic, and then you need the SDK to… Do some type assertion, and interpret it, yeah.
**Tyler** 23:08 Yeah.
So I… I mean, I think… I think if you do that, like, it would… not only avoid this linking, but it would also allow other SDKs to try to, like, play around with their own experimental issues, or, you know, whatever they want to do there. So, that might be actually even more beneficial.
**David Ashpole (dashpole)** 23:25 Okay, you want to just drop a comment, and I will make that update.
**Tyler** 23:31 Yeah, I can… I can do that.
I can do that after the meeting, too, though. I don't need to…
**David Ashpole (dashpole)** 23:36 Okay.
**Tyler** 23:37 Subject you all to me thinking out loud.
But yeah, I think, I think if that makes sense, like, I think if that… Yeah.
Think through it again, as well.
Any other thing you want to talk about on that one, David?
**David Ashpole (dashpole)** 23:53 No, just, yeah, then, that sounds good. I would love to be able to support more experimental stuff.
**Tyler** 24:00 Yeah, I think that actually kind of… is the best of situations, instead of, like, it would just really unblock a lot of experiment. Like, it's even then, like, if you wanted to, like, experiment in your own… you know, SDK on that, like, isn't even in the main reap one, you can really start to, like, show, like, proof of concepts there on, like, how you can use option patterns, yeah.
Okay.
Cool. Next up, is the next release. Damien, I saw that you opened a,
**Damien Mathieu** 24:27 request for this? Yes.
Mostly, like, one of the reasons is that there is a, security issue, maybe two, actually, that needs to be fixed, so, it's fair. Oh, I missed that the CI is failing, I don't know why, it may be just, like, cut coverage.
Links, so that's, expected.
Yes, so… unless there are blockers or anything, I will be doing it tomorrow, provided I get a signal in approval.
**Tyler** 25:00 Yeah, I think your second approval's gonna come in just a few seconds here. Yeah, I think that was my only question to you, is if you can coordinate this release, with the contrib as well, like, if you had time. But if you're gonna wait till tomorrow, then that.
**Damien Mathieu** 25:14 Yes, I mean, I won't be doing it today, but yes, I'll be doing it tomorrow with Conchip.
**Tyler** 25:22 Cool, alright, yeah, then let's… let's plan on doing that.
I will look for your PR in the morning on Contrip, and we'll try to get this out.
Okay.
**Damien Mathieu** 25:33 I mean, if I'm stuck on contribute, I'll ping Robert and merge it with SQL approval, I guess.
**Tyler** 25:40 Yeah, that, yeah, he should be, he should be active then.
There aren't any breaking changes that we need to address, right?
**Damien Mathieu** 25:48 Don't think so… no, no, sorry, between core and contrast, no, they're not.
**Tyler** 25:54 Okay.
Cool, alright, yeah, that sounds good.
Okay, cool, I'm gonna stop sharing my screen.
Any other topics folks had that wanted to talk about that aren't on the agenda?
**Damien Mathieu** 26:11 Just a reminder that, not really, really any day now, but, in, like, a month or before, I will be off until September.
**Tyler** 26:24 Oh, yeah.
Yeah, good point, yep. Thanks for bringing that up.
**David Ashpole (dashpole)** 26:27 Yep.
We'll miss you.
**Tyler** 26:33 Yeah.
Also, we should probably make sure that we codify that whole thing about, like, the owner or the author of the PR is counted as a separate company, again, because that was awkward last time.
**David Ashpole (dashpole)** 26:44 It is codified. It is.
**Tyler** 26:46 Okay, then, cool, alright, we're good.
**David Ashpole (dashpole)** 26:48 Rechecked, yep.
**Tyler** 26:49 Yeah.
Cool, alright.
If there's nothing else people want to talk about, we can end the meeting early here. It's good seeing y'all.
Thank you all for all the hard work, and yeah, we'll keep it going.
Okay, bye everyone.
**David Ashpole (dashpole)** 27:06 Bye, everyone.
