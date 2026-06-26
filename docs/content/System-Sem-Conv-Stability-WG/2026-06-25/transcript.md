SIG: System Sem Conv Stability WG
Date: 2026-06-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 03:39 Hello.
**Dmitrii Anoshin** 03:43 Hi, everyone.
**Pablo Baeyens** 04:00 I guess Raider will be attending. I'm not sure about the… Elastic people, probably not.
Well, Igor is in my team, while other people join, maybe we can… Say hi, also… I mean, he's here for… host ID, specifically, unlike host… Area stuff, but we can talk about it.
the general scope.
I guess.
Yeah, well, you know me, Igor.
Right now. Beautiful.
**Dmitrii Anoshin** 05:14 I agree.
**Igor Peschinskii** 05:14 Nice to meet you.
**Dmitrii Anoshin** 05:15 Just in a nutshell.
**Pablo Baeyens** 05:19 Yeah, so in terms of skull, the SIG is responsible for… the system namespace?
Process name phase and the host name phase, basically, on the semantic conventions.
So, that includes, system metrics, which you can… Let's see here… Process metrics… And then the host would be… Well, I think I already sent you that, like… Here.
Yeah, so the main goal… So far as being on… Stabilizing these conventions so that the… Implementers, mostly the host metrics receiver, can use them.
And, like, we can stabilize them.
Hey, Raider.
Maybe, Braden, you can tell us what you… talked about what LDTs on Monday?
You're muted.
Still muted.
Okay.
**Braydon Kains (Google)** 07:55 Alright, how about through here?
**Pablo Baeyens** 07:58 Yeah, we can hear you now.
**Braydon Kains (Google)** 07:59 Okay, stupid.
Google Meet unit, I press unmute, it doesn't unmute. It says it's unmuted, it's not unmuted. Anyways… So, at the entity meeting, the… we were talking about the main thing I talked about was making sure that the ISA relationship thing with entities still made sense, where we had that idea of, like, host ID was… whatever it was under, like, like an AWS ARN, or a GCE instance ID, or whatever, and then we would join that on some other entity, like a GCE instance entity that would have more specific information. It would… you'd join on the host ID, being the same as the instance ID.
Sounds like that part still makes sense, but… there's kind of a larger open question of the fact that we… there isn't really, like, a good default value we can give to host ID. We can't just say, like, under any circumstance.
this host ID is a good fallback.
like, there's not always Etsy machine ID to fall back on, there's not… Always… like, if you're just, like, a… like, a server under a desk, what are you gonna call your machine ID? Like, your MAC address, or… like, a combination of MAC address and host name, or something?
It's all kind of… Kinda screwy, and… This, with, like, resource detection in the collector, it's a bit weird, too, because… under the current model, the way you'd have to do it is you'd have, like, a generic host detector first, and then the AWS one would go and set host ID a specific way on the host entity, as well as giving its own So… all this to say is that I don't think I don't think we're off base, but entities might not necessarily be ready for… what we need to figure out, so we might need to… Be a bit more… Closely involved on that to try and solve the data model problem so that we can solve the host entity problem.
Did I… did I cover it properly, Dimitri, or do you remember anything differently there?
**Dmitrii Anoshin** 10:19 Yeah, that sounds right. I… I guess… from an entity perspective, we will have separate entities for AWS and for GCB, wherever, but the biggest problem is how we get host.id, and we… I don't think we're gonna change anything that is currently set in the semantic conventions. It's, like, it's okay for… from… NGT Sikh perspective.
to host ID to be set to wherever, whether it's a host machine ID, or if it can be set to… cloud… instance name, it's also fine, because that's what's currently set in the specification. We don't want to change that.
So, I don't… I don't think we are even blocked by some entities here. We just need to, like, let's say, formalize and stabilize an algorithm of how we set a host.ad.
Okay.
**Pablo Baeyens** 11:22 I think we need to… Yeah, I think we need to formalize the algorithm. I'm probably… I don't know if this is a good idea exactly, but, like, maybe require that a cloud provider attribute is set if the host ID is coming from, AWS.
some sort of information that allows you to understand what the host ID value is.
I don't know what that would look like exactly.
**Dmitrii Anoshin** 11:50 That's… that sounds good, and from entity's perspective, it's… it's gonna be, hey, there must be another entity associated with the resource.
if, like, it said to AWS ARN, whatever, the AWS instance has to be present, but it's… it doesn't require entities to be ready for that. We can just say for now, hey.
AWS ARM is supposed to be set as well, and it has to be the same value, essentially.
**Pablo Baeyens** 12:26 Okay, yeah, so we don't need to wait until entities figure things out, but we do need to figure out… Like, Formula Macs basically hosts the.
**Dmitrii Anoshin** 12:34 Exactly.
**Pablo Baeyens** 12:38 Okay.
Yeah, well, I mentioned this before you joined Breita, but Igor, is from my team, and he may be working on that exactly, on Q3.
**Braydon Kains (Google)** 12:48 Okay.
**Igor Peschinskii** 12:49 Yeah, hi.
**Braydon Kains (Google)** 12:52 Nice to meet you.
**Igor Peschinskii** 12:54 Nice to meet you.
**Pablo Baeyens** 12:55 Okay, we need to clarify this data model, but that's not a blocker.
Okay, the other topic I had, I don't know if people saw… Should probably have posted this on the public channel, sorry.
I tried to do, like, a map of what are the most interesting Attributes to stabilize based on how many metrics depend on them, basically use them.
And so, excluding the ones that are already released candidates.
The more interesting ones are system.device.
network interface name, and then the 3 that I put on the… The meeting notes, the ones from System Files System.
On… Yeah, so Braden said, the networking group is going to talk about network interface name.
Sister.
**Braydon Kains (Google)** 14:07 We will.
**Pablo Baeyens** 14:08 Okay.
And then system device, I think we also mentioned that last week, like, that's a bit more controversial.
But the other three… I wanted to take a look to see if we could… Bump the stability of those, Hold on, I guess I'll… Find a link to the… registry.
Fort these, Seamlessly.
I mean, I think… Maybe the table on system file system usage has all of them.
Do you think that concerns you have, Braden, about system.device?
Also affect the mount point?
In some way.
**Braydon Kains (Google)** 15:37 Whoa.
**Pablo Baeyens** 15:37 really understand.
**Braydon Kains (Google)** 15:39 the… the mount point… is… like, that's technically Linux… like a Linux word, calling something a mount point, but… like… File systems are also mounted on Windows, and they have… they are mounted at some spot, so, like, it's not… that weird.
mode is not necessarily a Windows thing, but I think that just means that on Windows metrics, we don't report it.
And that's probably fine.
And then… what was… what was the last attribute? There was mount point, mode, And…
**Pablo Baeyens** 16:20 On… Type.
**Braydon Kains (Google)** 16:23 Type.
That's also fine.
Yeah, I think… so I think… I think all three of them are fine. Mount Point, maybe, is a… maybe I'll… maybe I'll go digging through some, like, old Microsoft docs and stuff, and just, like, make sure that, like.
the word mount point isn't, like, totally antithetical to the way you refer to NTFS, usually. I don't think it is, I think it's… I think it's relatively normal.
and I'm pretty sure MountPoint is fine for all the Unix-based systems.
and then I don't know for, like, mainframes and, like, ZOS and stuff.
But pro… We don't have enough… People who know that stuff to… to…
**Pablo Baeyens** 17:12 Yeah.
**Braydon Kains (Google)** 17:18 So, I think I'm okay with Mount Point. Maybe after the meeting, I'll just quickly verify that it's not crazy to… Use that term.
In an NTFS context, And then as long as that's… true. Like, maybe… do you want to open an issue saying we could maybe stabilize these three attributes, and then I'll just comment on the issue, saying, I think it's fine.
**Pablo Baeyens** 17:45 Okay, yeah, I'll… I'll do that.
I guess we also have the chance of not necessarily stabilizing all of the possible values for the type if we don't want to. I don't really see a reason to do that.
But we.
**Braydon Kains (Google)** 18:05 Yeah.
I… I think… Are we defining file system type as, like, an enum right now?
**Pablo Baeyens** 18:15 Yes, it's like an open enum, so you can have… Here.
you have X spot, X4, FOD32, HFS+, NTFS, R-E-F-S.
**Braydon Kains (Google)** 18:36 As the following list of well-known values.
**Pablo Baeyens** 18:39 Yeah, so it's, like, open, if you want to use something that's not there, that's fine.
**Braydon Kains (Google)** 18:44 That isn't a weird… I actually just kind of hate enums and SEMCOM in general, they're kind of killing me.
like, the… the way we handled CPU.mode is still not my favorite, because the enum is different depending on the context you use it in.
And… and for, like, file system, it's like.
Is it even worth calling it in… enum, necessarily, like, we should… like, I guess it's just, like, we know certain file systems have this, like, common, like.
type, and if it applies, then you should use it, and I think that's…
**Pablo Baeyens** 19:20 Because enum is my… my way of calling this, but actually it's that. It's like a list of well-known values.
**Braydon Kains (Google)** 19:27 Yeah.
And I think those are probably fair to stabilize, like, I don't think… I don't think anyone's ever gonna change the way you refer to… Any of these… Any of these file systems.
**Pablo Baeyens** 19:42 Okay.
Okay, unless there are other opinions, I'll file the issue, and yeah, you can comment, Braden.
**Braydon Kains (Google)** 19:52 Yep, will do.
**Pablo Baeyens** 19:58 Okay, I guess we can move on to the… the PR is from the meter.
**Dmitrii Anoshin** 20:06 Yes, so my PRs are about… more than CPU.
attribute as opt-in, now given that it's possible with mdataGen.
And it's gonna be the first, metric when we… Apply this, like, opt-in capability to any attribute.
I guess that's what we already agreed on, and it's defined in semantic conventions, so I don't think there is… Should be any debate about that, please take a look at the PR. But the second PR is something that I think we should do, given that we're removing Information about how many cores you have.
And, by default, I mean not removing completely, but by default, how many cores you have in your machine. I think we need to enable, by default, logical count as a separate metric to, like, come to balance this kind of… like, to… so we provide to… Same inf… like, equivalent, way of representing data.
Let me know what they think.
**Braydon Kains (Google)** 21:22 I think the second PR, I agree.
For the first PR, should we make it opt out?
**Dmitrii Anoshin** 21:31 everything is opt-out, why would we need to make it opt-out? I guess we…
**Braydon Kains (Google)** 21:36 Well, opt-in implies that we're gonna start turning that attribute off by default. Yeah. Is that the case?
**Dmitrii Anoshin** 21:41 And that's what we have in semantic conventions.
And I think we discussed that a couple of times, and there are people submitting PRs, and I see a lot of, like, users actually just doing it with transform processor before we had this capability of reaggregation, so… Why, why would we need… Yeah.
**Braydon Kains (Google)** 22:02 it's just, it's a breaking change, kind of, I think? Yeah. It is gonna change the time series.
**Dmitrii Anoshin** 22:09 It is, yeah, it is breaking change, of course.
**Braydon Kains (Google)** 22:13 Okay, if we're okay with making a breaking change like that, that's fine.
**Pablo Baeyens** 22:18 Hi, I'.
**Dmitrii Anoshin** 22:18 I'm… I… Go ahead.
**Pablo Baeyens** 22:20 Yeah, like… We'll have to break people eventually. I would rather break people all at once, or maybe even… We could do it, like, per scraper or something.
But… I guess I'd… if this is not going to break a lot of people, I'd be okay with it, but I'm not… sure what day impact would be.
**Dmitrii Anoshin** 22:49 I think with this change, it's like, it's… Better to do it, like, gradually. Gradually moving towards semantic conventions, because there is one knob already available that you can turn back the previous behavior.
And first of all, it'll… Like, users will learn how to use that.
And, next time, it'll be easier for them, rather than have… I don't even know what other metrics we need to… what other attributes we would need to make as obtained, so… I don't know what we need to wait for.
**Pablo Baeyens** 23:28 Okay, I mean… In terms of reducing breakage.
I guess one thing we could do is… Add the system CPU logical count metric first.
And then make the change for… the… the other attribute to be opt-in on, like, the next version, or something like that, so that you have one version where you can Migrate without seeing breakage.
I don't know.
Maybe I'm overthinking this a bit.
I'm scared about breaking this component, because everybody… uses it.
**Dmitrii Anoshin** 24:10 I mean, we can do that, but I think at least they have to go side by side.
At least they have to be in one release.
But we can… we can also separate them if you want.
**Pablo Baeyens** 24:26 I want to… Think about it. I, like, I… I don't want us to do that.
And then not have any real advantage for users, like, if… If we're reducing breakage, then yes, but I… I don't know, I want to think about…
**Dmitrii Anoshin** 24:44 Yeah.
**Pablo Baeyens** 24:44 Whatever.
That would actually help.
**Dmitrii Anoshin** 24:58 Yeah, we… I guess we have to do that anyway, sooner or later, and probably better to do it before we… stabilize and have this feature gate for new matrix conventions, because it will be one less thing for users to Care about by default, right?
One last attribute.
**Pablo Baeyens** 25:28 Yeah, could we… Maybe pause that second one. I think… Like… Other people are going to be fine with adding a new metric, that's not… problem, but maybe… we put it on AutoCollector to, like, ask our people, like.
Are you concerned about this breaking change at all? I don't know, I… I want to be a bit cautious.
**Dmitrii Anoshin** 25:55 Yeah, I can post a message in the channel.
**Pablo Baeyens** 25:59 Okay.
**Braydon Kains (Google)** 26:09 There was something… in this… the PR that confused me, the… Where, the CPU frequency… attribute was added, but then that's the logical CPU number starting at 0, and then CPU.frequency is used in the metric instead of CPU.
**Dmitrii Anoshin** 26:31 Yeah, it's just to… It's just to make CPU frequency unaffected, because I… So this, attribute… Being optional.
It's, I'm applying it only to CPU.Time and CPU.utilization.
But I'm not sure if we need to apply it to the frequency. If you want to apply it to the frequency as well.
But it… no, it doesn't make sense for the frequency, I guess, because, like, why… why would you, like, take average of the whole course frequency?
But they can have separate… I don't know, if you think we can disable that for the frequency as well, we don't need that extra attribute. But that attribute is essentially the same, it's just different alias for the same attribute, because we cannot, in mdata Gen, we cannot… change attributes peer metric. They… they reference another attribute section.
So, and that attribute section defines whether attribute is able to… or enabled by default, so if we wanted by separate metrics, I had to split them, that's pretty much it. But it's only, like, it's an alias, it doesn't… make any difference.
**Braydon Kains (Google)** 27:53 Yeah, okay, I was… that was… very confusing to read on the YAML. I'm… I was very confused what was going on. I get it now. I understand.
**Dmitrii Anoshin** 28:02 If you think we can disable it from the frequency as well, it'll be cleaner.
I'm not sure about that. Let me know.
**Braydon Kains (Google)** 28:10 Yeah… I don't think there's any way… any reason to… Average Hertz across cores, basically, ever.
So, yeah, that… that's… that's tricky, I don't know how to handle it.
**Dmitrii Anoshin** 28:25 I guess this is…
**Braydon Kains (Google)** 28:26 The only way, really.
**Dmitrii Anoshin** 28:28 If someone enables frequency, they always get frequency per core, by default.
But do we think that same frequency across all the chords is, like.
Vast majority, and, like, even any violation of that, we can just ignore.
By ignoring, I mean ignoring by default. In that case, we reduced number of MTSs significantly for the majority of the users that have the same frequency over all the cores.
**Braydon Kains (Google)** 29:03 Yeah, good question.
Okay, I'll look into that, too, after the meeting. So I have two things to look… I have two action items going out of this.
**Dmitrii Anoshin** 29:14 Okay, thank you.
**Pablo Baeyens** 29:20 I think I'm going to add system file system state to the issue, because… tall.
**Braydon Kains (Google)** 29:26 The file system state.
**Pablo Baeyens** 29:29 Yeah, okay.
just because it… I think it makes more sense to consider all of them together. That one is also… Well-known values previously abused.
Don't think that. I mean, I'm… I don't know, like… I don't expect that to be different on Windows, but I don't really know.
**Braydon Kains (Google)** 29:52 Yeah, I don't… I don't know. The… I… I'll look into that at the same time.
**Pablo Baeyens** 30:03 Alright.
See you… Next week.
**Dmitrii Anoshin** 30:09 Thanks, Victor.
**Braydon Kains (Google)** 30:09 Thanks, everyone.
**Igor Peschinskii** 30:10 Yep.
**Pablo Baeyens** 30:11 Right?
