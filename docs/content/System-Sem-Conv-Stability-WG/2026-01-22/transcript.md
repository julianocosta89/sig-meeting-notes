SIG: System Sem Conv Stability WG
Date: 2026-01-22
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/EcrNmIHy2UDNCTMah3DKVRdFtycqXzroJlO2Uz2FszrcXQK9EuxPSK_E7jl0itE.3H9tNh-A5GxWNoMp
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:48 Hey guys.
**Braydon Kains (Google)** 01:51 Hello. Opt.
Opt out?
Right? Because who is this person who added Read.ai to them?
Okay, that worked.
Nice.
We've had… we've had worse AI bots that were way harder to kick.
**Christos Markou** 02:11 Oh, that was easy. I just started looking for the guides on how to remove it, because it's been a while since we do it.
Yeah. Since we did it, yeah, but that was easy.
**Braydon Kains (Google)** 02:24 I think this one… this one was just…
Had to type something in the chat, that's good.
I don't even know who that is. Did they join a previous SIG meeting somewhere? I have no idea.
**Donal O'Sullivan** 02:39 Surely you'd have to update the meeting invite for that, would you?
**Braydon Kains (Google)** 02:42 I think so? I mean, in the past, we've had some where, like, if a person happens to join a meeting one time, their bot will continuously rejoin that invite, just, like, all the time.
I also think it's possible that
some of these… like, I don't use any of these, but I would imagine that some of them might integrate with someone's calendar, and so if someone put the hotel calendar merged with their calendar, the AI would be like, oh, you're going to all these Zoom meetings, I'm gonna attach myself.
**Donal O'Sullivan** 03:16 Nice.
**Braydon Kains (Google)** 03:19 Very fun.
**Donal O'Sullivan** 03:21 Very sneaky.
**Braydon Kains (Google)** 03:22 Yeah.
**Dmitrii Anoshin** 03:39 Hi, everyone.
**Braydon Kains (Google)** 03:40 Morning.
**Christos Markou** 03:42 Nope.
**Braydon Kains (Google)** 03:49 Yep.
I know I have stuff that is assigned to me that I did not make much progress on. I'm on a, like, tight deadline project that's not going super well, and I haven't had time for
much, much else outside of that recently. So, if there is things that are waiting on me, let me know and I can…
Try and get to it soon.
I know that the big one is my…
I have a PR for our OS naming guidance that got a bunch of feedback, and I haven't addressed it yet. And there was the issue I was going to open about encoding duration, either in a name or in a label, and I haven't gotten to that yet either.
**Dmitrii Anoshin** 04:43 That's fine, I guess that's the common problem between all of us.
A lot of stuff.
**Braydon Kains (Google)** 04:49 Yeah.
**Dmitrii Anoshin** 04:50 On other sides.
**Braydon Kains (Google)** 04:54 has kicked in.
**Dmitrii Anoshin** 04:56 Yeah, true.
I guess there is nothing else on agenda.
Do you think, we can… we should discuss anything else, or we can just call it for today?
**Christos Markou** 05:16 Is there anything we could maybe, like…
I know we have these, two items for the process stability.
That we discussed those also the other day. Anything on the host metrics receiver that…
It's, like, open for whatever, maybe, Donald, joined, joined us also to help here, so maybe he could…
Give a hand there, I don't know what's the status.
last time I saw, I tried to actually apply the dual, the feature gate thing on the host metrics receiver, and Briden, maybe you remember,
I found these issues with, how code is generated, and what we should do with,
Settings and enabling, disabling the metrics, because we don't have anything like aliasing.
So, yeah, we need to figure this out.
**Braydon Kains (Google)** 06:18 Yeah.
Yeah, I actually don't know how to handle that part of it either.
**Dmitrii Anoshin** 06:25 I can, like, maybe help with that, but I don't have any time to work on it, but if you, like, don't know if you have time to do some investigation and come up with some ideas how to approach that, I can… we can maybe collaborate, and I'll provide some feedback, and
If you want to take that part.
In general, that would be…
**Donal O'Sullivan** 06:47 Yeah, no, yeah, that sounds good. I appreciate that, Dimitri. So that's the, issue I put in the document there. Is that the one we're talking about? So it's figuring out, like, that…
my, you know, handling both legacy and… Current scheme is, is it?
**Braydon Kains (Google)** 07:03 Yes.
**Dmitrii Anoshin** 07:05 Yeah, that's one, yeah.
**Braydon Kains (Google)** 07:08 Yeah, this is the parent issue, and I think this is where Crystal's put the… the issue with the… with the config that we… I don't know how to… how to figure out, either.
**Donal O'Sullivan** 07:17 Yeah, I… yeah. I was looking at this, just reading through it, and I know the second point there was just about refract… Refactoring the,
Each scraper.
So that's obviously a separate thing.
**Braydon Kains (Google)** 07:31 So…
**Donal O'Sullivan** 07:31 No, you… you promised.
**Braydon Kains (Google)** 07:32 Yeah.
**Donal O'Sullivan** 07:33 operating, I think you bought them, didn't you?
**Braydon Kains (Google)** 07:35 The big thing is, like, so the general plan was mdataGen.
Generates two packages, one for the old schema, one for the new schema.
And the feature gate decides which one to build, and we…
I had an idea for, like, an abstraction that would say, like, that we would actually interface for, like, record data point for, like, CPU time or whatever, and based on the value of the feature gate, it would use either the semconf package or the original metadata package, and…
Build the right the right semconf that way, or the old schema, basically.
But the issue Crystal's brought up that I don't know how to deal with is the fact that the, the,
config.
gets really screwy, because we have a field in the config called metrics, and it's not like we can
merge them both exactly? Like, it's either one or the other, and…
We can't have, like, the semconf metric builder config
As a separate field that we then, like.
Break by deprecating and moving into the original metrics field.
But we also can't… Alias both of them as metrics that
Changes based on the feature gate.
**Donal O'Sullivan** 09:01 So you want to use one or… so you want to use one or the other, you can't use them both at the same time?
**Braydon Kains (Google)** 09:06 The only way to use both at the same time is…
Either to have a, like, some way to, like, squash them into the same structure.
or to have two fields, one called metrics and one called, like, semconf metrics or something, but then the forward compatibility gets screwed up there when we decide to deprecate the old schema and move only to the SEMCOM schema, and then it's like, people have a SEMCOMF metrics field.
That they need to move into a different name.
**Donal O'Sullivan** 09:36 There is a pattern you can use, like a strangulation pattern, where you're only… you're allowing the old version
And then eventually you migrate that out to…
To only allow the new version.
Like, you're strangling the old pattern now, it's kind of a weird name.
Yeah, would something like that work?
But, sorry, so is the idea you would allow a user to use both schemas at the same time? No, that wouldn't be a thing, right?
**Braydon Kains (Google)** 10:03 I… think we… Would want that to be possible.
**Donal O'Sullivan** 10:08 Right.
**Braydon Kains (Google)** 10:09 People might want to compare one against another… one against the other, or produce both and migrate their dashboard slowly over time.
**Donal O'Sullivan** 10:18 Yeah, yeah, yeah.
**Braydon Kains (Google)** 10:18 We want that to be… to be possible.
**Donal O'Sullivan** 10:22 So this is purely talking about the metadata, if you have two different versions, and you can generate the code from the two different versions. Is that what we're talking about?
**Braydon Kains (Google)** 10:31 that's what we're talking about under the hood, but the problem that I don't know how to solve is the configuration side of things, because the
Awesome.
**Dmitrii Anoshin** 10:41 So the configuration parts, they are all…
generated and publicly exposed, right? So, potentially, you can just redefine another metrics struct, And, like, manually, somewhere.
And, fill it with, metrics from both, generated.
**Donal O'Sullivan** 11:03 Yeah.
**Dmitrii Anoshin** 11:04 From both generated configs, manually.
**Donal O'Sullivan** 11:07 Yes.
**Braydon Kains (Google)** 11:09 That's the only one I can really think of where, like, we make some… some, like, intermediate struct that squashes both.
**Dmitrii Anoshin** 11:16 Yeah.
**Braydon Kains (Google)** 11:17 Intuit.
**Dmitrii Anoshin** 11:18 Right.
**Donal O'Sullivan** 11:21 Are there other than Meta.
It's like a meta-meta config, maybe. You combine both, and then eventually you just get rid of that and use the new one.
**Dmitrii Anoshin** 11:30 Yeah, that can be done manually. And also, I guess the feature gate would be enabled, you would disable all two feature gates, and we need that.
that additional… Config only if both feature gates are enabled.
**Braydon Kains (Google)** 11:47 Yeah.
**Dmitrii Anoshin** 11:48 Okay.
Does that make sense?
**Donal O'Sullivan** 11:51 Just in terms of the GitHub issue, so is that… that main one I linked, is that the one to be working off for that, or is there, like, a sub-issue created already, or…
**Braydon Kains (Google)** 12:00 There is not a sub-issue created for the scraper refactors yet.
**Donal O'Sullivan** 12:05 Okay.
**Braydon Kains (Google)** 12:06 This is sort of like the parent tracking issue we've been using for a long time.
Yeah.
I know I've made subissues for some things, but, not for this. I can make a sub-issue for this, we can discuss it there.
**Donal O'Sullivan** 12:20 Yeah, yeah, I could also do that as well, if I should have a bit of time, if that makes sense. You might have more…
Context, though, Braden, I guess, to…
**Braydon Kains (Google)** 12:34 I'll make the initial issue, and I can… I can assign it to you if you'd like.
**Donal O'Sullivan** 12:38 Yeah, cool, yeah.
Sounds good. I can, yeah, I can work on it then, I guess.
Yeah, sure, I'll try and get something… try and get something going, and I guess we can… we can see what it's like, and kind of go from there, if that makes sense.
**Dmitrii Anoshin** 12:53 Oh, good. Thank you, Donald.
**Donal O'Sullivan** 12:56 Yep. Thanks, guys.
**neilyashinsky** 12:58 Yeah, hi everyone, pardon me, for…
jumping in, but I'm very new to the,
Special Interest Group, my name's Neil, nice to meet you all. I wanted to chime in, because I've actually,
Been working on an approach that might be instructive here, if you don't mind me,
Sharon, a little bit of code in the comments?
**Braydon Kains (Google)** 13:22 Sure. Well, this is actually not code yet, I guess. This is.
**neilyashinsky** 13:25 my approach, but, it didn't render very nicely, unfortunately. But basically…
I, used… I think what you were talking about was basically a single configuration with two explicit modes, and with a… with a attempt to basically…
Because I had an older schema, and now I'm moving completely to, like, the OTEL Gen AI and the ATA schema, and so I had… I think this is similar. Please stop me if you think this is totally unrelated, because I am so new, so that's why I wanted to validate before I…
Proceed. If this seems like, what you're talking about, though, I'll continue.
**Braydon Kains (Google)** 14:08 Sort of. I think there is…
There is a requirement for this to be controllable by feature gates so that we can control
In a visible way when things become default on or default off.
**neilyashinsky** 14:22 Yeah, so, okay, well, yeah, I mean, let me know if you need more. I mean, I'm happy to post another link, or even look at the issue, with someone's help, as well, of course, considering my newness.
**Braydon Kains (Google)** 14:36 So this is,
the way you were… sorry, you were working on a separate project. This wasn't specifically working on most metrics, but this was… but this is… you had to solve the same problem.
**neilyashinsky** 14:48 Yeah, exactly. This is, exactly. So, I think there's a little bit, just more detail on, like, the
How to, how to transition from one…
semantic convention, I guess, to another.
And, you know.
have some transition period if you want, or, like, be… I guess I tried to be as…
accommodating as possible to allow people to do what they felt was best for some period of time, and then support a cutover, if ever they felt.
Necessary.
**Braydon Kains (Google)** 15:23 Was your project, like, within the collector, or was it something separate?
**neilyashinsky** 15:27 Oh, yeah, I mean, I take an OTEL philosophy, so I have kind of, like, a description of the requirements, if you will, a protocol that I have to follow, and then I have a software reference implementation of it as well.
**Braydon Kains (Google)** 15:38 Okay. The…
The… part of the challenge that we need to specifically deal with has to do with, like, specifically within the…
collector configuration, when you have a component that enables or disables metrics, the configuration under the hood is, like, generated. So, the… Correct. In the YAML, the name of the metric, and then enabled, disabled.
That all gets generated. And so, how we handle that with two schemas,
might not apply quite the same way, if I'm understanding this part correctly, because we still… we still need to solve that problem of that the config
will break regardless.
Because of the generated nature of it, if we generate new config that…
Changes when old schemas go away.
And
Like, we also need to support, like, people to, like, enable and disable individual metrics in both schemas at the same time.
So, that… I don't know how to…
Get rid of the forward compatibility pain there.
**neilyashinsky** 16:45 I… yeah, I… I dual emit, I guess is the simple answer in the beginning. So I do dual implementation, or dual emit implementation to allow both to be created, but I… but again, I'm so new, I don't know if that would solve your problem or not.
Of omitting both of them, if that still breaks the metrics being generated.
**Braydon Kains (Google)** 17:07 I think we… we… we are planning to allow emitting of both of them. It's, it's about,
when we get to the point where we want to deprecate and remove the old schema, that's the pain that we're not sure if we can get around.
**neilyashinsky** 17:22 Oh, I see, I see.
**Braydon Kains (Google)** 17:24 Because eventually, that old scheme.
**neilyashinsky** 17:25 run over.
**Braydon Kains (Google)** 17:26 to go away.
**neilyashinsky** 17:27 Right, right.
Interesting. I'll say less, but thank you for entertaining me, especially so new to my… You know, time together.
**Braydon Kains (Google)** 17:37 Yeah, thank you for sharing. I mean, we need any ideas we can to try and figure out the best way to do this.
**neilyashinsky** 17:45 Okay, great, maybe I'll work on the, on the,
Is it a… is it an issue? I'll lurk on the issue a little bit and see if I can add some more value in the comments.
**Braydon Kains (Google)** 17:54 Yeah, it's… I'll open it, and I'll put it… I don't know if you're in the System Metrics Slack channel, but I'll… I'll post the issue there.
**neilyashinsky** 18:01 I don't think I've been added, to the Slack instance here.
**Braydon Kains (Google)** 18:05 So, that one is public, that you…
**neilyashinsky** 18:07 Oh, that one is popped up.
Oh, okay, great, then I'll jump in there.
**Braydon Kains (Google)** 18:10 Health System Metrics, is what it's called.
**neilyashinsky** 18:12 Perfect.
Thanks. Is it Braden? Thanks, Brad.
**Braydon Kains (Google)** 18:14 Yep, no problem.
**Dmitrii Anoshin** 18:29 Okay, I guess that's it for today.
**Braydon Kains (Google)** 18:33 Probably.
**Christos Markou** 18:35 Cool, folks.
**Braydon Kains (Google)** 18:37 They're on.
**neilyashinsky** 18:39 Thanks. Have a good day, everyone.
**Braydon Kains (Google)** 18:41 Thanks.
**neilyashinsky** 18:42 Yeah.
