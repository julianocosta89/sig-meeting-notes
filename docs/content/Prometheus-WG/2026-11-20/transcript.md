SIG: Prometheus WG
Date: 2026-11-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**David Ashpole (Google LLC)** 01:41 You're me.
Inc.
**krajo (Grafana Labs)** 02:15 I don't I won't have video, because I couldn't find a stable driver for my laptop camera.
So… Yeah.
**David Ashpole (Google LLC)** 02:25 It's…
**krajo (Grafana Labs)** 03:10 How are you, by the way?
**David Ashpole (Google LLC)** 03:13 I'm doing well. I'm recovering from a cold after KubeCon, classic.
**krajo (Grafana Labs)** 03:19 Oh, I'm in a cold right now, so…
**David Ashpole (Google LLC)** 03:23 Boom.
I've been very… I got a new bike.
Which I've been very excited about, but haven't been able to ride, because I have a cold.
So instead, I've just been riding the bike with my cold. It's hard, but it's fun.
Yeah, no, it's good. I'm, I've felt much better ever since we've stopped.
Just going on about the same question.
Now I'm just, like, working to try and stabilize stuff wherever I can, and… We'll get to the spec stuff when we can get to it.
**krajo (Grafana Labs)** 04:06 Yeah.
**David Ashpole (Google LLC)** 04:07 I've been making good progress on, like, the remote right receiver and the… Prometheus Exporter and Remote Write Exporter. There's a lot of cleanup to do.
**krajo (Grafana Labs)** 04:15 Oh yeah, that's, interesting. I don't know if you talked to Artur, but that's of interest to us as well. We have a client.
**David Ashpole (Google LLC)** 04:23 I'm… I'm just like… you know, wherever we can make progress, I want to make progress.
If we get stuck somewhere, then I'm just gonna try and make progress elsewhere.
The other client is coming along.
**krajo (Grafana Labs)** 04:41 Yeah, and thanks for the PRs on the JavaScript client.
The maintainer reactivated himself suddenly, so we got some comments, so I'm trying to drive that forward, and also possibly get another maintainer, although the person that is volunteering isn't… That grid, plus I have to do background checks, so… I don't know.
**David Ashpole (Google LLC)** 05:02 Hmm.
Yep, they've been… they've been helpful, they've been giving me some good feedback.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 05:13 Hello.
**David Ashpole (Google LLC)** 05:21 Alright, what's on the agenda for today? I think we should start with… you said you had some open questions on your PR cryo?
**krajo (Grafana Labs)** 05:29 Yeah, if you could bring it up, I'm, like, not in the… Best position, too.
there's two… Comments left.
I think that we should discuss.
And otherwise, it should be go to… good to merge, I think.
**David Ashpole (Google LLC)** 05:52 This is the right one.
**krajo (Grafana Labs)** 06:02 Yes.
**David Ashpole (Google LLC)** 06:11 Oh, nice, Josh.
**krajo (Grafana Labs)** 06:25 Yeah, we can probably, yes, resolve it.
**David Ashpole (Google LLC)** 06:27 Okay.
Do you wanna… I haven't… I'm reading this now, so if you wanna walk us through…
**krajo (Grafana Labs)** 06:39 Yeah, so… there's… Like, multiple places, but one place in particular, when we say that, you know, we associate, Job instance with some target info metric.
Like, basically do the join in the spec.
And Arba pointed out that maybe we should, like, say what Like, in what… domain we do the join.
And for a script, it's, like, fairly simple, because we do it inside one script, because that's, like, one… You know, set of… Things that we script, it's self-contained.
Everything's peachy.
But when it comes to the remote ride receiver, because of batching, you cannot just say that, oh, we're going to do it per write request.
That would be awesome, but, like, you know, you can get the target info.
In a different batch.
And, looking at the code.
there is a global cache, so if you send from, you know, 3 places to the receiver, that cache is populated from O3 and used by all three.
Even though, like, the per-request one is preferred, but it falls back to the… Cache, if it's… if the target info isn't in the… Request.
So… Yeah.
I I think the… The… this global cache is taking advantage of the… of the idea that job instance are identifying.
like, globally identifying in Prometus, but we avoided saying that, so it's kind of hard to suddenly come up with that here.
So I'm not quite sure what to write here. I, like, I have this little bit clumsy thing.
suggested that we… that we add what Arva suggested, which is, you know, per script, or per remote write request, or possibly cached.
In the receiver, and just… Not over what the curtain is. This isn't yep.
**David Ashpole (Google LLC)** 08:55 This isn't normative, right? This is just, like… Let me find which line this is on.
the infometrices… Oh, yeah, yeah.
**krajo (Grafana Labs)** 09:14 It is kind of normative, because we do say that.
**David Ashpole (Google LLC)** 09:16 It is, yep.
**krajo (Grafana Labs)** 09:16 Must be converted.
**David Ashpole (Google LLC)** 09:20 So this, this does matter.
**krajo (Grafana Labs)** 09:22 Yeah.
**David Ashpole (Google LLC)** 09:28 I… I would be okay with this.
If… if we… I would say it must… Be attached to anything that's part of the same request.
But I would go further and allow it to be attached to things that are outside of the request, meaning it would be Must for within a request, and may.
for… outside, because… Like, there's… with caches, there's always gonna be eviction, and like…
**krajo (Grafana Labs)** 10:02 Yep.
**David Ashpole (Google LLC)** 10:03 It's kind of like… I'd like to make it clear that It's not incorrect.
to do what the Prometheus receiver… or remote right receiver is doing.
But at the same time, like, there won't be an expectation that this… happens.
In, like, any random implementation. I don't know if that makes sense.
Arthur?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 10:26 I had a question. I think I'm… I didn't follow very well. You say that we have a problem because of batching?
And the problem is which component exactly?
**krajo (Grafana Labs)** 10:39 Remote right receiver.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 10:41 Receiver.
**krajo (Grafana Labs)** 10:47 The problem is that… yeah, sorry, go ahead.
**David Ashpole (Google LLC)** 10:48 You can go ahead.
**krajo (Grafana Labs)** 10:49 Yeah, so for… for… for Script, for the… normal Prometus receiver.
the… the kind of the domain where you do this joining from series to target info is one script. It's very simple.
But when it comes to the Prometheus remote write receiver, because the request can come in Like, it's not one request that has all the data. It can be, you know, 5 or 10 or whatever.
And then… There's a… there's a cache, basically, there.
So that you don't lose target info data.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 11:28 Okay, I understood, thank you.
**krajo (Grafana Labs)** 11:39 David, I guess, you know, in the interest of I meant, you know, moving forward, can we just try to come up with some… something that we agree on and commit that?
**David Ashpole (Google LLC)** 11:52 I'll suggest my… addition, And then if anyone opposes it, we can have that discussion. How does that sound?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 12:02 But I think krao's point is, like, could we do it now?
**David Ashpole (Google LLC)** 12:07 Oh yeah, I can do it now.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 12:08 Yeah, make the.
**krajo (Grafana Labs)** 12:09 Yeah, yeah, that's what I meant.
**David Ashpole (Google LLC)** 12:11 I see, I see, okay.
Suggestion, and then let's start with… Nope, that didn't work.
What's the best way to frame this?
Must…
**krajo (Grafana Labs)** 13:35 So, targeting food supply, additional resources needs.
Hmm. So… I mean, that cash… basically is keyed on job analysis and cache's resource attributes, so… I guess, resource attributes… Maybe copied from… a cash… keyed on the Jovan instance.
And then it's…
**David Ashpole (Google LLC)** 14:31 I mean, the other thing we could do… Does add or future?
Mmm, but this is a must.
**krajo (Grafana Labs)** 14:58 I don't think it's future, like, the cache is for the… for the past.
**David Ashpole (Google LLC)** 15:03 Well, it's saying that target info May apply to requests received in the future.
**krajo (Grafana Labs)** 15:09 Oh, I see what you mean. Okay, yeah, that sounds good, yeah.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 15:13 Do you think it's a bad idea to mention cache? Is this, implementation detail?
We could just say that, like, we could reuse from cached,
**David Ashpole (Google LLC)** 15:29 it's like, I would prefer… if we can describe it, just in terms of the… The inputs and outputs that feels better.
Yup.
But I'm not against cache. I don't like having it in normative language.
Normative sentences.
I'm okay to keep this general, because we're not… it's… it's a May, so ultimately this hopefully just gives us flexibility to… Apply this to future… Points as we see fit.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 16:56 This also means that if there is implementation, that remove… that receives… Target info and metrics in separate requests.
They are free to… To not implement this.
**krajo (Grafana Labs)** 17:14 Yeah.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 17:15 Yeah, I guess it's… that's fair.
Because, like, this requires… It's stateful implementations, it's more complex, less reliable.
Yeah, I'm fine.
**krajo (Grafana Labs)** 17:29 Yeah, you would probably… Yeah, I agree, but, like, you would probably still implement it, otherwise you're not getting… You know, some resource attributes. So, you have an incentive to do it.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 17:42 Yeah, yeah.
**krajo (Grafana Labs)** 17:43 Okay.
Sounds good.
**David Ashpole (Google LLC)** 17:50 Give me top, sorry.
Do you want me to commit this? I don't know if I can. Yes, I can. Do you want me to commit this now?
**krajo (Grafana Labs)** 18:01 I mean, Arve, you raised the point.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 18:07 I think it's good like this, Al.
I think it's on the improvements.
**David Ashpole (Google LLC)** 18:15 Awesome.
**krajo (Grafana Labs)** 18:16 Yep.
**David Ashpole (Google LLC)** 18:25 And then…
**krajo (Grafana Labs)** 18:45 Yeah, so this is basically a rephrase to be more easily understandable.
I think it's fair, so I would commit it, I just wanted to make sure that everybody's on the same page.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:03 Yeah, my goal with the suggestion there was to… to be unambiguous.
like I thought, the… I thought the original phrasing, had ambiguity, if you… if you cannot see it from, As… from someone trying to, to implement the, the, spec.
**krajo (Grafana Labs)** 19:36 Yeah, I wanted to be super precise, and I think I overcomplicated it a little bit, so I actually like this method.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:44 Yeah, I mean, reading this, at least I… It makes sense to myself.
I hope others feel the same.
**David Ashpole (Google LLC)** 19:56 Do you think it is worth combining these two paragraphs, or do you like having them separate?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:02 Hmm… didn't really think…
**David Ashpole (Google LLC)** 20:04 I don't know if you could… oops.
For each job.
**krajo (Grafana Labs)** 20:09 I mean… I would.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:12 I like… I like them as two paragraphs. I… I do, absolutely. So it's kind of like, they kind of do… They kind of have two… two different purposes, or responsibilities? So, yeah.
**David Ashpole (Google LLC)** 20:26 Only.
Yep.
This… This looks good to me. Are there any other concerns? Otherwise, I'm gonna hit the… I don't know if I can still hit the commit button. Oh, I can't, good.
Arthur, are you good with this?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 20:45 Yeah, yeah.
**David Ashpole (Google LLC)** 20:48 soon?
And then it says there is one comment thread somewhere left.
Scraping.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 21:06 Yeah, this is… this is the same thing, I think, just for scraping.
Yeah, exactly.
So, like, a repetition of the… of the concern.
**David Ashpole (Google LLC)** 21:18 Okay.
Yep.
Any objections?
**krajo (Grafana Labs)** 21:24 Nope.
**David Ashpole (Google LLC)** 21:32 And that brings us down to no open threads, and… Bunch of approvals. Should I hit the merge button?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 21:43 I approve.
**David Ashpole (Google LLC)** 21:44 Okay.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 21:46 I'll… I can leave an, I'm gonna leave an improvement on the PR, so, I mean, just for, For future's sake.
**David Ashpole (Google LLC)** 21:53 Great.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 21:56 What is… what is this UI? How do I get that?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:01 That's the… that's the key to a preview, isn't it? There's a green button, yeah, in the corner there.
I also used that. I think… I think I had that bug there once. I don't remember what the bug was, but there was something.
In general, I think it's okay.
**David Ashpole (Google LLC)** 22:21 Okay, and then we have another spec PR from Cryo.
Exponential histogram to Prometheus.
We did fix the zero threshold bug.
**krajo (Grafana Labs)** 22:39 Yeah, I don't remember if that was the last thing, I… Probably? But, they… I mean, the previous PR and this one changes the same changelog, so I would hold off.
**David Ashpole (Google LLC)** 22:55 Okay.
**krajo (Grafana Labs)** 22:55 Just… just… let's get that big one, you know.
**David Ashpole (Google LLC)** 23:06 It's this, but that's probably not that important.
S… I don't think this is particularly interesting, but I guess I'll just at least let everyone know that I did open a PR to specify the bridge. So this is the one that's in OpenTelemetry Go. I think there's one in Java as well.
This is… not… I don't care about the specification as much as the fact that it exists means that we can put it in the declarative config.
And have, like, a stable name for it and stuff.
Which would be pretty nice, if people could install the bridge that way.
Let's see, Arthur approved this. Would be good, maybe, to get one more approval on it. This is just the… It doesn't say anything other than… A Prometheus exporter is a poemetric exporter.
**krajo (Grafana Labs)** 24:24 What's the number?
I-445.
**David Ashpole (Google LLC)** 24:28 413.
**krajo (Grafana Labs)** 24:29 Okay.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 24:30 You know…
**David Ashpole (Google LLC)** 24:42 This is coming?
Oh, I never opened this.
Okay, so this, this is still on me. This is not ready yet.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 24:52 Like, this is about, today when there's conflict, we… put both values together, separate by a comma, right? And… We want to get rid of this.
**David Ashpole (Google LLC)** 25:13 Yeah, so this is keeping the most recent one by… Timestamp.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 25:18 Okay, about timestamp, okay.
**David Ashpole (Google LLC)** 25:22 So this is not… we're not gonna merge target infometrics.
I think last time we talked about this, we were happy with the change, but wanted it implemented upstream first.
In the collector.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 25:46 Yeah, I saw the PR, but I didn't review since it was the draft, so I thought you were still working on this.
**David Ashpole (Google LLC)** 25:51 Yep, I'm still working on it.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 25:53 Okay.
**David Ashpole (Google LLC)** 26:05 see if there's any issues for us to… I guess, does anyone have any topics? Otherwise, we can keep going through… Things that are… On our lists.
**Michael Burt (Splunk Inc.)** 26:17 Yeah, I was hoping to, raise the issue that we talked about, David, at KubeCon around a relabel processor.
**David Ashpole (Google LLC)** 26:26 Oh, yeah.
Let's go to contribute.
**Michael Burt (Splunk Inc.)** 26:33 I had talked to David at KubeCon about requesting remote configs on the remote write exporter, and he looked into it and provided a comment on this issue that maybe it would be better implemented as a processor.
**David Ashpole (Google LLC)** 26:52 Yeah, it's a tough one.
**Michael Burt (Splunk Inc.)** 26:55 You are.
**David Ashpole (Google LLC)** 27:00 So I… I don't know if other people have context, but… It would be easy for us to support write relabel configs.
In the remote right exporter.
The big challenge is, like, when you use relabel configs.
it's much easier to apply if it's already in the Prometheus data model.
And it's really hard to apply to the OTLP data model, because you essentially Have to convert them back and forth.
Or… Like, pretend you're converting them back to… back and forth?
I think it's mostly… It's mostly a question of, like.
We generally try and avoid processor behavior in exporters.
But a lot of people have… Like, relabel configs already written.
Arthur?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 27:59 I was not at KubeCon.
But I was at PromCon, which we had a similar discussion.
About, like, there's a lot of features from, remote, right, that we… We kind of duplicate the implementation in the collector side.
And it's mostly because… I wouldn't say because, like, since we never wrote the original remote write code, expecting people to use the way we are using in the collector.
like, the code just doesn't look friendly.
But, like, we have a bunch of maintainers in the Prometheus… we have a bunch of maintainers in the Prometheus side, and we have a different set of maintainers in the collector side, and it basically implements the same thing, just gets a bunch of data.
transforms into the protocol and sends it back… is sends through HTTP.
And we were considering, like… like, what if we refactor the Prometheus code in a way And we can just use the Prometheus implementation, both sides.
And I think if we get to this point.
I would be happy to implement relabeling configs, if that makes part, like, if this is part of the API. Like, I… I don't think with the theme that we have today, it's easy to maintain like, the codebase, if, like, it doesn't work very well with OTLP.
**Michael Burt (Splunk Inc.)** 29:39 Yeah, I think part of David's comment was that relabel configs are probably better suited as a processor in OpenTelemetry, just given, kind of, the design patterns of the collector, and how the relabel configs are You know, operating on the data flowing through the collector, as opposed to exporters, which are just exporting that data.
**David Ashpole (Google LLC)** 30:03 I think Anthony had also voiced that maybe in the past?
Is that… am I making things up? Maybe I am.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 30:12 Anthony Mirabella?
**David Ashpole (Google LLC)** 30:13 Yeah, yeah, I think this had come up before as well.
So I… when I looked into it, I didn't think it would be that hard to maintain. I thought we were… we would be able to use parts of Prometheus. Maybe not… maybe they're not intentionally exposed, but I thought they were. I can double check.
I think the biggest It's just whether we want this functionality in the exporter.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 30:39 Yeah, since I joined the SEEK, almost 3 years ago, I've never seen Anthony. So if the discussion happened, it was a very, very long time ago.
**David Ashpole (Google LLC)** 30:49 Okay, yeah, yeah, that's fine.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 30:52 I… if… If we… Do this in a processor.
I… who is maintaining this code?
**David Ashpole (Google LLC)** 31:11 Yeah, that's a good… that's a good question.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 31:18 If we have maintainers, I'm happy to sponsor.
But I cannot maintain this myself.
**Michael Burt (Splunk Inc.)** 31:27 Yeah, I'm a maintainer of a couple different components in the collector, and I'm happy to submit a PR for this. I don't have as much experience in the Prometheus core codebase, though. I have contributions to, like, Prometheus Operator and Thanos and other parts of Prometheus, but also on Server.
Splunk also maintains a pretty widely distributed distribution of a collector, where I could… take a stab at implementation, but my worry is that I won't get the types of feedback from the Prometheus SIG or community if it gets implemented in the Splunk distribution, as opposed to the It's a broken trip.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 32:07 Yeah.
**Michael Burt (Splunk Inc.)** 32:09 And I… I don't want to do anything out of band without the… You know, buy-in of this group, so…
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 32:16 I think I'm happy to help. Like, I just… I'm just concerned if there's just code a strong Above the wall, and… Like, if you're willing to collaborate with us, yeah, I'm also happy to do it.
**Michael Burt (Splunk Inc.)** 32:32 Yeah, I would definitely appreciate the opportunity to engage more with this SIG and this code, so…
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 32:39 Nice.
And also, I also want to mention that, like, in the Prometheus community, unrelated to Hotel, we've seen several times discussions happening just, like, changing the Prometheus codebase just to help or tell.
So if you get this processor going, and we see it gets momentum, we see adoption.
we could ask Prometheus to refactor codebase a little bit.
as long as it doesn't bring downsides from each, of course. So the processor is easier to maintain.
**Michael Burt (Splunk Inc.)** 33:20 Yeah, that sounds good.
Should I, start with kind of a design proposal and add it to this issue and get some feedback?
**David Ashpole (Google LLC)** 33:29 Yeah, I would… I would be really interested to see a prototype. I'm… Like, conceptually, it fits as a processor.
I'm worried that we won't be able to make it.
Performant.
Like, if the idea is we're gonna convert to… the Prometheus representation.
run the relabel configs and then convert back. Like, that'll be super expensive.
**Michael Burt (Splunk Inc.)** 33:52 I mean…
**David Ashpole (Google LLC)** 33:53 And so… Yeah, it might be interesting just to throw together a prototype, doesn't have to be cleaned up or whatever, so we can try and evaluate it and figure out if it's really a viable path.
In terms of, like, Being correct, and being… reasonably efficient compared to, like, OTTL or something.
Arthur, I'm not sure if you wanna… It seems like you're potentially interested in… Putting this in the exporter, kind of… Anyways, maybe, if it's already functionality that Prometheus Upstream would support?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 34:30 Yeah, if we find a way to refactor the Prometheus codebase, so relabeling configs as part of the API itself, and we… we just import a library, and we get this for free in the collector, that would be… that would be nice.
But again, needs discussion with Prometheus, remote Bright maintainers, needs to pass performance, etc, etc.
**David Ashpole (Google LLC)** 34:57 I mean, I think it's gonna be way more performant if we're doing right relabel configs on Prometheus data, right? Because this… Michael, am I understanding correctly that This is a feature that Remote Write already supports?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 35:12 Yep, it is.
**David Ashpole (Google LLC)** 35:13 Yes. Okay.
**Michael Burt (Splunk Inc.)** 35:14 Yeah, yeah.
**David Ashpole (Google LLC)** 35:16 Okay.
**Michael Burt (Splunk Inc.)** 35:19 I think for my use case, and most use cases I can imagine, I think it's okay to do it.
In the exporter, I think if you were to do it as a processor, maybe people could use the Prometheus relabeled DSL on OTLP in and OTLP out.
But it seems like a very common use case. Mine is I'm scraping Prometheus, and I want to send it to multiple backends with different relabel configs, and it's not possible with the collector today.
**krajo (Grafana Labs)** 35:57 See you.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 35:59 See ya, bye-bye.
Okay, oh, Michael, already… Buena.
I think, I think Michael saw us saying goodbye, and thought the meeting was over.
**David Ashpole (Google LLC)** 36:19 If I'd cry.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 36:21 Yeah.
No death.
**David Ashpole (Google LLC)** 36:24 Let me…
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 36:24 Okay, yeah, do you have his… his Slack? You can tell him that he's happy… that we are happy to proceed.
**Michael Burt (Splunk Inc.)** 36:38 Sorry about that, I realized that you guys kind of weren't ending the meeting.
But yeah, just, I guess I can look together a prototype and, put together some… proposal around design here, Arthur, and we can collaborate on this issue.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 36:54 Yeah, sounds good.
**Michael Burt (Splunk Inc.)** 36:56 Great.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 36:59 We were wondering if you saw us saying goodbye to Cryo, and if the meeting was over.
**Michael Burt (Splunk Inc.)** 37:05 Yeah, sorry about that, I didn't see the chat message there.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 37:09 Yeah, no problems.
**David Ashpole (Google LLC)** 37:24 Just taking notes.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 37:32 Michael, you're… you're gonna, start proposing the processor, right? If I understood correctly?
**Michael Burt (Splunk Inc.)** 37:44 I think so, yeah.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 37:46 Yeah, yeah, okay.
**David Ashpole (Google LLC)** 37:48 I think I'd like to see a prototype of the processor, and I'd like to see how much worse it is than.
Other things, that'll give us some numbers.
So we can figure out if it… If it makes sense as a separate processor, if we should try and build it in.
Because I agree it would be easier to maintain if it was just part of the exporter.
And just use the Prometheus library.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 38:17 And by the way, the main drivers on this was Bartek, And Kyle Eckert.
About refactoring remote, right, to be easily reusable.
The thing that they asked is if this refactor happens, then the maintainers on the collector side also help maintain, on the Prometheus side.
And I think the maintainers today are you and me, and I'm happy to do it.
**David Ashpole (Google LLC)** 38:51 We'll see. I do enough for Bartek now, huh?
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 38:53 Okay.
**David Ashpole (Google LLC)** 38:55 Sure.
Why not?
Alright, what else do we have? Should I keep… I can find more spec issues, if that's helpful.
Or we can call it.
**Michael Burt (Splunk Inc.)** 39:09 There's another component, actually, that one of my coworkers, kind of had a crackpot idea, which was, like, a Prometheus MQL receiver, actually.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 39:20 Alright, Antoine?
**Michael Burt (Splunk Inc.)** 39:22 Yeah.
I don't know if that has been discussed in the SIG or not.
**David Ashpole (Google LLC)** 39:28 I talked with him at KubeCon, actually, about it as well.
**Michael Burt (Splunk Inc.)** 39:31 Yeah. Okay.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 39:33 How'd it go?
**Michael Burt (Splunk Inc.)** 39:39 Yeah, David, did you guys come to any decisions or anything for the future event?
**David Ashpole (Google LLC)** 39:43 Oh, I'm… Hmm.
My recollection was that… I talked through some of the challenges with him, right? Like, PromQL… a PromQL receiver would have some of the same issues that recording rules would have, which is, like.
You'd generate a bunch of float histograms, and then we would proceed to drop them immediately.
Cause we don't support them.
Other than that… It definitely is viable.
It's like, he was describing some of the use cases, Behind the receiver.
And it sounded like they would actually, honestly, be better met by… the remote right receiver, then by a PromQL receiver.
It doesn't mean that there isn't, like.
it's pretty similar to recording rules, right? Except it's… from a TSDB instead of from scrape, right? So, like, clearly there are reasons why people use recording rules, so… It'd be interesting.
right, we could work on a PromQL receiver, we could also work on a… what's it called? If we need recording rule support in the… Prometheus receiver, that could also be an option.
But they're both… they both are pretty similar, right? They do essentially the same thing.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 41:15 I also worry about performance, like, it's… I've… I feel like this is a very easy way to kill your backend.
if you put some, like, crazy queries on the PromQuil receiver, you're constantly hitting backend with dispensive queries, like, this is gonna blow up very quickly.
I frankly, I always… was designed… was not designed to be a data transfer protocol. It's not optimized for that. Remote ride was, so… Yeah.
**David Ashpole (Google LLC)** 41:49 That's a good point. If you're already… storing something in a Prometheus… System.
It's almost like you'd rather… Use a recording rule on the way in, and then remote write that to the collector.
Rather than try and… use a PromQL query to generate the metric.
when I talked with Antoine, the conclusion we came to was mostly that, like.
We probably don't want to build this.
But I'd have to understand the use cases better.
**Michael Burt (Splunk Inc.)** 42:26 Yeah, I mean, I think generally a PromQL receiver would support, kind of service teams who don't own the backend infrastructure of Prometheus, necessarily.
It's pretty easy to add, like, a prom rule.
If you're a service team, but, adding, like, remote write configs on the ruler or something is, like, a different thing entirely.
So, but the collector, you know, you can use some hotel collector custom resource.
and configure PromQL and be able to extract data from PROM and move it into other backends more easily. But I understand. I think, I don't have a strong opinion on this either way. And I definitely see the wisdom of a comment like PromQL's not transport protocol. That's true. I think it feels like an abuse.
The collector to introduce something like this.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 43:34 Cool,
**David Ashpole (Google LLC)** 43:36 Yeah.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 43:38 I think if we… with us merging this, this, SPAC PR that we discussed earlier.
We are now good to go back to the… So what we do… what do we do with, resource attributes, right?
**David Ashpole (Google LLC)** 43:57 I think the plan was to open competing draft pull requests? Arv, is that what you remember?
Or, like, open them for each… Proposal.
So we could evaluate them? Is that what we want to do?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 44:13 Yeah, I think I remember you suggested that, let me see…
**David Ashpole (Google LLC)** 44:19 don't cry.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 44:20 Where are… where are we? There again, like, I mean, yeah, I think that suggestion came from krajo.
Mmm… So where are we… so that's where… that's… that's where we're at? I don't quite remember anymore.
**David Ashpole (Google LLC)** 44:37 Yeah, cr… that krao said that he… Wanted to get them all written out properly, and then he said that writing them out properly was too hard because of the current Specording.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 44:49 Yeah, that's the thing, that it was sort of dependent on the… On cleaning up the current spec wording first, but are we… have we got to that point where it's clear… all the cleanup is done?
**David Ashpole (Google LLC)** 45:03 that that was what this PR was supposed to be. I think if they…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:06 Okay.
**David Ashpole (Google LLC)** 45:06 cleanup we want to do, we can, obviously, but…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:09 Yeah, yeah, maybe we have to… like, like, I… I almost don't know how much cleanup krajo thought we needed to do.
Bam.
But I guess krajo needs to… so krajo is the one who has opened one and more PRs at the moment, right? No one else?
**David Ashpole (Google LLC)** 45:31 In the spec, I think there is… there were, like, 2 or 3 small PRs, but unrelated to the… Resource specification at all.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:41 No, I meant the… the PRRs, corresponding to the design doc proposals. That was the idea, right? That Nikario proposed.
**David Ashpole (Google LLC)** 45:51 Yeah, none of the proposals have any open PRs right now.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:55 I thought kojo had maybe gave up before cleaning up.
I thought he had to open the PR.
But maybe I misremember.
Maybe he…
**David Ashpole (Google LLC)** 46:07 Yeah, yeah, yeah.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:08 As I said, the… oh, yeah, yeah, I had the recollection he started on that, but then maybe he, kind of gave up, because he realized cleanup was needed.
Yeah, so… Probably, we're back to the point… Where… where we should open those PRs, like, certainly CAIO, is planning on, opening one or more PRs?
But, what I can do is I can sync with WG on… Monday?
True.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 46:46 Do you think Cryo will… wants to open all?
like, a PR for each proposal, or is, like, David writes his proposal, you write yours.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:57 I…
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 46:58 No, it is.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:59 I just remember that krajo wanted to spread the load, specifically. Like, he didn't want to do all of them.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 47:05 Alright, makes sense.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 47:06 Which is understandable… which is understandable.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 47:09 Yes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 47:11 I'm just trying to see if he's available on Monday… Oh, yeah, it's probably semi-available on Monday, so I'll check in with him then.
**David Ashpole (Google LLC)** 47:31 Cool.
Yeah, I can put something up as well.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 47:37 I'm gonna do a surgery on Monday, I'll be out for a week, so I'll be able to help.
But in the week after, I'll be back, and I can start helping more.
**David Ashpole (Google LLC)** 47:52 Yep. And next week is… holiday week for the U.S. for Thanksgiving, so…
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 47:58 Okay.
**David Ashpole (Google LLC)** 48:00 I'll be semi-available early in the week.
Yeah, we can maybe, for the next SIG meeting, have a goal of having, At least… the two main… proposals up as pull requests, as draft PRs.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 48:18 Yeah, sounds like a good goal.
**David Ashpole (Google LLC)** 48:21 Cool.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 48:28 nose.
**David Ashpole (Google LLC)** 48:28 We can keep going through stuff, but,
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 48:34 I think we don't have many open PRs, and the ones open already have, like, approval from everybody. It just needs to merge.
**David Ashpole (Google LLC)** 48:41 Okay.
Cool.
I have more coming.
**Arthur Silva Sens (Raintank, Inc. – Grafana Labs)** 48:46 Okay.
Alright, thank you, everybody. Thanks. See ya.
**David Ashpole (Google LLC)** 48:51 Bye.
