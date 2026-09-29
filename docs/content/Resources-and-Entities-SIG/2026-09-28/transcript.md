SIG: Resources and Entities SIG
Date: 2026-09-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 03:34 Hey, is my audio working?
**krajo (Grafana Labs)** 03:36 Is mine?
**Josh Suereth (Google LLC)** 03:39 Yep.
**krajo (Grafana Labs)** 03:43 first Zoom meeting back from location, so you never know.
**Josh Suereth (Google LLC)** 03:47 Good. Yeah.
I had a… last hotel meeting, my whole internet just crashed halfway through.
**krajo (Grafana Labs)** 03:58 Yeah, that sucks.
Don't you have a backup? Because… like, I'm contract… my contract requires me to have two ISPs, so I actually have a backup.
**Josh Suereth (Google LLC)** 04:10 Oh, I… I have a backup, which is to tether my cell phone.
Right. But like I wasn't ready with it, you know.
**krajo (Grafana Labs)** 04:19 Yeah.
**Josh Suereth (Google LLC)** 04:21 Okay.
Hmm.
**krajo (Grafana Labs)** 04:31 I should open that PR then. 5147.message.
**Josh Suereth (Google LLC)** 04:35 Yeah, I was going through all the, to-dos in it.
Yeah, we have a good bit to get through.
This one now has enough approvals we can merge it. I was gonna wait for Dimitri or at least one other to… Comment.
This is kind of the big… the big change, I think, is the fact that we remove I remove OTEL resource attributes from here.
And it is now only specified in Resource SDK. It is not specified as a configuration option.
Which I think some people called out.
Let's see… Okay, that one I think I'm going to resolve.
Daniel said he's gonna be a little bit late, so it might just be you and I for a little bit. I don't know if Dimitri can make it, he usually has a lot of work conflicts.
This is the one that I think we need to talk through, which the three of us can in a bit.
This one was, A knit about calling something.
Populates process entities are all relevant attributes of the entities. There's only one single entity today. I want to leave it generic in case we add them more, so that I don't have to change the specification if we add a new entity.
Hopefully that's reasonable. I'm going to mark that as resolved.
**krajo (Grafana Labs)** 06:31 So you want to keep entities, or…
**Josh Suereth (Google LLC)** 06:33 And yeah, I'm going to leave it plural.
So if it, like, the idea would be it's a set of entities, it could be 1, it could be 0.
whatever the entities are, you provide them, right? So if there's more than one, you provide more than one.
But I don't want to change the spec. This is like an English grammar thing.
Hey, Dan, there's, two open questions. One is from One is from you and one is from David. So just going through those on the PR to start with.
**Daniel Dyla (Dynatrace LLC)** 07:07 I have an open question.
**Josh Suereth (Google LLC)** 07:09 I think so.
**Daniel Dyla (Dynatrace LLC)** 07:11 I made a comment.
**Josh Suereth (Google LLC)** 07:12 Dimitri.
**Daniel Dyla (Dynatrace LLC)** 07:12 For other reviewers.
**Josh Suereth (Google LLC)** 07:14 You have a comment I need to probably figure out if it's okay, and then with, it's from Dimitri, actually.
From.
So this one, I just wanted to confirm before I just mark it as resolved, which is David wanted us to say that there's only one entity today for process, because there is only one, but I want to have it be plural in case there's more than one, because I consider it the set of all entities, which could be just one or more.
**Daniel Dyla (Dynatrace LLC)** 07:40 Is it… One or more? Like, isn't there only one process entity? Even if you detect.
**Josh Suereth (Google LLC)** 07:47 No, so this would be, this is basically populates process entities or all relevant attributes of the entity.
Kind of like we say, process service, service instance entities!
Umm.
This is more about the namespace.
I can change it, because I think for hosts, do I keep… yeah.
Oh, the problem is for all the other ones, there are more than one entity, so it's host and OS. I can change it, it's fine.
I see why everyone's complaining.
**Daniel Dyla (Dynatrace LLC)** 08:19 I mean, I don't think it matters that much, but, like, we have said you can only have one entity per type.
**Josh Suereth (Google LLC)** 08:26 Yeah, and there should be multiple… I want all the process namespace entities here. I'll just commit this, that's fine.
**Daniel Dyla (Dynatrace LLC)** 08:35 Like if we add process, I don't know.
**Josh Suereth (Google LLC)** 08:37 can.
**Daniel Dyla (Dynatrace LLC)** 08:38 And.
**Josh Suereth (Google LLC)** 08:38 If the process got something, we would actually change the spec, so…
**Daniel Dyla (Dynatrace LLC)** 08:41 Yeah, it's like a separate entity.
**Josh Suereth (Google LLC)** 08:43 Yeah. Okay.
This is the last one here about, having a plan for OTEL resource attributes and OTEL entities being together. What… what I did, as you saw, was there's a… I removed from configuration the description of this. It still exists in the spec, it's still required, everyone still needs to use it, it still doesn't change its importance within OTEL. It just removes it as a configuration option and leaves it as a resource propagation mechanism.
**Daniel Dyla (Dynatrace LLC)** 09:14 Yep.
**Josh Suereth (Google LLC)** 09:15 Yeah.
So, I saw that you commented on that and approved it. The PR is approved by a lot of, folks already, it's just I was waiting for Dimitri here.
**Daniel Dyla (Dynatrace LLC)** 09:28 Yeah, my comment was not meant to be, like, positive or negative, it was just informational for other reviewers. I found that table hard to, like, visually parse and figure out what actually changed, so…
**Josh Suereth (Google LLC)** 09:39 Yeah, this diff sucks. By the way, if you want to see what, if you do.
Let's source diff. If we switch to rich diff, it's a bit better.
**Daniel Dyla (Dynatrace LLC)** 09:48 It's a little better. You can still see the tables, but it's hard to say, like, did anything in the OTEL propagators line change?
**Josh Suereth (Google LLC)** 09:54 Oh, because it changed.
**Daniel Dyla (Dynatrace LLC)** 09:55 myself.
**Josh Suereth (Google LLC)** 09:55 you.
Yeah.
**Daniel Dyla (Dynatrace LLC)** 09:57 The whole table just gets replaced there. I went through it, and I don't think anything else changed, and if I'm wrong about that, let me know, but I think.
**Josh Suereth (Google LLC)** 10:05 No, it's, it's so weird because like OTEL SDK disabled didn't change, so why does it mark it as changed?
**Daniel Dyla (Dynatrace LLC)** 10:11 Yeah, it just marks the whole table as, like, one changed… thing. It's… it's just a diff view problem, but best I can tell, two of the rows changed, and then…
**Josh Suereth (Google LLC)** 10:21 Yep.
**Daniel Dyla (Dynatrace LLC)** 10:22 The spacing, like, all of the dashes, and, like, that all changed on every single row.
**Josh Suereth (Google LLC)** 10:28 Do you know why?
**Daniel Dyla (Dynatrace LLC)** 10:30 There's probably an auto formatter.
**Josh Suereth (Google LLC)** 10:32 There's an auto-formatted lint that I triggered that was very angry with me.
**Daniel Dyla (Dynatrace LLC)** 10:36 It's fine. I don't matter. It doesn't matter that much. It's just.
**Josh Suereth (Google LLC)** 10:40 That's probably why the whole table shows as a diff because of the the all the dashes had to change length.
**Daniel Dyla (Dynatrace LLC)** 10:45 Yeah, you can, if you go to the source diff, you can, like, ignore white space.
There's…
**Josh Suereth (Google LLC)** 10:51 White space, though, it's this space. Like, these spaces change length.
**Daniel Dyla (Dynatrace LLC)** 10:55 Yeah, but only on those rows. Like on most of the rows, there's not dashes on every single row.
**Josh Suereth (Google LLC)** 11:01 Yeah, oh, I see, so, like, this changed, but the one.
**Daniel Dyla (Dynatrace LLC)** 11:04 Yeah, like, if you… if you set it to remove whitespace, or to ignore… White space changes.
**Josh Suereth (Google LLC)** 11:12 Where's that? Here.
**Daniel Dyla (Dynatrace LLC)** 11:13 I think it's right there, yeah.
**Josh Suereth (Google LLC)** 11:15 I.
**Daniel Dyla (Dynatrace LLC)** 11:16 think… Yeah, I know. Yeah.
**Josh Suereth (Google LLC)** 11:19 work.
**Daniel Dyla (Dynatrace LLC)** 11:19 So…
**Josh Suereth (Google LLC)** 11:20 Yeah, there you go.
**Daniel Dyla (Dynatrace LLC)** 11:22 go.
**Josh Suereth (Google LLC)** 11:22 Don, that's it.
**Daniel Dyla (Dynatrace LLC)** 11:25 Oh, so I was actually wrong. I thought you removed OTEL resource attributes too, but you must not have.
**Josh Suereth (Google LLC)** 11:30 It's still… it's still there, yeah.
**Daniel Dyla (Dynatrace LLC)** 11:32 Yeah, so my comment's actually incorrect. I'll edit it.
Or if you… yeah.
**Josh Suereth (Google LLC)** 11:40 Resource attributes.
It's still there.
didn't… what? Because I remembered going back and forth on it. I think I might have removed it on an earlier one.
And I might have updated that since you looked. I didn't want to remove it from that stable.
That's… Honestly, I think it should be removed, because it's already in the other part of the spec, but if people are already used to seeing it here, you know what I mean?
**Daniel Dyla (Dynatrace LLC)** 12:13 Yep. Alright. I just edited my comment.
**Josh Suereth (Google LLC)** 12:15 Okay.
We'll leave it there for reviewers.
Cool.
And then I think this is the only other open one, of basically what's our plan for OTOL resource attributes and OTOL entities?
Right now, having them as separate controls means disabling is going to be confusing and kind of awkward.
So, this was specifically around the notion that we have an ENV detector that you have to configure, and this goes into some comments that Jack had around, the way configuration and default resource detection works. It's actually super awkward.
In practice.
**Daniel Dyla (Dynatrace LLC)** 13:01 Yeah.
**Josh Suereth (Google LLC)** 13:05 So this is where my thinking is, this is a separate… like, once this PR goes through, and we start updating resource detection, then I think we go through a round of, how do SDKs work in real-life practice, and go… because it's different across the SDKs, whether or not, configuration, like, takes precedence order over non-configuration, right?
**Daniel Dyla (Dynatrace LLC)** 13:31 Yeah.
**Josh Suereth (Google LLC)** 13:34 That's my thinking.
Okay.
**Daniel Dyla (Dynatrace LLC)** 13:40 As long as there is a way to control it, I'm just thinking, like, if… Yeah, it should be consistent among SDKs, but it might be difficult to walk some of that back.
**Josh Suereth (Google LLC)** 13:51 That's more what I'm afraid of, because I think what Dimitri wants is good.
And we should definitely push for it. But, what's proposed in the spec here is, I think, what is non-breaking.
Then we have to go through all the existing implementations and say, okay, we're going to be adding a specification that didn't exist before.
We have to do so in a way that stable SDKs don't break.
And so, it is a hodgepodge.
I know because I did the, like, TC review for, like, 2 or 3 of the SDKs, so… They're not the same. They're all up to spec, but they're not the same, because the spec was very loose.
Yeah.
**Daniel Dyla (Dynatrace LLC)** 14:38 Yeah, I think we'll have to audit all the SDKs and see what they're doing.
It may be a problem, it may not.
**Josh Suereth (Google LLC)** 14:46 Okay.
But in terms of the plan for how to get this on by default, I still think that should be, like, a default configuration option for SDKs, which we'll have to talk to the… the… config folk about, but I don't think, like… I don't think this becomes something that isn't controlled by config.
Right? Like, one of our goals, I just want to confirm, was that the order of these providers becomes a configuration thing that users have access to.
**Daniel Dyla (Dynatrace LLC)** 15:14 Yeah, yeah, I agree.
**Josh Suereth (Google LLC)** 15:16 I don't want to do shenanigans outside of that. Go ahead. Yeah.
**Daniel Dyla (Dynatrace LLC)** 15:19 I agree, and I think that, like, resource attributes and entities from the environment are just… separate… detectors, right? And the order that you configure them in will define their priority, but… is… what that default is, is maybe up for discussion, but I think it should work out just fine.
**krajo (Grafana Labs)** 15:43 Sorry, just one question. You said these are kind of resource detectors, but… They are both under ENV, right? For the environment variables.
**Josh Suereth (Google LLC)** 15:54 So actually, in the… only OTEL Entities is under ENV, because of the existing spec.
**Daniel Dyla (Dynatrace LLC)** 16:00 Yeah, so we didn't originally… Specify any resource detectors, including the environment. We just said, like, this environment variable is a blessed one.
I think some of the SDKs… implemented that as, like, a detector that's on by default, but I know that some did not. Like, OTELJS, for example, I know just had, like, a… during initialization, read from that variable, and that was that.
**Josh Suereth (Google LLC)** 16:31 So…
**Daniel Dyla (Dynatrace LLC)** 16:32 Fairly easy to walk back though and just make it an on by default detector, at least in JS.
That's an easy change to make.
**Josh Suereth (Google LLC)** 16:42 I… and I think if you read this… the wording of the spec here, right, the wording of the spec is just… you… you… the OTEL resource attribute detectors always last, effectively.
So if the user configured anything, it comes first, but we have a must, and we have that it's last. So we can either just leave this as is, and you can implement it as a resource detector that always comes last.
Or we can start backing off this spec a little bit, but I think too many people depend on it.
So I I I honestly think that this is one of those unmovable blocks in the spec of this has to stay. It's a must.
It talks about merging, and it talks about merging after all user-provided things, so we know that the entity ENV, if you specify it, would come first, then OTEL resources would be second, but it does mean OTEL resource for override entities, where it exists.
**Daniel Dyla (Dynatrace LLC)** 17:34 Yeah, I think that's fine. I would probably… If I had my way, just mark this as deprecated when Entities is available, and document, like, Entities is the way forward, and… But, like, I kind of want to… de-emphasize… Unassociated attributes as much as possible, at least in, like.
default normal configurations. Like, end users may put out things, like, I know that some people put, like, cost center tags and stuff like that, which, fine, I don't care that much.
**Josh Suereth (Google LLC)** 18:08 Those will those are part of an entity now.
**Daniel Dyla (Dynatrace LLC)** 18:10 Yeah, sure, like, I meant, like, you know, some… everybody will always think of something that we haven't… that we haven't specified yet.
**Josh Suereth (Google LLC)** 18:18 100%.
**krajo (Grafana Labs)** 18:19 I was going to, that's what I was going to say, that if you deprecate it, I'm sure somebody will try to add something because they have this special case where they can only put this into an environment of the pod and.
Whatever, so it's going to be very hard to deprecate.
**Daniel Dyla (Dynatrace LLC)** 18:33 well.
**krajo (Grafana Labs)** 18:33 building.
**Daniel Dyla (Dynatrace LLC)** 18:34 Yeah, I didn't mean deprecate in that way. I meant more like de-emphasize, like.
**krajo (Grafana Labs)** 18:38 Oh, yeah, I see.
**Daniel Dyla (Dynatrace LLC)** 18:39 Entities wherever possible, and even for custom stuff, I would argue you should be, like.
putting that in an entity of some kind. Like, if you're… if you have, like, owning team, then maybe you have, like, an ownership entity that… that you define in your company, or something like that. But for now, I think we have to keep it.
**krajo (Grafana Labs)** 18:57 Yep.
**Daniel Dyla (Dynatrace LLC)** 18:59 And possibly forever.
**Josh Suereth (Google LLC)** 19:03 Yeah.
Line 306… Okay, so I'm gonna do that.
Mark, this is resolved.
And then I think this is good to go.
Do you have any concerns if I merge this, Dan?
**Daniel Dyla (Dynatrace LLC)** 19:51 No.
**Josh Suereth (Google LLC)** 19:52 Okay.
Let's see if I can click the button.
Markdown link check? Oh man, an update. I'll update the branch and try to merge it later.
**Daniel Dyla (Dynatrace LLC)** 20:02 Yeah, the link check is probably just, like, a…
**Josh Suereth (Google LLC)** 20:05 It's, it's almost always…
**Daniel Dyla (Dynatrace LLC)** 20:07 It was the same.
**Josh Suereth (Google LLC)** 20:07 Stupid thing. Let's see.
It is… What do you think it is today? GitHub? I bet it's GitHub. No!
P. 1816 Teller.
Perfect, from server…
**Daniel Dyla (Dynatrace LLC)** 20:22 Forcibly close the connection. VLDB.
**Josh Suereth (Google LLC)** 20:26 You're trying to download a PDF, and we probably tried to download it a bajillion times in the spec repo.
Not a good idea. I know that…
**Daniel Dyla (Dynatrace LLC)** 20:35 The late checker actually downloads the whole thing? I would think that it would just, after the… Headers come…
**Josh Suereth (Google LLC)** 20:43 It does a head request, which is just supposed to return okay, but some really lazy web servers don't do that.
Yeah, so no, it's not supposed to… it's not supposed to download the link at all. It issues, what's the HTTP request? It's HEAD, right?
**Daniel Dyla (Dynatrace LLC)** 20:59 Yeah.
**Josh Suereth (Google LLC)** 21:00 Yeah, it, like, it only is supposed to issue head requests, but it could be that they, this is lazy, so they, literally have a, like, a deny rule on all PDFs, that you can't hit them at all, even for head requests, which… I understand blocking a GET request, I don't understand blocking a HEAD.
**Daniel Dyla (Dynatrace LLC)** 21:16 Well, they might, but it's been working. So I'll bet it it says network error. My guess is it's just an overloaded server.
**Josh Suereth (Google LLC)** 21:23 Okay.
Everybody likes VLDB.
I don't even know what that's from, honestly, in the spec. Like, where does that one come from?
**Daniel Dyla (Dynatrace LLC)** 21:32 I don't know.
**Josh Suereth (Google LLC)** 21:35 Yeah, we can also add that to an excluded list eventually. All right.
Oh, here it comes from Colimer Encoding.
**Daniel Dyla (Dynatrace LLC)** 21:48 From columnar encoding, yeah. It's probably Josh McDonald adding like.
a bunch of references for why columnar encoding is better, because VLDB is, if I remember right, like, very large databases.
**Josh Suereth (Google LLC)** 22:02 Yes.
**Daniel Dyla (Dynatrace LLC)** 22:03 I think it's… yeah.
**Josh Suereth (Google LLC)** 22:05 They are. Okay, so this is good to merge.
**Daniel Dyla (Dynatrace LLC)** 22:09 Yeah, I think so.
**Josh Suereth (Google LLC)** 22:10 Alright, so next… next steps in terms of… this is around the, like, state of the project.
I have, like, two big things I think are next steps. One is one I think we need to handle a little bit sooner rather than later, which is around contextual identity. Let me grab… the PR from… I think it's still open in the proto repo, but I got closed elsewhere from Dimitri. Do you remember this, PR? The… here.
Share this tab.
I'll put it in the notes so you can click along.
**Daniel Dyla (Dynatrace LLC)** 22:49 Yeah.
**Josh Suereth (Google LLC)** 22:50 For this one? Yeah.
**Daniel Dyla (Dynatrace LLC)** 22:52 Well, I remember its existence. I don't know that I ever dug too deeply into this.
**Josh Suereth (Google LLC)** 22:57 This one's pretty interesting of, basically inside of entity. Let me expand it a little bit.
So, a new field on Entity Ref, again, it doesn't break Entity Ref, it just adds to it.
Actually, hold on, is it on the SDREF?
**Daniel Dyla (Dynatrace LLC)** 23:14 Yeah, it is.
**Josh Suereth (Google LLC)** 23:15 Yeah, because that… it's the white space pane, yeah.
**Daniel Dyla (Dynatrace LLC)** 23:17 Yeah.
**Josh Suereth (Google LLC)** 23:18 Amen.
**Daniel Dyla (Dynatrace LLC)** 23:19 Moves the end bracket and adds an end bracket and a new line, and it just renders weird.
**Josh Suereth (Google LLC)** 23:25 Yeah, hide white space. Are you gonna work.
**Daniel Dyla (Dynatrace LLC)** 23:27 I don't think that's gonna work on this one.
**Josh Suereth (Google LLC)** 23:30 did!
**Daniel Dyla (Dynatrace LLC)** 23:30 Oh, you know, okay.
**Josh Suereth (Google LLC)** 23:31 Look at that. Why not turn that on all the time now? Okay. Anyway, yeah, so this adds the ID context type so that you basically, if you're like a host and you're inside of Kubernetes, you can say the host references Kubernetes.
As its, like, outer, you know, thing that gives it unique identity.
What I don't like about this is I don't know if the arrows are the right way for how instrumentation works.
**Daniel Dyla (Dynatrace LLC)** 24:06 Yeah, I, hmm.
I… so it seems like this is trying to establish, like.
an owner of the identity, right? Or, like, a… If you have two identities, or two entities that conflict, which one is correct?
It's trying to… to establish.
**Josh Suereth (Google LLC)** 24:33 No, this is more the issue of, like, I, so… There are environments that you can run in where you can't get a unique ID.
So, so there's, there's two problems going on.
**Daniel Dyla (Dynatrace LLC)** 24:45 Oh, I see. Local unique ID should contain the type of the context.
**Josh Suereth (Google LLC)** 24:49 Yeah, so, like, when I am, when I'm a host, right, I might have, like, an IP address or a MAC address that I use to say, oh, this is me, I know that my MAC address isn't gonna, like, change.
And you can use it as a kind of identity.
Cool.
But what if I have two Nick cards? You know, which one is my identity?
**Daniel Dyla (Dynatrace LLC)** 25:09 Yeah.
**Josh Suereth (Google LLC)** 25:10 That sort of thing. So, with hosts, they actually went through a bunch of review around a host identity, and they couldn't pick one that was relatively generic.
**Daniel Dyla (Dynatrace LLC)** 25:19 Yeah, because you could technically have the same host ID across, like, two different data centers. Yeah, I getcha.
**Josh Suereth (Google LLC)** 25:26 So then what they decided was, what we decided, Host is always locally unique. So there's something that gives it its uniqueness.
So if I am running, like if in my, I have a Kubernetes cluster in my basement now because it was really easy to set up.
And, if I'm… Talking about anything there, IP address is fine for identity. I don't need anything more. The Prometheus instance that I use to, like, manage all of it, I just use host detection. I don't put anything else in it. I don't need to identify what Kubernetes cluster, because there's only one.
You know? So, in terms of, like, entities I have, my identity is small and localized. If I'm inside of a cloud where it becomes confusing, there's something above me that has the additional context to make me unique.
And that was a decision we made around entities early on, this, like, local versus unique identity. So, we want… This, this one is basically to work In many, many systems.
And I think just for the whole thing to function, we need to be able to construct actual, like, UUIDs that are reusable. And so where we have one of these situations where, like, the identity isn't known.
By the, by the thing. So, like.
a process That's running, knows its process ID, It might know a host ID, but it doesn't know that it's in Kubernetes or something. Maybe it does, maybe it doesn't.
**Daniel Dyla (Dynatrace LLC)** 26:59 You could have this… you could have PID1 and, like, 25 different processes on a machine pretty easily.
**Josh Suereth (Google LLC)** 27:05 Right. And so then who identifies it is is this that's what the local context is is the thing that gives you global uniqueness. And so you can have a layer of these.
**Daniel Dyla (Dynatrace LLC)** 27:15 So, is the context… What you're reading from, like, the context type would be, like, process in that case?
**Josh Suereth (Google LLC)** 27:22 So, so for… it goes the opposite way. So, so the proposal that Dimitri has is the host would say, I'm part of a Kubernetes cluster.
And that's my identity. And then the Kubernetes cluster can say, I'm part of a cloud, and that's part of my identity. And then your unique identity would be what cloud you're in, right? What cluster ID you have, and then what host you are.
**Daniel Dyla (Dynatrace LLC)** 27:44 absolutely.
**Josh Suereth (Google LLC)** 27:45 Entity would be the chain.
**Daniel Dyla (Dynatrace LLC)** 27:46 You may not always be able to determine that, right?
**Josh Suereth (Google LLC)** 27:51 Right. Craig, one second. I'm gonna list the, the, so the two.
**Daniel Dyla (Dynatrace LLC)** 27:56 Oh, yeah, I'm sorry, Krao, I've been just talking right over the…
**Josh Suereth (Google LLC)** 27:59 you might not be able to determine that, and then the second issue is we have this notion, the reason why we don't just make a UUID, because we could, in process, just synthesize a UUID.
It's relatively unique, no one else is gonna have it, we're the only ones that know about it, we can just use that UUID everywhere, right? The reason we don't do that is for the multi-observer problem, and the push-pull problem with Kubernetes. So Kubernetes uses the identity of what port you own.
Okay, and your IP address for, like, some of its service discovery? That's a good way to get a process ID.
Like, uniquely, because only one process is gonna own that port, generally, theoretically, that you're getting data from.
That's not great for OpenTelemetry push, though, because when we push, it could be one of, like, 20 ports.
So it's not, like, if you use the port IP address identity.
That works for pull, it doesn't work for push. And since we have multi-observer pattern, where we want the identity to be the same, regardless of if you pull or push.
Right? That's what makes things a little awkward. You can't just synthesize a UUID and push it out everywhere. You need to let people independently pull from you, and we also can observe entities from multiple systems. So, like, if I'm on… if I'm running VMware.
And I have a Kubernetes cluster inside of that, or Proxmox or something, right? I might be able to hit Proxmox and ask questions about a VM. I might be able to hit Kubernetes and ask questions about nodes, and I might be able to hit the hosts itself and ask questions. And I want to be able to resolve that these are all about the same thing.
**Daniel Dyla (Dynatrace LLC)** 29:31 Yeah.
**Josh Suereth (Google LLC)** 29:32 And so that's the multi-observer problem combined with context is where this is. So Krajo, I wanna hear what you have to say.
**krajo (Grafana Labs)** 29:39 Yeah, I'm just a little bit weirded out by this ID context type, because… Sure, I can set this to post or cluster or whatever, but without something actually providing That… Oh.
Part of the identity, you know, what is the host, what is the cluster.
It doesn't mean anything, it's not going to make the thing… You know, more identifying.
So I'm not… like, I don't really see the value of this at the moment, but again, I'm just back from vacation, so I'm trying to catch up.
**Josh Suereth (Google LLC)** 30:16 I want to point the arrow the other way. So, like.
Instead of this ID context type.
Being the way it is now.
I don't know what I would call it, but imagine if this was types of identities that I Might have underneath me.
Right? So, if I'm a… if I'm a Keats cluster.
I could say, I am an IT context host, for… host entities. If I'm a host entity, I can say, I'm an ID context for process entities.
Right? Meaning, like, processes are part of a host, hosts are part of a cluster.
So, if I see both the Kate's cluster and the host together, I know that I compare them to make the unique identity, but the arrow comes from the Kate's side, not from the host's side.
Right? So me, as a host, I don't need to know who provides that outer context.
But wherever… sorry, my cat really wants attention. But whoever owns the, the cluster, whatever, that resource detector would say, when I do resource detection for Kubernetes, I will provide this ID that says, you know, I… I, as a cluster, can have hosts.
And I will provide context for that host to let you know how… where it's unique within, right?
**Daniel Dyla (Dynatrace LLC)** 31:39 Yeah, that seems.
**Josh Suereth (Google LLC)** 31:41 Good.
**Daniel Dyla (Dynatrace LLC)** 31:42 That assumes you can only have one type of.
Like, thing underneath you.
**Josh Suereth (Google LLC)** 31:49 Yeah, unless we make it repeated. And I'm not super happy about making it repeated, but yeah.
**Daniel Dyla (Dynatrace LLC)** 31:56 I mean, I can't immediately think of something of a case where that's not true, but like.
Can we say that it's definitely not true? I get, you know.
I don't have enough expertise in that area, but that's a limitation that I can immediately see. If you point at your parent, you're definitely only going to have one parent.
Or one parent type.
But you may have multiple types of children, just makes it easier, but it's easier to detect your children with like more certainty.
**Josh Suereth (Google LLC)** 32:30 It goes into… I think this is in the specification.
Where do we have this?
**krajo (Grafana Labs)** 32:37 By the way, I mean, right now, if you don't have this, then, you know, you have your resource detectors, and basically from the… types, you would Be able to kind of guess what's under what, like, and how to navigate it, because… If I read cluster and host, I know that host It's probably in the cluster. So if you want to formalize it.
And because resource detectors, I assume, You would put, cluster detector afterwards. So yeah, I think I'm more.
you know, agreeing with Josh on this, that the direction is the other way around. It doesn't make much sense to Point out of a context to something that's unknowable.
**Daniel Dyla (Dynatrace LLC)** 33:30 There's also… potential, like… Gaps.
If you say… You know, my I am a cluster, I have hosts.
And then somebody doesn't enable a host detector for whatever reason, but has a process detector. There's a broken link there where you cannot say these processes are like a part of this cluster.
Yep. If we, you know, maybe we just shrug and say, enable your host detector, but it is a potential gap in either scenario.
**Josh Suereth (Google LLC)** 34:12 Yeah, I think the reason why Dimitri's going for the way that he's going is this particular decision we made on relationship, general relationships for entities, is that when you're making the… when… when you're… Creating that event stream of, like, here's the relationships between entities.
You are always… we're recommending that you prefer the shorter lifespan or higher churn rate entity.
So that we minimize how often you have to spend relationship events, right?
The problem we have is, at one point, we were trying to keep the entities in resource and the relationships completely disjoint. So relationships come down a separate stream, right?
What we're realizing as we implement these systems and, like, go to town on them is There are… like, we want to get a unique identity for an entity.
That involves its contextual, like, identity context, if you will.
And having that inside of the resource is useful. I'll give you an example.
OpenTelemetry has a service namespace, okay?
Where we have this notion of service name, service namespace, service instance. That forms an entity triplet that is completely unique.
Okay? Like, your service is something that you define as a user. You say, cool, I want to put a boundary around the service. It has nothing really to do with the architecture. And those… that triplet makes a unique identity you can use, which we rely on for a lot of our Prometheus translations, right? Because service name, service instance ID become Prometheus job and instance labels, right? Cool.
That's wonderful, but now I have host in there as well, and I have Kubernetes cluster, and I have process, right, as entities in resource. And those form their own separate line.
And they're the same, right? Like, one is the same as the other, but they're, like, different views of identity.
And so, I think that's partly what we're teasing out here, is this, like, you know, if we were to be minimalists in OTEL, resource would have nothing besides service, and then all the other stuff would come out the entity signal to say, oh yeah, by the way, this service instance ID has a relationship to this process on this host on this node, you know what I mean?
But that's not how things work in the real world. Our database is now Are more optimized at having big, wide tables and that sort of thing.
So people want all this in the resource as well.
And now we have this, this, this conflict of identity in resource.
**krajo (Grafana Labs)** 36:57 Yeah, not to mention that we… we were promised that we don't need to use the async events, if you… if that's what you meant.
**Josh Suereth (Google LLC)** 37:04 Yes. Yeah. You you shouldn't have to use that because we can do the drum in Oto. Right.
**krajo (Grafana Labs)** 37:08 Yeah, but I do need a way to implement that left-hand navigation somehow, and, you know, there's two problems there.
One for the, what do I display, and the other is this, like, what's the order of things?
And we can just build, like, some, you know, database of our own, and say that we know that cluster is, host is inside cluster, but You know, if we could get it… In the data, that would be nice as well.
**Josh Suereth (Google LLC)** 37:35 Yeah, everyone has built that mapping, by the way, themselves.
Based on, like, what OTIL does.
So that's… that's the thing that I think, like.
The ecosystem is kind of done.
**krajo (Grafana Labs)** 37:51 Okay, but then, okay, then do you have to actually solve this if everybody already has this, and you just slap in your entities and detect them?
**Josh Suereth (Google LLC)** 38:01 It's hard coded and inconsistent. That's the reason I want to solve it. So two things. One is if I have a particular open telemetry signal.
can I make a, like, a string that represents this is the same as this other thing? Right now, we're forcing people to do, like, a ginormous amount of key-value pair diffs. Right? And so one of the ideas behind Entities was we wanted to have an ID where you can say, this is indeed truly the same as this other thing.
Now we have this notion of, at least for the way I describe service versus, like, hosts.
Entities ID is you have a logical ID, and you have a physical ID.
Right? And they might be different.
**krajo (Grafana Labs)** 38:42 Right, but still, this doesn't have anything to do with what's inside what and the context.
**Josh Suereth (Google LLC)** 38:49 That is the problem of the physical ID, right.
But the what's inside what in the context is, the ability for us to make these IDs of, like, here's the physical ID, here's the.
the logical ID, here's the ID for whatever purpose, and that the thing you're looking at goes down the tree in all three of those areas. Yeah, you're right, maybe we don't need to solve this, but… I have this… this back-of-my-mind suspicion we do, given Dimitri's tried to solve it, and given some of the bugs that I've seen, kind of, or questions people have asked about entities, right? Like, around relationships. I think the only relationship we'd want to encode in OTLP Would be this identity one, so you can follow it easily.
**krajo (Grafana Labs)** 39:39 Yeah, that would be nice for sure. Again, we don't, we wouldn't have to like in Grafana, we have this knowledge graph and that knows these things, but like.
**Josh Suereth (Google LLC)** 39:46 Yeah.
**krajo (Grafana Labs)** 39:47 If we could get it from the model, that would be nice, obviously.
**Josh Suereth (Google LLC)** 39:50 Right, and the knowledge graph is also something, like, we have, what, our asset inventory, which I think is the same as your knowledge graph on GCP?
And, yeah, like, that… that, we need the ability to, like, fill that out and flesh it out, but the… Anyway, there's model mapping going on, there's all sorts of fun. I think I exhausted that discussion topic. I do need to.
I think… I think I need to call it here for myself, because I'm late for another meeting, but let me check… I think that's the discussion I wanted to have, basically, and I don't think we're ready for… more right now. I think…
**Daniel Dyla (Dynatrace LLC)** 40:41 We want Dimitri too.
**Josh Suereth (Google LLC)** 40:42 We don't have Dimitri, right? So what I think… The next steps for both of these are somewhat related. So contextual identity, I think the question we'll have is, do we need this?
And what problem… Are we tackling… You should crisp it up.
Cool.
**Daniel Dyla (Dynatrace LLC)** 41:01 Like, hard, examples of, like, this doesn't work and would work if we had this would be great.
**Josh Suereth (Google LLC)** 41:11 Yeah, I… so I'll work on that for next time. I think with this PR merging, then the other thing we should do is keep working on our.
our actual prototypes and get them actually submitted. So I'm hoping…
**Daniel Dyla (Dynatrace LLC)** 41:24 Prototype match the latest spec, too.
**Josh Suereth (Google LLC)** 41:28 Cool.
And thank you for cleaning up the spec. I think your rewording is a lot better than what it was. So I'm excited.
**Daniel Dyla (Dynatrace LLC)** 41:35 I like it.
**Josh Suereth (Google LLC)** 41:36 Yeah.
All right. I will see you all in about a week. Thanks everybody.
**Daniel Dyla (Dynatrace LLC)** 41:40 See you then.
