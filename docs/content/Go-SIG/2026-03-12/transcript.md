SIG: Go SIG
Date: 2026-03-12
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Bryan Boreham** 00:22 Hmm.
**Pellared** 00:26 Hello, Brian.
**Bryan Boreham** 00:28 How you doing?
**Pellared** 00:32 Luz, how about you?
**Bryan Boreham** 00:35 Yeah, I'm okay. There's too much going on.
**Pellared** 00:40 Yeah.
I have commented on one of your PRs.
I'm not sure if you saw the notification, I guess you have plenty of them.
Regarding, what… regarding adding string methods to the attribute key values.
**Bryan Boreham** 00:56 Yeah, I haven't… I know… saw it go by, I haven't caught up with that.
Thank you for, taking a look.
Still have no idea where that is.
**Pellared** 01:12 I can send you a hyperlink later, if you want on Slack.
unless you want to discuss it now, I'm not sure.
Maybe we can do it. I will find you to add to the agenda.
Hello?
**Tyler** 01:56 Cool, alright, so… Looking at the agenda, we're still getting it figured out. If you haven't yet, go ahead and add your name to the attendees list.
And if you have other topics you wanted to talk about, please go ahead and add them there. I don't think Damien's joining us today, it's the later meeting, so we could probably get started here.
start sharing my screen Cool.
So first up, Sunal, you wanted to talk about this PR in Contrib?
**Sonal Gaud** 02:41 Yes, yes. So, I wanted to take this up, so, like, I had a word with Robert, and it's like, this is going to be a difficult one, and we will have multiple proposals to it, so I just wanted to know the ideas from everyone, and, you know, so we could start working on it.
**Tyler** 03:01 Yeah, that sounds good. Robert, what are your thoughts on this?
**Pellared** 03:06 My initial thoughts, I was just… I haven't done a big analysis on it, but I just thought that the library concept… I remember we had an idea to propose it maybe even upstream, or things like maybe API or stuff like that, but then I realized that if you have some complex instrumentation.
and you have some, I don't know, function, which is then instrumented by many instrumentation libraries.
maybe even it can… it can even have the HTTP server, which then also has, like, HTTP client.
And, if you pass, if it will be a single labeler, then you do not have the granularity of selecting for each instrumentation you want to add, for instance, you know, attributes. So I think it's better To have the kind of laborer concept, for each instrumentation.
Not sure if library instrument… probably for instrumentation library will be good enough.
And, yeah, even for the sake of total HTTP, I think it should be a separate thing for server and client, for the reasons I just said before. And, I'm also not sure if we even need the Labor… the label… labeler type, if we just do not just need functions that operate on… on the context.
But yeah, these are just… yeah, these are all just my ideas after, like, one hour of thinking about it.
And I miss Damien here.
During school.
Those are a few thoughts?
So now, did you have a chance to discuss it with Damien?
**Sonal Gaud** 04:49 Yeah, I asked him, and he had the same idea of having labeler for different instrumentations.
**But he didn't briefly say it, so I told him that we will discuss in the meet, but, he didn't join, so… Pellared** 05:06 Missy.
**Tyler** 05:09 Yeah, well, let's see if we can ping him here.
Yeah, I mean, I think that all sounds good. I think I'd like to get Damien's, input on it as well, but yeah, I think that makes sense. So, Sanal, if you don't get any response from this.
Maybe in, like, a few days? I think maybe it's just time to start working on a prototype, to address it.
**Sonal Gaud** 05:41 Makes sense.
**Tyler** 05:42 Yeah, okay.
Well, cool, alright.
Okay, anything else on this one, or are we okay to move on?
Okay, moving on.
I don't know how this ended up here, but okay, so next up, I've got, a new prototype. This is something that's… Starting, in the specification.
There's a… yeah, this is definitely some work to be done. So, in the specification, there's an idea to… for a long time, to have this remove, or finish, or stop, recording.
And unregister things from synchronous instruments to prevent memory… excess memory usage.
It's taken up by, Antoine, he started working on a PR for this. I know David's also been actively working with this one and a few other people, so one of the things is prototyping this in particular languages.
I'm pretty motivated for this one, just kind of background on this one for maybe, like, motivating the use cases. I think that there's a lot of users, we've definitely had a lot of users commenting on this issue, but then also, like, OB itself actually already, does this, by… dirty things where it actually just implements its own API and then shims in our SDK. So it'd be really nice if we could just have our SDK there, and then we wouldn't have to do a lot of that, like, shimming, in other OpenTelemetry projects that already require this. So, yeah, moving forward with this one, I think it's pretty, pretty important. So, I tried updating, Antoine's original.
Proof of concept for this… small tweaks, mostly just, merging in main and that kind of thing. There's a few things I wanted to maybe just, run by here in the meeting with folks. Not necessarily the SDK implementation.
I don't actually… this is probably not… ready, for evaluation too much. There's… there's definitely details in, like, the histograms, or I'm sorry, the, exemplars that probably need some, looks, but one of the things is, like.
So maybe at a high level, so all the synchronous instruments get this new method, this new method is, finish, which is defined in the specification. It takes these finish options, these finish options are kind of like the… the point of discussion here, so the finish option is really just accepting attributes, so, you know, attribute sets or attribute, slices, depending on your flavor of, wanting to do this.
It has its own config. It doesn't use the measurement option, because that would, potentially have conflicts if you wanted to add new things to the measurement option.
that… Providing them to finish wouldn't make any sense, so this adds a new option type.
The, the kind of the big issue becomes.
This option thing returns a measurement option right now, Yeah, and so, this changes the function signature to return an attribute set option, and I'm not 100% sure on that. Obviously, like, the attribute set option is embedding the measurement option, so, like, there's no, Features that are not going to be there.
however, like, it's, it is a new type explicitly, so I'm not exactly sure about the backwards compatibility of this, so still evaluating that, just got this together, not really… Fully fleshed out, so just kind of a heads up on that one. It may be that, like, we don't return this as an attribute set option, just keep returning it as a measurement option.
And it's just gonna be confusing to users, because technically it'll implement also the finish option, so you can go use it there, it's just our docs. We'll have to… be, you know, using English to say this, rather than the syntax of the API to say this. If we don't go this direction, if we are able to go this direction, I haven't fully evaluated, but, you know, just kind of a heads up on that one.
But yeah, I mean, that's kind of the long and short of it. The SDK implementation, obviously, like, you gotta make this work, which is still something to work on, but it's more about, I think, the API at this point, looking for a review.
for people on the POC, I would say you can take a look at the SDK if you really want, but it's, yeah, still something I'm working on.
**David Ashpole (dashpole)** 09:52 I don't remember the latest proposal for how it was gonna work. Can you pass in… Like, a single attribute?
And it will match all the things that has that, and then match all the series as well that don't have that, or do you have to pass in the… Exact attribute that you want.
Like, so for example, a common thing would be, like, I'm monitoring a container.
And I've got 20 instruments associated with that container, and I'd like to go through all the instruments and delete all the series.
that have that container name or something, right? Like… I think… or I guess maybe this is still active in the… the… I wonder if OBI has similar needs as well, where you don't want to have to go through and find every specific attribute set that you've ever offered.
To go delete it with something, right?
**Tyler** 10:42 Yeah, no, OBI does exactly what this is saying, where it's, like, an exact list.
Yeah.
**David Ashpole (dashpole)** 10:53 Do you have to maintain that, or… Tyler 10:55 Yeah, I mean… Is that something you happen to have?
Yeah, we have it pretty easily. It's like, it's stored in a map, because essentially, like, we need some sort of identifier to, like, yeah, like, essentially return… we don't keep instruments, we keep, like.
I mean, we do keep instruments, but we keep a separate map, essentially, of all the attributes that come in in OBI, or… now you got me saying it.
It's an acronym, not initialism. Anyways, like, yeah, so, like, that isn't a big deal, but I think what you're saying is, yeah, I mean, I think that that's a great suggestion, like, having something like that.
I think that that's worth maybe, like, investigating a little bit here, in this, POC. Yeah, because, like, if you could do, like, some sort of, like, finish option that has, like, some sort of, like.
filtering, like, either an allow list or a deny list, or something like that, like, I think that would be very useful to users in processing, so, yeah.
**David Ashpole (dashpole)** 11:49 Anyways, yeah, I was curious if… I'm more curious from, like, the OBI perspective what you want than anything about this POC specifically.
**Tyler** 11:59 Yeah, this, like, honestly, like, our, Shoehorns, API pretty much has this exact signature, just without the context, because we don't pass the context through, but, like… Yeah, it's just a… in fact, I think it's actually not even an option, obviously, it's just, like, a slice of attributes that we pass through. We can take a look, actually, if you want, but, yeah, it's very… it's very bare bones, because, like, we know exactly what we want, but we just sort of, like, stop registering this, and we'll just pass it through, yeah.
But I think from outside perspectives, that may not always be the case. I think that, like, you have provided a good example with, like, the cloud provider stuff.
**David Ashpole (dashpole)** 12:38 And then, the only thing I noticed skimming the implementation, I know you said don't look at the SDK, but sorry, I did.
No, so it's fine. I think probably what we'll want to do is, like, when we get a finish.
We'll want to just mark the series as having been finished.
**Tyler** 12:54 Yeah. And then export the points.
**David Ashpole (dashpole)** 12:57 Rather than just… Like… deleting the stuff we've got associated with it. Or, like, we still need to get the data out once we've finished something. It needs to not, like… continue into the next cycle. Then we have to figure out how we're gonna handle, like, someone finishes something and then immediately re-observes a new thing. Right.
**Tyler** 13:18 Essentially, like, tombstoning and, like, figuring… yeah, I was kind of thinking.
**David Ashpole (dashpole)** 13:21 I think that's… yeah, that'll be interesting to see how that looks. And I think he'll… I think maybe it would be helpful to… one topic I didn't put on the agenda, but we could discuss here is, I added the new developmental, start time.
A cumulative start time tracking spec.
Do we want to make that change, and put it behind a feature gate, and then use it here? Because I assume this won't work properly unless we have Start time.
You can still implement the prototype, probably, but it'll have bizarre start times.
**When you finish in the… Tyler** 13:57 Exactly.
**David Ashpole (dashpole)** 13:57 Thank you.
**Tyler** 13:59 Okay. Yeah.
**David Ashpole (dashpole)** 14:02 Behind a feature gate, then.
**Tyler** 14:04 I kind of like that idea, yeah, if you wanted to go ahead and implement that, I would be up for doing that.
**David Ashpole (dashpole)** 14:09 I don't know how the feature gate.
**Tyler** 14:13 I mean, it's just an environment variable that we could set and says, like, okay, yeah, okay, yeah, yeah.
**David Ashpole (dashpole)** 14:28 Yeah, I'm super excited. Thank you for your help on this. I also have wanted this for a long time.
Cuz… anything that Prometheus can do really well that we can't do at all, is, like, a thorn in my side that I get annoyed by.
**Tyler** 14:43 Yeah, that's a good point. I think you were the original author of, like, this is not working for me. So, yeah, okay.
Cool. Yeah, any other feedback, David, please keep it coming on this. I think these are great suggestions, so, I'll… I will keep iterating on it as well, and any other feedback from other users as well, please… please just comment in this PR, and we'll just keep updating. Yeah, I may be a little slow on this, it's not my top priority, but I will try to keep going on this, so, yeah.
**David Ashpole (dashpole)** 15:10 Cool.
**Tyler** 15:12 Okay, Moving on, Robert, discuss What's Up Hotel quoting, I don't need to speak for you. Go ahead.
**Pellared** 15:22 No. You were doing a very good job.
Yeah, so, so there was no Slack message, I think it was from the end users, if I remember correctly, about having some podcasts, and they want to have some some, I don't know, monthly or bi-weekly, I do not remember, like, updates from, like, I don't know, interview or update from the 6, and I just wanted to ask you if, yeah, every month.
So I just want to ask you if… any of you want to volunteer. Personally.
if I'll be there, I'll need someone to help me, because it's pretty late.
And I'll be extremely stressed, and I'm pretty sure that I will be even having problems understanding any questions that will come up.
**Tyler** 16:15 Yeah, sorry, I think I saw this. I was having an issue opening Slack from links.
So it looks like a form, and we fill out the form just to say, like, we're interested?
**Pellared** 16:28 Yep.
**Tyler** 16:31 Oof.
**Pellared** 16:33 I think, like, I remember our, GC liaison recently also asked us what we are doing.
And I also said, like, David, like, the stuff you proposed, and I thought that maybe there's something worth sharing. What do you think, David?
**David Ashpole (dashpole)** 16:50 I can share it. It feels like… I mean, it's still on our 2026 plan, so there's a part of me that's always like, yeah, I'll just wait for, like, one more thing to land.
And then I can mark it done. But I might… I might be waiting for this podcast for 3 years, then.
**Pellared** 17:06 Yes.
**David Ashpole (dashpole)** 17:08 So, I… Yeah, I mean… You can put me in, or like, I don't know if you want to start a chat or something. Where did they reach out?
**Tyler** 17:17 So it's in that form, that Robert has linked, in the doc, and then you just fill out the form for, I think, your… David Ashpole (dashpole) 17:25 And this isn't associated with, like, a company or something, this is, like, OTEL is doing a podcast.
**Tyler** 17:31 I think this is, yeah, Reese and, I can't remember the other community liaison, role.
**David Ashpole (dashpole)** 17:36 Folks, yeah, they're the ones that are setting this up, if I remember. As long as it's, like, not… Not some random vendor, yeah.
**Tyler** 17:46 Yeah.
Yeah.
Somebody… yeah. Wouldn't be the first time. Anyways, Yeah, no, I think that's great. I think also, like, any other things that we have, like major milestones or accomplishments like that, I think that'd be awesome to continue to do this.
**But do you think, there's a lot of other… David Ashpole (dashpole)** 18:08 When logs graduates, you're gonna.
**Tyler** 18:09 Yeah, that's what I was thinking, too.
I expect Robert to be the showcase of logs going forward, yeah.
Yeah, I think that… I think there's other works in other SIGs as well we could try to popularize on this one. I think also stabilization of, you know, hotel HTTP or other things would be great to get people talking about that as well, just to kind of talk about the instrumentation. So, maybe this is something for Damien as well, we could ping, Damien there.
Cool.
Okay, I can start sharing my screen again. Next, we want to talk about the… adding the string method to the key value and value, if I remember correctly. Pr, this is something that's being sprung on Brian, but… It's something Robert and I are really passionate about as well, so I'm super excited to talk about this one.
**Pellared** 19:05 Yeah, I saw that also David, like, kind of thumbs up… gave a thumbs up for the proposal to use this string method and make it compliant with the specification. So, probably just to… probably… I think everyone is on board.
It's just about, you know, kind of… saying that I can probably work on it after KubeCon.
**David Ashpole (dashpole)** 19:28 Did… did that spec go stable? Not that it should block this, but… Pellared 19:33 I think it is, but that's a good question. I'm not sure if I can… have I put the hyperlink here?
**Tyler** 19:40 Yep. Yes, I think this is… David Ashpole (dashpole) 19:41 it, right? Yeah.
**Tyler** 19:45 Well, it's stable.
**David Ashpole (dashpole)** 19:46 3 months.
**Tyler** 19:49 Yeah, right. Yeah, I think it is that. This is stable, except otherwise… Except… Pellared 19:53 Try to find the experimental, or development.
**Tyler** 19:57 In development, yeah.
**Pellared** 19:59 Where is it?
**Tyler** 20:00 That's… David Ashpole (dashpole) 20:02 Just finding the… Pellared 20:02 No word.
**David Ashpole (dashpole)** 20:04 I think it might just be stable.
**Tyler** 20:07 Yeah, I think I'm… I think you're right, yeah.
**Pellared** 20:09 I think when I stabilized the stuff, I have forgotten to change this text.
These complex attributes.
**Tyler** 20:17 I don't… Yeah… Yeah, I mean, maybe that's a good question. I… I guess, I don't know. Maybe it just became de facto stable.
**David Ashpole (dashpole)** 20:32 Anyways, I don't think it's blocking for this. I was just curious. Thank you for looking.
**Tyler** 20:38 Yeah, I, yeah, I think that that makes sense.
**David Ashpole (dashpole)** 20:43 Yeah, I agree with your reasoning, Robert. I just… Didn't have the time at the time to… Look into it.
Does it still need… Approvals?
**Tyler** 20:55 I think.
**Pellared** 20:56 I think it is redesigned, because right now, it just reuses emitter.
**David Ashpole (dashpole)** 20:59 Oh, yeah, yeah, that's right.
Okay.
**Tyler** 21:02 Yep.
So time-wise, Brian, is this something that if Robert picks up after KubeCon, you'd be okay, or is that something you plan on picking up in the next month or two?
**Bryan Boreham** 21:12 Oh, well, yeah, I answered for March, because I'm… Yeah, I'm at, like, 4 different events in Amsterdam, and, 2 events next weekend, but if we… if we speak about… like, after KubeCon, yes, I might pick it up.
I… I don't know.
**Tyler** 21:40 Yeah, no pressure. Why don't I add it to a milestone, so that we don't lose track of it? I'm guessing 43 or 44, Robert, which one are you thinking?
**Pellared** 21:47 44.
Okay.
**Tyler** 21:49 Yeah, we'll do that. I think that gives us… Pellared 21:51 It doesn't… it's not… it should not block it in… Next race.
**Tyler** 21:56 Yeah, and then after the next release, we can reprioritize, and if you are still busy, Brian, we could try to find somebody else to pick this up. This is great, so yeah.
Okay, cool.
Next up, David, do you want to talk about update on metric SDK optimization, experimental histogram, or exponential histogram optimization for a small change?
**David Ashpole (dashpole)** 22:15 Oh yeah, yeah, I forgot to fill out the rest of it, but yeah, so I wanted to just… I've re… Restarted my effort to… We don't need to review this part of the PR now. I just wanted to describe what I'm doing so that people understand the plan.
And I, I will admit to… I'm dipping my toes now in the AI stuff, so please just ping me if anything is not… Not up to my usual standards. But I have implemented the whole thing.
I did it once by hand a few months ago, but it was… Not very clean, and it was one giant PR, and splitting it up was very difficult.
So I've, used AI to help me split it up into PRs, and to reduce the scope slightly.
And I also had it find gaps in the test coverage for concurrency tests, and helped me… expand those. So, I have two PRs out to improve the tests for like, concurrent stuff and aggregations, and actually it found some really interesting, One ways to test it, like running Observing the same numbers parallel and in serial and concurrently.
And checking the results, was one thing it does.
And also just expanding the inputs.
to cover more of the, actual code. So, I think those improvements are helpful, and will give me a little bit more confidence in it. The thing that it came up with is almost identical to the strategy that I was using, manually, so I do understand the changes and stuff like that, but again, please, please let me know if, if, I should stop using it, or, anything like that.
I'm just letting people know, as an act of transparency here.
And then… so that's that. There's 3 PRs out, you're welcome to review.
Let me know if you need me to split up or do anything else, if they're too large.
Then, for the other… for the attributes-related stuff, I think I'm still just waiting for one more review on the… Benchmark.
the, like, EDE benchmark PR. So if anyone has time… I thank you, Robert, for taking a look, but I think it needs one more approval.
That's it.
**Tyler** 24:40 Is this blocked on me, or is this looking for somebody outside of Splunk, David?
**David Ashpole (dashpole)** 24:44 It's looking for someone outside of Splunk, so you're right. Although, I still appreciate your blessing, because I know we've had a lot of discussions, but I'm not going to wait for you.
**Tyler** 24:53 Unless you want me to.
No, don't. I will try to take a look at it as well, but yeah.
**Pellared** 24:59 If I remember correctly, it will be even util, because… Oh.
**Tyler** 25:03 Yeah.
**Pellared** 25:04 Yeah.
**Tyler** 25:05 Yeah, because David's… yeah, outside of… okay. So yeah, I'll try to take a look.
**David Ashpole (dashpole)** 25:08 Hell yeah.
**Tyler** 25:09 Yeah.
**David Ashpole (dashpole)** 25:09 You can, okay. But Damien approved it.
Before a lot of changes, so, yeah.
He may be interested as well.
**Tyler** 25:20 Yeah, I saw some of these other test PRs yesterday, and I got halfway through them before I got distracted, but I'll try to prioritize all these PRs for review today, is my goal.
**David Ashpole (dashpole)** 25:32 Okay, cool.
**Tyler** 25:34 Awesome. Well, if that's that, that's the end of the agenda. Any other topics people have that aren't written there?
Any other cool… Things that people are working on externally?
With OTEL in mind, how's the Kubernetes space coming along, David?
**David Ashpole (dashpole)** 26:02 I don't think there's been any developments, although… It… you're gonna think I'm crazy, but it seems like a good… a good thing for me to throw an AI agent at and see what it comes up with, because I just don't have time to actually go Play around with it as much.
**Tyler** 26:20 Oh, nice, yeah.
**David Ashpole (dashpole)** 26:20 I think I know what I want, I just… Yeah, we'll see. So I'll see if I can make progress. There's someone else from Netflix who's driving it right now.
But it seems like a side project for them, so we'll see.
**Tyler** 26:32 Yeah.
**David Ashpole (dashpole)** 26:33 I'm… I am actually quite interested in the stable release of the… declarative schema package, because I want Kubernetes to use it to configure tracing in its components, rather than we have, like, a home… homemade You know, schema file that we use that doesn't support the vast majority of the features, so… Tyler 26:59 Yeah.
**David Ashpole (dashpole)** 26:59 That would be pretty cool to see.
**Tyler** 27:02 Okay, yeah, that's good feedback. That's great feedback.
**Pellared** 27:10 And he said.
**Tyler** 27:10 Oh, man.
**Pellared** 27:11 asking for Prometheus… Prometheus OpenTelemetry.
compatibility.
Anything you need there?
**David Ashpole (dashpole)** 27:19 Hmm… let's see, Open Metrics 2 is gonna probably have a release candidate in the next… Few weeks.
Bartek's gonna go out on leave in April, so we're trying to finish that up in March so that some of the Prometheus clients can actually start implementing it.
**I still don't… Pellared** 27:40 I see that Bartek will have a talk also in KubeCon, on Thursday.
**David Ashpole (dashpole)** 27:44 Yep, yep.
**Pellared** 27:45 Yeah, I already subscribed to it.
**David Ashpole (dashpole)** 27:49 Anything else interesting?
**Tyler** 27:52 I thought I saw a lot of open issues in the specification for stabilization.
**David Ashpole (dashpole)** 27:56 Yes, so those are trickling in, but it's like a PR a week that we're getting in, so it's looking like it might take another few months before we can look at marking our exporter stable. We're prioritizing the Prometheus receiver first, which is the Prometheus to Oak TLP mapping, and then we'll look at the reverse mapping after that, which is what matters for SDK exporters.
**Tyler** 28:23 Right, yep.
**David Ashpole (dashpole)** 28:26 Yeah, I think… I think next Tuesday I'm giving a spec… Or I'm giving an update on the whole thing in the spec sig, so, I'll have a little bit more prepared there.
For people who tune in.
**Tyler** 28:40 Cool, yeah, that sounds great.
Well, cool. Alright, yeah, if that's the case, we can probably end the meeting early here, if there's no more topics. It's good seeing y'all. I will, see you all in a week's time, or asynchronously. Until then, bye everyone.
**Sonal Gaud** 29:09 Thank you.
