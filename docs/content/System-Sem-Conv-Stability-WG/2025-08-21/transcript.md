SIG: System Sem Conv Stability WG
Date: 2025-08-21
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Roger Coll** 02:02 Hello, hello.
**Braydon Kains** 02:04 Hello.
So I don't actually have any topics myself, because I've been on… in on-call hell, so… Not much… not much to say. I see there's one topic that we should talk about, though, right?
Yeah.
**Roger Coll** 02:45 I think I added a few days ago related to, I think, what we were discussing in In the CNTF as well.
… Right, that our initial goal was to… have a release candidate for KubeCon NA of this year, but I think it's October, or maybe November.
and… Yeah, probably what we can do is kind of have an overview of the GA board and see how feasible it is, because there's still… a few issues plugging GA, so….
**Braydon Kains** 03:26 Yeah. Let's get in.
**Pablo Baeyens** 03:31 Maybe one time sharing? Oh, okay.
**Roger Coll** 03:33 Oh.
Or….
**Braydon Kains** 03:41 I think it… it probably is a tall order for KubeCon. I know we were… we've been talking about that.
… I do think, like, after… after I finish a couple… a couple internal straggler tasks, I will actually have more time to dedicate to System SemConf, but I don't know if it will be… Enough.
To… Get us to this point.
**Pablo Baeyens** 04:12 Who'd we maybe… I don't know if that's going to be enough, but could we scope it down to a particular namespace? Like, is it… System namespace, or the process namespace closer?
**Braydon Kains** 04:24 Yeah, it's possible, like, I think… I think system and process.
I have… A pretty decent chance.
….
**Pablo Baeyens** 04:36 Maybe even just focus on one of those two, just to make sure we are able to….
**Braydon Kains** 04:42 Yeah, process is smaller, for sure.
**Roger Coll** 04:51 Hmm.
**Pablo Baeyens** 04:59 That's still meaningful, and that's still something we can… Can't talk about.
You could add to the filter on the top, where it says SystemCom GA blocker, you can also add label.
**Braydon Kains** 05:10 Interesting.
**Roger Coll** 05:13 This one.
No.
Requirements.
There's few open issues.
**Braydon Kains** 05:56 Oh, yeah.
Oh, I forgot about this one.
Huh, do I still agree with that?
Maybe.
**Roger Coll** 06:47 If it's the only… Left issue.
For the decision mate, maybe it's… Yeah, it's better if we just target, … For us, or that looks matched easily.
**Braydon Kains** 07:02 Yeah, I think if… if we… if we really focus on prog… pro… sorry, process.
**Roger Coll** 07:08 We actually, we probably could.
Yeah.
Let's see if we get documents.
Okay.
Not like most of them, I have a decision, so… What do you think? I… I think that for the whole system, it would be… Quite complex to target.
KubeCon, probably someone will be on vacations as well, in September, and….
**Pablo Baeyens** 08:31 Let's start with process on… See how far we get with system, if….
**Roger Coll** 08:36 Yeah.
**Braydon Kains** 08:37 Yeah.
That's fine, we can… we can… we can do that, I… A lot of the process stuff is blocked on me, so… when I can really dig into… to SEMCOM stuff, I will… I will focus in that area.
**Roger Coll** 08:53 Sounds good. We are.
**Pablo Baeyens** 08:56 On the ones that are blocked, is there any way to unblock them? Like, what are they blocked on?
Oh, okay.
I guess that is… Don't… Or maybe not.
**Roger Coll** 09:48 Okay, so this has moved to the entities.
part.
Right? And maybe it's not a problem anymore.
Having these required attributes here.
**Braydon Kains** 10:03 Oh, yeah, and I think, … Someone just opened… PRs that make process.executable entity.
**Roger Coll** 10:16 Okay.
**Braydon Kains** 10:17 And I proofed it, because I thought it seemed fine.
So….
**Dmitrii Anoshin** 10:22 Rayden, what is that? What does it mean?
Processing… okay, I see it.
And where is the automatic conventions? Okay.
**Braydon Kains** 10:32 Yeah.
**Dmitrii Anoshin** 10:32 I missed that one.
**Braydon Kains** 10:50 The only thing is that, like, I think… Probably the right way to model this with entities is that like, the process entity would have a HASA relationship with the executable entity, and I don't think there's a way to define that in SEMCOM right now.
**Dmitrii Anoshin** 11:05 What's the identifying attribute for this one? It has to be… when we define an entity, we need to define, like, a set of identifying and descriptive attributes.
But I don't see it here.
**Braydon Kains** 11:26 Oh yeah, this doesn't… … Is that what the attributes field is? Is that identifying?
**Dmitrii Anoshin** 11:35 No, there must be two separate sets of attributes. One of them is identifying set, and another one is descriptive set.
**Braydon Kains** 11:41 I just mean it in the schema, is that… in the YAML schema for entities is attributes, the name of the descriptive.
**Dmitrii Anoshin** 11:50 What was the identifying attribute for this particular entity in that case?
How would identify a particular process executable?
**Braydon Kains** 12:03 Anyway, that's… I don't know, to be honest, like….
**Dmitrii Anoshin** 12:07 Yeah, I'll take it to the entity secrets, probably.
It's something that… George allowed to be added, but we probably don't have Probability to distinguish between them, which is weird.
I will discuss later.
**Braydon Kains** 12:29 In this, at the very least, I think the build IDs are not all identified, because they're optional, so they're not all identifying attributes. The name and path, I think.
are identifying, because the intended uses… use of this process.executable entity is for, like, The process is running.
it's holding… A handle to an executable, and this is the description of that executable.
So it's not like the description of the file in the system, it's the description of The literal executable Held in memory by this process.
**Dmitrii Anoshin** 13:08 So, if you would model it, what would you say? Probably executable path would be identifying attribute in that case?
**Braydon Kains** 13:15 Yeah, I think… I think the… the… the path would be.
An identifying attribute.
**Dmitrii Anoshin** 13:21 Okay.
**Braydon Kains** 13:22 … If we would be more specific, it would probably be, like.
The file handle number, like, the file… or the descriptor… Or what's the word for that?
The descriptor number or something, but… I also don't know what the intention is for this.
… I don't know how useful it is to… like, I think this is for, like, CICD or something?
**Dmitrii Anoshin** 13:58 So I said, what?
**Braydon Kains** 14:01 I, I think this, these process.executable… attributes got added for something CICD related.
**Dmitrii Anoshin** 14:08 Oh, really? Okay.
**Braydon Kains** 14:09 And in… in that PR where they were added, I was… Saying that… like… Shouldn't these just be, like, file attributes?
The fact that a file happens to be an executable shouldn't really… Shouldn't really affect… Like, for a process executable attribute, it should be like, this is literally the executable being run by this active process right now.
And I don't know what that is used for at the moment.
**Roger Coll** 14:52 Which metrics would you provide for this process executable entity?
**Braydon Kains** 14:59 I think the… The way it would be modeled, it would be like… the process… Has an executable.
And then the metrics would all be attached to the process?
**Roger Coll** 15:13 I don't think there's any.
**Braydon Kains** 15:14 Metrics for the executable.
**Roger Coll** 15:17 And then why we need an entity for the executable?
**Dmitrii Anoshin** 15:21 Yeah, that's a good question.
**Braydon Kains** 15:22 So if the executable, if they could just be attributes on the process entity.
**Dmitrii Anoshin** 15:27 Right, right. That's the definition of… if we… we need an entity to be able to associate some signals with that. If we don't have signals, it doesn't make sense.
Much like quite an entity.
**Braydon Kains** 15:39 Okay, that's a good point. I think I'll revoke my approval.
**Dmitrii Anoshin** 15:43 Yeah, we need maybe some more context why this is being added.
**Roger Coll** 16:00 Alright.
Okay, this one was pulled off from another one, but it seems that it has been solved.
**Braydon Kains** 16:21 That got merged, okay.
I will get back to that, that blocked one then.
**Roger Coll** 16:26 Cool, thank you.
And the last one….
**Pablo Baeyens** 16:34 Yeah, I thought one is just, like, the….
**Braydon Kains** 16:37 Oh, the general, like, migration?
**Pablo Baeyens** 16:39 Yeah.
**Roger Coll** 16:40 Okay.
**Pablo Baeyens** 16:45 Okay.
**Roger Coll** 16:48 Okay, so let's… I will try also to focus and help with the… With the process, … Name a space, and it looks match.
physical life, I'd say, so… Okay, so I guess for this topic, we're done.
Pablo? I don't know, I just….
**Pablo Baeyens** 17:29 I was just curious if you discussed it in any way, because I saw some support went on Monday.
Go ahead.
**Roger Coll** 17:35 Yeah, basically, I thought a little bit about… that we are… And I changed, … Yeah, so basically we were… changing system.network.drop to system network packet.
Got dropped, but then we also saw, right, that we had… system.
network of packets as metric, and this is, not consistent, right, with the, … With uploaderization guidelines, and… So I think one way to make it, yeah, aligned with that would be to change the package To the actual packet namespace, and make it, like, a .count.
And that would, I would say, … Comply with that.
Dropped as well, as is a counter.
Then for the… also, one of the questions that we had, it was with the system.network.errors.
If you remember that we checked the slash proc slash net debt.
And basically, what I have seen in the Linux documentation is that It does not map, actually, to the… Back to the number of packets, but… Genetically to the errors in the interface.
So, probably, it should not land in that packet, namespace. I mean, we can keep it as… GenericSystem.network.errors in that interface.
**Braydon Kains** 19:24 Okay, I see. That's why I hadn't changed it here.
**Roger Coll** 19:29 Hmm… Mostly that's it, there's just… None.
**Braydon Kains** 19:39 Okay, I think that makes sense. Well, probably errors will need to change to error count, right? Because I think pluralization is… is generally discouraged for… even for, like, metric suffixes.
No.
If I remember correctly. Or maybe it was just for namespaces, maybe metric, maybe suffixes are fine. But I mean, if we already are gonna have packet.count, having error.count would be… Consistent.
**Dmitrii Anoshin** 20:08 X estimate?
**Roger Coll** 20:11 I guess we can Generic review from the… from the group.
Yeah, good.
All right.
Any other topic?
**Braydon Kains** 20:30 I have nothing else for today.
**Roger Coll** 20:36 I'm gonna be okay.
10 minutes back.
**Dmitrii Anoshin** 20:40 Thank you, folks.
**Braydon Kains** 20:41 Right, thank you.
**Roger Coll** 20:42 Have a good one.
