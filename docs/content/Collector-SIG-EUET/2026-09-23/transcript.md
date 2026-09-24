SIG: Collector SIG (EU/ET)
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jade Guiton** 00:49 Boom.
**Vojta Vojacek (SolarWinds Worldwide, LLC)** 00:55 Hey.
**Pablo Baeyens** 02:02 Hello!
**Andrzej Stencel** 02:04 Hello.
Pablo, one thing I noticed, there's, the batch processor is not in the list of high-priority components, right? Because we, I suppose, we want to deprecate it.
So, the… the approach… These users should be using… batching in exporters for V1.
This is what we got.
**Pablo Baeyens** 02:40 Yes.
That is the goal, yeah.
I guess we could start with that topic. I feel it's, like, part of the high priority issues.
So, it's… George McDonald has been the one mostly working on this, and I mean, there's other people on the call that are working on it as well, so… I guess… interrupt me if I say something wrong, but, the idea is that For most use cases.
People would just rely on the exporter helper batching instead of the batch processor.
The batching on the exporter would be enabled by default.
So… In most cases, people wouldn't have to do anything to hot budget. It would just work.
Now for the cases where people want to use batching earlier in the pipeline for some reason. The QBatch processor Would be the replacement, or… the batch processor on those cases.
Yeah, the exposure helper patching is… While most… At feature parity with the patch processor.
So, you can do… Whatever you… Were doing before.
Yeah, I mean, the RFC goes into more detail, but one thing I like is that Because you… know what exporter you are in. You can tweak the way batching works for that exporter specifically. Like, maybe the intake limits are different, or maybe you want to batch based on different payload format, you can do it after… Using exporter helper button.
**Andrzej Stencel** 04:41 Right, yeah, so to, like, check off that point I added to discuss, I think… I think I have my answers now. I was confused initially, because the batch processor README doesn't mention the migration or anything. I think maybe we should add something to the batch processor dock, right?
**Pablo Baeyens** 05:00 Yes, I think so. So, One of the next steps on the phase we are currently in is writing a blog post.
about this, to announce it, I think it makes sense to also update the documentation to mention it as At the same time, I think Dimitri and Joshua McDonald are working on the blog posts.
Okay.
**Andrzej Stencel** 05:27 Cool.
**Jade Guiton** 05:28 I think the gist is that it's not officially deprecated yet, so… Don't want to cause too much panic in advance.
**Pablo Baeyens** 05:36 Right, yeah, everybody uses the batch processor, so it needs to be careful.
**Andrzej Stencel** 05:42 The question came from somebody internally at Elastic, preparing some docs or tutorials and asking whether they should even be mentioning batch processor, or just skip it altogether.
**Jade Guiton** 05:58 Yeah, the more forward-thinking way would be to… Mentioned the exporter helper batching.
Only caveat is that we don't really have a replacement for the cases outside… for batching, outside the exporter yet.
Although, actually, it got merged, I think, right? The Quebec processor?
**Andrzej Stencel** 06:17 It is, it is at the developer stage.
**Jade Guiton** 06:21 Okay, yeah, it just doesn't have the telemetry yet, but yeah.
Okay, so yeah, it makes more sense to… to work on that. Is that the thread on the OpenTelemetry channel?
I forget.
By Lisa Jung, or is that a different person writing a tutorial?
**Andrzej Stencel** 06:41 I think it's a different thing, that was, where I came from was an internal elastic, Okay That's… You mean the OpenTelemetry channel? I can… can you link the chat to the thread?
**Jade Guiton** 06:59 Yeah, sorry, it's in the Otak Collector.
**Andrzej Stencel** 07:02 Okay.
**Jade Guiton** 07:03 I, pinged Josh on it,
**Andrzej Stencel** 07:07 Oh, actually, I think this is it.
**Jade Guiton** 07:09 Oh, okay.
**Andrzej Stencel** 07:10 International Beginner's JavaScript series. Yeah, maybe I mixed things up. I think this was a question I got.
Thanks, Rob.
**Pablo Baeyens** 07:21 Yeah, and in terms of the… the current thing that… is happening with the botch migration. There's… this draft BR, that… If you want the details, I think Jade is going to be able to speak to it much.
more concretely than I can. I… Thank you.
somebody wants to help, the best would be to reach out to… to Joshua McDonald, to JMFD.
**Jade Guiton** 08:01 Yeah, right now, there's still work ongoing to, implement the same telemetry that the exporter helper has in the QBAT processor.
Problem is, like… It's kind of a big project, because the exposure helper telemetry was never meant to be used in a processor.
Oh, it's all named after Exporter.
**Pablo Baeyens** 08:21 Right, because the QVatch processor is basically a wrapper over the exporter helper.
**Jade Guiton** 08:26 Yeah.
**Andrzej Stencel** 08:30 I think with the internal metrics from the collector, I think I have a… I'm not sure if this is a similar problem with metrics.
reported by an internal library like Stanza.
those metrics, like, in the scope of the library, and not of the component that uses the library. So we have, for example, two different components using Stanza.
I'm not sure if there's even, in the name of the metric, there's no way to get the component name, right? Like, you would expect receiver underscore file log underscore something, but you get stanza something, or something completely different.
**Jade Guiton** 09:10 I think, this is part of what the… Scope attributes were supposed to solve.
I don't remember if it's enabled by default for metrics, Now… I think it's for Matrix, it's still under FutureGate.
But if you enable that feature gate, you can get scope attributes that describe which components the telemetry is from, regardless of what instrumentation library emitted it.
Right. The problem is you need something that handles scope attributes.
**Andrzej Stencel** 09:38 Yeah, sure, scope attributes are good enough, I suppose.
It's the metric names, I suppose, that we won't be able to get to, but… I guess that's fine.
**Jade Guiton** 09:50 Yeah, I'm not… yeah, I'm not sure it would be a good idea to… rename… The metric name emitted by an instrumentation library in the first place, because it might have a semantic convention associated with it.
**Andrzej Stencel** 10:03 Yeah, yeah, yeah.
Okay, cool, thanks.
**Pablo Baeyens** 10:18 Okay, I… I will add up topics instead there's… No… Nothing written down right now. So I have a few PRs, and Alex has a few more, to enable keep-alives by default, on different components.
We are… Trying to do that to be able to… get configured HTTP to be, one point something, so… on a… I'll appreciate our review if you're a code owner of one of those, let me get a link. If there's no reply, we will merge them soonish.
Yeah, Mikola?
**Mikołaj Świątek** 11:09 So… We are… in the end, we are doing the breaking change, because dropping those deprecated fields in ConfigHCP is a breaking change.
**Pablo Baeyens** 11:20 I am supportive of making a breaking change, yes. Yep.
**Mikołaj Świątek** 11:23 Okay, like, it's fine with me either way, but I recall that Dmitry was against it, so we should get his approval on, like…
**Pablo Baeyens** 11:33 Yep, the…
**Mikołaj Świątek** 11:34 Or at least let them know.
**Pablo Baeyens** 11:36 That makes sense, yeah. I want to first get to a point where we can actually remove the fields if we want to.
**Mikołaj Świątek** 11:45 Yeah, please do it in Contrib, right?
**Pablo Baeyens** 11:48 Siri?
**Mikołaj Świątek** 11:49 What I meant was at least do it in Contrib, right? Because we…
**Pablo Baeyens** 11:53 Yeah, yeah, yeah, that's it.
**Mikołaj Świątek** 11:54 Right? But we don't control any other users of Config.HCP out in the wild, right?
**Pablo Baeyens** 12:01 Right.
Yeah, so I want to do it in Contrape first, and then… like… will… will ask Dimitri, but I feel like it should be fine? I don't know.
We'll see. So yeah, the PARs are linked on this issue from Mikolaj, Yeah, we will… Vers them in the next couple of days if there's no reply, so please take a look.
And I guess if there's no other topics, I'll mention one more thing.
We are a graduated project now, OpenTelemetry as a whole, so, we have a video at KubeCon North America.
For about 1 minute. That gets shown, well.
As part of the keynotes and in other places.
in KubeCon. So if you're a maintainer, and you are interested on appearing on the video, I mean, you can reach out to me, or there's a message on Auto Maintainers.
About that. It would be something like… 5 seconds, or 10 seconds, so it's not… Not a lot of effort, but it needs to be, done within The next couple of days, because the due date for the video is… I think next Monday.
Yep, thanks for the link.
She, any other topics?
**Anitha Vadla** 14:53 Hi, I'm Anitha. I'm sharing one PR in the chat.
That needs attention from reviewer, like, if you can give some inputs on that.
-Oh.
**Palash Kulkarni** 15:13 Oh, I see, so it's, it's regarding, the… the exporter.
Bug, right, Anitha?
If you could check out a bit more so that it would be helpful for us to understand.
**Anitha Vadla** 15:31 Yeah, so, in sending… in exporter, in… under sending queue, component, there is, small, like, there is something called MaxEdge, if… If any record is more than that max size, all the records after that particular oversized record is getting dropped.
I made a small change where, Only the max size… the record which is more than max size will be dropped, and all other records will be pushed to the downstream.
-Oh.
Yeah.
That's, a small summary of… about that up here.
**Pablo Baeyens** 16:16 So, I think this is… Israel, didn't you have a PR about this?
Maybe it got closed?
**Israel Blancas** 16:28 Let me check… Because I think, yeah, there was something.
**Pablo Baeyens** 16:40 Yeah, phone it. I think it's this one, it got closed.
I… Is this the same thing? Sorry, I… Don't know if it is.
**Anitha Vadla** 17:09 I'm sharing beer again in the chat.
Let me look at… look into the PR, which you have shared.
**Israel Blancas** 17:25 Yeah, I think… I think it's the Sakuten.
**Anitha Vadla** 17:30 Yeah.
**Pablo Baeyens** 17:31 There was some open discussion on the one from Israel with J Mathie, did never got a reply from him.
But I feel like we need to resolve that discussion before we… merge something… Related to this, I… I don't know his relative would be willing to… comment on the PRO, Anitha, on… maybe I can take care of, like, getting JMUCD2.
To look into this again.
Cool.
**Anitha Vadla** 18:25 Yep.
**Srikanth Pathlavath** 18:27 Hi, everyone. Hi, everyone.
these Srikanth. So, recently, like, Yeah, I was working on, Postgres receiver. So, in Postgres Receiver, like, we have a hotel semantic convention feature gate. So, when I turn on that, like, I have a setup of, like, one RTS instance, which has more than 30 logical databases in it. So… I… after turning on that feature gate, like, immediately CPU is spiking, like, I just, Ran the Collector in a, to, two vCPUs, instance. So, like, one core, it's almost, like, taking 50% of the CPU utilization immediately after turning on the feature gate. So, for that, I have made a small fix, actually. So, like, I'll share that PR.
So, yeah, I need your thoughts, actually. I think I got one approval, so still, I'm waiting for… I think Dimitri also commented on that, so I have addressed all those comments.
**Pablo Baeyens** 20:05 Yeah, I think we just need to wait for Dimitri to reply here, just… Since you replied yesterday, let's give him a bit more time.
**Srikanth Pathlavath** 20:16 Yup.
**Pablo Baeyens** 21:06 Anything else?
Alright, I think we can call it a day.
Thank you, Rhardy.
**Evan Bradley** 21:31 That one.
**Israel Blancas** 21:32 You're on.
**Vojta Vojacek (SolarWinds Worldwide, LLC)** 21:33 Bye.
