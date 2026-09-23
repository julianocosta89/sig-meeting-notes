SIG: CI/CD SemConv SIG
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 02:44 Hello, hello.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:49 Hey, how's it going?
**Robert Pająk (Splunk Inc.)** 02:51 Fine, how about you?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:52 I'm doing okay, thank you.
**Robert Pająk (Splunk Inc.)** 02:55 I see Christoph is not joining.
I'm not sure about Alan, but I know he's busy recently.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:04 Okay.
**Robert Pająk (Splunk Inc.)** 03:09 Do you have anything, on the agenda?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:12 I can put one thing on the agenda.
**Robert Pająk (Splunk Inc.)** 03:20 One is good. It's nice. It's more than.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:22 Yeah, exactly.
**Robert Pająk (Splunk Inc.)** 03:34 Nice again.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:55 I cannot spell this morning.
Anywho… Let's see… So…
**Robert Pająk (Splunk Inc.)** 04:08 Do you want to share your screen, or present, or you want to…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:11 Yeah, I can… I can share, I guess.
The… I don't know if I want this on recording, though.
I'll just preface it on the recording as we do not condone nor support or nor prefer any particular observability vendor. That's gonna be my.
**Robert Pająk (Splunk Inc.)** 04:35 Display.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:36 And then, I can share, where is my… alright.
So there's been some issues… let me see if I can find the issue, too, actually, that would be helpful.
And I think I gave you access to this. If I didn't, I… am sorry, I definitely can.
I'm allowed to do that within the CICD group.
But I just have been asked to keep it under wraps, because it's been a temporary thing. So, not last year, but the year before… I think it was the year before, yeah, it was the year before. When we did a talk at, KubeCon EU, we had… had built two… specific solutions.
Let me find… Here's the other thing. We had built two specific solutions that, Are the backends for storing the telemetry that comes from all of our… traces. And one of the things we demoed in that talk was, like, the ability to understand the queue times, and troubleshoot them, and, like, catch them early instead of having, like, people just say, hey, what's going on with my pipelines? Why are they not running?
Well, the queuing issue has popped back up in the community within OTEL. There's lots of pipelines that are getting queued. This is a GitHub problem, more than anything. But, this is… this observability data that we… we have.
Has not been opened to the community.
Or to the observability community, or the hotel community, rather.
And so, I can't make it open to everyone at this point in time, because it is stored primarily in a vendor. We used to have two, we had, we had, Honeycomb was one backend for the demo, and then I had also deployed a self-hosted version of Signals.
There. Just as two, like, so we could show both, like, more than one option, and kind of have the whole, like.
We're not picking solutions here, we're just, like, showing you the fact that, like, the traces themselves can, you know, be sent to anywhere, right?
in the hotel way. But… but now there's more of a need for the larger hotel community to be able to have access to this data, and so that does not… Fly being stored in a vendor at this point in time.
Because we don't want it to, you know, seem like we're picking solutions here. Now, we do have the traces, and I can send this to you for the, like, interim, Like, this is, just a quick little board I created, the other day. I don't know why it does that.
used to not do that, but, I want to expand it. I don't remember how to expand it, they've changed a lot. I don't look at this frequently, but we do have, like, QSPAN stuff, but the whole thing is, is, like, where do we store this telemetry, like, moving forward, so that the whole community can, can benefit from it?
And it's not just a measure of, like, is it open source or not, it's a measure of, like, is it open source and vendor-backed, or not. So, like, Prometheus is CNCF-owned, so for metrics, that'd probably be okay. But, like, Grafana is not CNCF-owned, so that probably wouldn't be okay.
Same with, like, ClickHouse. I'm very familiar with ClickHouse. I have a preference for it. It's, like, not that hard to maintain for me. And actually, most of this infrastructure I maintain on myself right now, like, on an Oracle VM.
Out in the cloud, but it's, it's just, like, all on, like, me. Interesting.
**Robert Pająk (Splunk Inc.)** 08:45 Do you think that Grafana would be really a big issue, given… You can…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:51 Unfortunately, yes.
**Robert Pająk (Splunk Inc.)** 08:54 The issue… the thing is that we have already precedence that's used in OpenTelemetry demo.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 09:00 Right, okay, that's good to know. I didn't think about it from that perspective.
**Robert Pająk (Splunk Inc.)** 09:04 You know, I think that it was allowed for years, because there was not… I don't know if there was not… like, I'm not sure if there's anything com… like, you know, good enough, which is CNCF, you know, inside CNCF.
there is a lock key for me to use, but I think that for… I'm not sure what is for logs right now. I can quickly check, I think OpenTerm SVIO, if you go, I think there's a section about demo.
I think it's in ecosystem? Yeah, ecosystem? Demo?
Open 33 demo documentation.
Let me check, what is described here?
Architecture.
All right.
of survivability.
Jaeger, open search for Meteos.
OpenSearch, I think, is… isn't it CNCF?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:06 It's not CNCF, but it is Linux Foundation.
**Robert Pająk (Splunk Inc.)** 10:10 Okay, so probably that's the way.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:13 Yeah.
**Robert Pająk (Splunk Inc.)** 10:15 I don't have Grafana for the UI, because I don't share if there's anything even links foundation, or the UI, or, you know, merging them together.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:24 Right.
**Robert Pająk (Splunk Inc.)** 10:26 Oh, just…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:27 Perkins search not come with a UI by default anymore?
**Robert Pająk (Splunk Inc.)** 10:31 What do you mean?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:33 I, I thought open… go ahead, sorry.
**Robert Pająk (Splunk Inc.)** 10:37 I mean, there is wide open search, Jaeger and Prometheus, it's just you do not have, you know, these combined dashboards, etc, in one place. Everything is separated, and in Grafana, I think you have extensions to correlate stuff with Jaeger. For sure, with Jaeger and Prometheus, I was doing it also for some Or some presentations, probably for open search as well.
I'll just send this to you, maybe to help you somehow.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:02 Yeah, I… Cool, thank you. Yeah, the options are definitely…
**Robert Pająk (Splunk Inc.)** 11:10 Okay, limited.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:13 I… the ask of me has been to provide some options and their pros and cons, to Trask and Mary, and she'll be able to take that to the… to the, like, GC, and say, like, okay, what… what are we willing to approve? But that's kind of the intent, is, like, let's get some things to where it's, like, actually the rest of the community can use it, within OpenTelemetry. Because right now, like, this is, like… It's like, it's like, you know, we appreciate having it, but no one can use it other than us.
CD SIG. And there's definitely, like, people that need to get that information that's not just us.
**Robert Pająk (Splunk Inc.)** 11:53 Yes.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:55 And it's self-maintained, and… Yeah, so, that's kind of, like, where we stand. That's… that's a new… thing that I wasn't expecting to have to do, but is gonna have to get done.
for, like, the wider folks to use it. I think in the interim, though, like, while they go make that decision and take that proposal forward, we can still, like, implement the ENV context and the PR dashboard thing, and that's not… that's not a big deal, because we still have the traces, it'll just be repointing where the traces go.
But in the interim, like, I can… I can give you access, to this, so you can, like, start to see those traces once they're there, like, flow through, and, like.
Take screenshots if you want. It's just not something that we can open up to everybody. Can really only open it to this group.
That's my update.
**Robert Pająk (Splunk Inc.)** 12:49 Yeah, for… For me, I'm just working with Alan on the presentation, and no more updates, other than that.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 12:57 Cool.
**Robert Pająk (Splunk Inc.)** 13:03 Okay, we can drop off here.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 13:06 Alright, sounds good. Carlos, welcome, did you have anything?
**Carlos Alberto Cortez** 13:10 No!
**Robert Pająk (Splunk Inc.)** 13:10 Cool.
**Carlos Alberto Cortez** 13:11 Slow week at one.
**Robert Pająk (Splunk Inc.)** 13:12 Have you drink now?
**Carlos Alberto Cortez** 13:13 Yeah.
What?
**Robert Pająk (Splunk Inc.)** 13:16 You have joined now, or you have been.
**Carlos Alberto Cortez** 13:19 Sorry.
**Robert Pająk (Splunk Inc.)** 13:20 For a while.
**Carlos Alberto Cortez** 13:22 Sorry, my internet collection is… Not very good today. What were you saying?
**Robert Pająk (Splunk Inc.)** 13:28 I was asking, when have you joined, because I have not realized that you have joined.
And they're wondering, how about you.
Okay, sorry.
**Carlos Alberto Cortez** 13:37 I mean, it's…
**Robert Pająk (Splunk Inc.)** 13:39 Normal.
**Carlos Alberto Cortez** 13:39 You were, like, in the middle of your explanation of open search, it's fine.
**Robert Pająk (Splunk Inc.)** 13:46 Okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 13:49 Alright, cool. Well, if there's nothing, it's good seeing y'all, and we'll keep you updated, And appreciate all your hard work. Have a good one.
**Carlos Alberto Cortez** 13:58 Yo…
