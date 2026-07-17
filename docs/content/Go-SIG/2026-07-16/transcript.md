SIG: Go SIG
Date: 2026-07-16
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:29 Hey, Brian.
**Bryan Boreham** 00:31 I don't know.
**Tyler** 00:34 How's it going.
**Bryan Boreham** 00:37 Yeah, pretty good. Pretty good. Okay.
You.
**Tyler** 00:42 Yeah, same, same.
Just just chugging along.
A lot of stuff to do, but… Getting there.
Any big events going on at Grafana these days?
**Bryan Boreham** 01:04 Oh, we… We have a whole company offsite in Vienna, in The end of August. So it's not 6 weeks.
**Tyler** 01:14 Yeah, something like that, right? Yeah Yeah, I was, talking with some of your colleagues, and they were… I think they were mentioning something like that. I didn't know it's always fun to get a lot of people together like that, like, just get in person. Obviously, it costs a lot, but, I mean, I don't know, I think there's a lot of value in it sometimes, like, doing it, yeah.
**Bryan Boreham** 01:37 Yes.
Our CFO was nicknamed Inferno.
**Tyler** 01:45 I hope that's for his ability to spend cash instead of his temper. But yeah.
**Bryan Boreham** 01:52 Or at least by, bye, Raj, the CEO.
**Tyler** 01:56 Yeah, yeah, yeah.
That's pretty good.
That's pretty good.
Well, cool.
Yeah, I see, Robert and, Israel is also joining, Looking at the meeting notes, we don't have anything actually on the agenda, so we can… hang out here. If you did have something you wanted to talk about, happy to discuss that. I know David's not gonna be able to make it today, so it's gonna be a little bit lighter, But yeah, if you had some topics, I'd love to talk with them.
Yeah, if not, we, we don't have to belabor the point, that's also, that's also fair. I know there's a bunch of PRs that we're looking for reviews on, but obviously, like.
If you're… if you're interested, please take a look. I'm behind on a lot of these, so I think it's Getting to these reviews, so, yeah, I guess it's more just guilt bleeding through, but yeah, if folks… I guess also, if folks have something that is really, like, burning, if you wanted to ping us in, like, the Go channel and Slack as well, we could also… Take a look there. But yeah.
Cool, yeah, if there's… No other topics, where are we at? Oh, about 4 minutes in. Yeah, we could probably end the meeting, here.
Sorry to, not have a burning agenda, but that's also kind of good time, so, yeah.
Cool.
Alright, everyone, we'll see you all next time.
**Tyler** 04:45 Hey, what's.
**Puneet Singh** 04:46 Hey, Tyler, thanks for joining. Actually.
**Tyler** 04:49 Yeah, no worries.
**Puneet Singh** 04:51 So actually, I just wanted to discuss this meter configurator, if you… remember from… I think… Previous to previous meeting?
**Tyler** 05:04 The configurator, the hotel comp stuff?
**Puneet Singh** 05:07 Yeah, so, meter configurator is,
**Tyler** 05:13 Oh, meetings.
**Puneet Singh** 05:13 then…
**Tyler** 05:13 Oh, sorry. Oh, sorry. Yeah. Meter configure. Yeah. Got.
**Puneet Singh** 05:17 So, it basically takes instrumentation scope and produces a meter config, which is basically what is used… meter provider uses to enable or disable specific meter instances, right?
So I think one thing you mentioned that at some point it has to be integrated with the declarative config.
**Tyler** 05:42 Yeah, I think it is, I thought, but okay. But yeah, if it isn't, then yeah, sure.
**Puneet Singh** 05:48 Yeah, what I was thinking is that, Declarative config would be useful to initialize the meter configurator, but Not beyond that, because it seems like a kind of dynamic control.
Some sort of external, provider who is trying to alter the meter configs will use this functionality? Does that make sense?
**Tyler** 06:15 Yeah, it does. I mean, the other thing that like stands out though is that like this idea of Oh, no, never mind. I'm thinking something else.
No, I mean, yeah, I think that makes sense. I think that it would have to be an interface too, though, right? Or is this a static type? Are you envisioning?
**Puneet Singh** 06:34 I mean, let's… let's leave the implementation details, on the… on the side. I mean,
**Tyler** 06:44 Well, I just asked because, like, I wonder if it's something that, like, the default one doesn't support dynamic configuration, but, like, you could extend it to try to do that? I don't know… I don't know if the spec actually requires dynamic configuration on this, is my question.
**Puneet Singh** 07:00 I mean, there is no details in the spec, to, you know… it is an incomplete spec, I would say. Yeah.
**Tyler** 07:08 Sure.
**Puneet Singh** 07:08 Once, you know, my implementation kind of reached to a certain maturity, I started thinking about that, how it is going to be used actually. And the only thing that makes sense is that first is that meter provider is not going to decide, it's only going to act when the set configurator is called, which is to reevaluate that which meters have to be enabled or disabled.
So, it is very much a responsibility of external entity to decide that if a certain config has changed, and it has to call the set configurator to update the meters. That was… my thought on this. Okay. Now, this… there is this another proposal called Telemetry Policy from Josh Swarith, and, that is about updating the certain attributes of telemetry, but it seems more broader in the sense that it focuses on what flows through the telemetry. But the configurator is, like, more identity-oriented, like, disable certain meters based on the instrumentation scope.
**Tyler** 08:15 -H.
**Puneet Singh** 08:15 Where I see the overlap is how they are being delivered, which is dynamically, actually.
**Tyler** 08:22 Yeah, just for my clarification, like, are they expected to all be delivered, like, in code, or is this, like, an op-amp thing?
**Puneet Singh** 08:31 Yes, I'm glad you asked, actually. So, I mean, the policy thing is kind of… currently it is using OpAmp, from what I see. Yeah.
And in terms of config… when I started thinking about configurator, I mean, this external provider, which is going to watch some config and apply it, seems very much what the OpAmp agent would do, so…
**Tyler** 08:56 Yeah, I agree.
**Puneet Singh** 08:56 Even the responsibility doesn't match that, you know, something like policy will use OpAmp because it needs to apply certain policies cluster-wide. The… the idea of controlling it like, kind of feels similar to OpAmp, or, you know, something that is adjacent to OpAmp, which is file-based or HTTP-based providers. So, I just wanted to check, you know, if that makes sense, actually. So, me, rather than trying to imagine that what kind of this provider look like, You know, think in terms of what is already being present, actually, and why try to reinvent when you have already have, you know, mechanics to deliver such stuff.
**Tyler** 09:37 Yeah, I mean, I think that makes sense, right? Because otherwise, you're just going to reinvent it again, trying to… because, like, having dynamic configuration, if you're going to do that, that's great, but, like… how do you configure that dynamic configuration, right? So it's like, you need some sort of, like, communication protocol, like, which is what OpAmp is, so I think this policy thing is worth taking a look at. I do, Yeah, I mean, I think that makes sense to me.
**Puneet Singh** 10:02 Yeah, so what I'm thinking is that the current wire protocol that… or the data format that OpAmp has… So our pump doesn't care about what passes through. It passes the whole thing like a blob and compares a hash kind of thing to reconcile that hash actually. So I mean, I was just, I wanted to check if the idea makes sense and it is worth exploring to see if this can be, you know.
OPM or, you know, adjacent to OPM kind of a space can be explored for this.
**Tyler** 10:33 Yeah, I mean, I definitely think it looks interesting. Do you foresee this getting folded into the profiles or the telemetry policy thing, or do you think it'd be separate?
**Puneet Singh** 10:44 I think it will be separate, because in terms of the context or, you know, the scope that, So OpAmp doesn't care about what flows through, actually. But how it's… it gets triggered, that I haven't… haven't had a clear picture, actually, that, you know, how to different kind of… Configs flow through OptEmp, and how they synced on the different requirements, actually. So that is something worth exploring, but I just wanted to check if the idea makes sense.
**Tyler** 11:18 Yeah, I mean, I think it makes more sense.
since then without it, to be honest. Because, like, having the configurator with, like, this… like, having a static configurator on startup telling something is enabled or not enabled, like… Not that you…
**Puneet Singh** 11:31 That goes as a static config, right? I mean, I might use declarative config and just leave behind the configurator, I think. So the whole point is having such control so that you can disable the meters while not touching anything else actually. So. Yeah.
**Tyler** 11:45 Yeah, but even then, like, that, that, like, you could even achieve that with, like, a view, to be honest, to turn things on or off from the startup, right? So it's, like, it becomes a little bit less, like, obvious why you would need that.
But if you're talking about, like, dynamic configuration as you're going along, like, that's definitely not something you can do with a view. So, like, yeah, I do think that this is an interesting thing to pursue, and I would definitely want to include some sort of dynamic configuration, like what you're talking about, to motivate it. That sounds like a great idea.
**Puneet Singh** 12:14 Alright, alright. Okay, I'll keep, you know.
pursuing and see where it ends up, but thanks for the feedback on this. I think this was the…
**Tyler** 12:23 Yeah, yeah, that sounds good. Are there any other PRs you haven't contributed for resource providers that we need attention on?
**Puneet Singh** 12:29 Thanks on the feedback, by the way. The Docker was very interesting, actually, that I got to learn more about the image and text, and it's a nuance, actually. I think the only pending thing is the Docker one. I made changes with respect to what you… asked, but… but thanks for your patience, you know? It took, some… I… I couldn't foresee those things that, okay, this is also possible, and this… but… but yeah.
**Tyler** 12:53 Yeah, that one. You're not the first one to try to tackle this. That one's a complicated one. I'll take another look. Sorry. Yeah, I've got like a stack of reviews I'm supposed to be doing.
**Puneet Singh** 13:02 No, no issues. I think, I think you gave enough effort. I was like, yeah, I'll, I'll reach, you know, next week, we'll see how it goes.
**Tyler** 13:10 Okay, alright, cool. Yeah, sounds good.
**Puneet Singh** 13:12 Cool. All right. See you then.
**Tyler** 13:13 Okay, bye. Bye.
**Puneet Singh** 13:15 But yeah.
