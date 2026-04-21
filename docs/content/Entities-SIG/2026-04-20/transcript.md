SIG: Entities SIG
Date: 2026-04-20
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 04:08 Hey! Sorry I'm a little late.
**Dmitrii Anoshin** 04:13 Hi, Josh.
Probably not.
**Josh Suereth** 04:14 How are you doing?
**Dmitrii Anoshin** 04:16 Doing well.
I would… I would like to ask Josh if we can move this call 30 minutes late. What do you think?
**Josh Suereth** 04:27 I am totally fine with that, honestly. Like, I really struggle with this time. I think we proposed it, and no one complained.
And it's just not a great time. And then, we… the fact that all of us struggled to make it this time, I think is… yeah, 30 minutes later's fine.
Anyone, anyone have complaints with that?
Okay.
Cool.
Do you… do you want to kick us off then, Dimitri? I will actually go change the meeting right now, but I can't, drive and do that at the same time, but I will find it different to do it, so… Okay.
**Dmitrii Anoshin** 05:10 Yeah, from my side, I just wanted to close the loop on the PR that I've been, dealing with, and, yeah, I think it's ready to merge. I added a couple of examples how it will interact with, service entities, like, service entities relationships to process specifically, because it's kind of an entry point when you can join them together, and then process would be part of the whole infrastructure, topology, and service is Part of, application kind of side of things, right?
So I added that. That example kind of seemed critical. Otherwise, I think it should be good to go.
**Josh Suereth** 05:57 Yeah, I think I… So one thing I was looking for was at least one more approval. We have enough to merge, but if you can fix the conflicts, that'd be ideal.
**Dmitrii Anoshin** 06:07 Oh, really? I have a comp… sorry, I…
**Josh Suereth** 06:09 Yeah, no, it's, it's new. I think, the.
**Dmitrii Anoshin** 06:13 Okay, here's cool.
**Josh Suereth** 06:14 The release got cut, and every time the release cuts, there's a changelog.
**Dmitrii Anoshin** 06:18 Yeah, I'm doing quite… yeah, I'm doing it right now.
**Josh Suereth** 06:21 Okay. Let's see… I'm just in my calendar still, so I'm a bit distracted. Were there any… there's still open comments, too, those all have to be resolved?
But are there any open comments that are relevant?
**Dmitrii Anoshin** 06:34 No, I don't think so, I think we closed all of… like… there is a decision made on all of the comments. They're just, like, kind of left open, because I was maybe waiting for… feedback on them, but given the time passed, I think I just called them.
**Josh Suereth** 07:02 Alright, yeah, this is… The right calendar… alright, so… we're moving our meeting to 1230. Do you still want it to be an hour? I think so.
This and following events… Whooping.
Excuse me, I'm happy.
work.
It's good.
Cool.
In other news, because I think we only have two major PRs right now, we have this one, and then we have the merge one.
And the merge one… But it looks like that's trying to release now. Right.
**Daniel Dyla (Dynatrace)** 07:40 The entity merge PR, I think merged.
**Josh Suereth** 07:44 Did it finally merge?
**Daniel Dyla (Dynatrace)** 07:45 I think so. I was looking this morning, because I was working on the SDK startup, not last week, but the week before.
and realized that I had duplicated some stuff that you were doing, so that's why I don't have a PR open. I actually do have a branch pushed, but I was waiting for that to merge so I could rebase and push mine, so I'll do that after the meeting today.
**Josh Suereth** 08:09 That's awesome. Yeah, I spent… I spent this morning trying to fix this up, get rid of, some conflicts and fix things. Let me… let me walk you through real quick what I changed, based on… on feedback, because it was… it was all minor. So, first of all, before the I had current entity being the one that was higher priority than the new entity, but right now I just… it was confusing everyone, so now the new entity is the one that has priority, because that's how we implemented it everywhere. Just in the example, that was confusing some folks.
Let's see… the other thing was, in Merge Resources.
**Daniel Dyla (Dynatrace)** 08:48 So, we changed the priority order, we… we…
**Josh Suereth** 08:52 Minimal.
**Daniel Dyla (Dynatrace)** 08:53 merge algorithm?
**Josh Suereth** 08:54 No, no, no, no, no, just the example.
**Daniel Dyla (Dynatrace)** 08:58 Oh, I gotcha, okay.
**Josh Suereth** 08:59 Yeah, just in this example of current and new, new is the one that's higher priority. In the example before, current was the one that was higher priority, and that was confusing everyone.
And I looked in our implementations, no one implemented it that way anyway. That was… They always put the higher party on the right, so I was like, okay, fine, we'll do that.
**Daniel Dyla (Dynatrace)** 09:15 Yeah, I gotcha, okay. So higher pri- just in the literal pseudocode function block, or whatever, okay.
**Josh Suereth** 09:22 Yeah, sorry, I'm not presenting the thing I'm looking at. This right here.
Just this. Yeah, it was just this. Like, before.
No, that's KenMerged. Before, this had, basically, it would only insert into the new entry… it would only insert new entry if current entry didn't have it, and that was confusing people, of like, oh, well, which one's higher priority? Like, okay, fine. New entry's the higher priority one, it's always gonna override the insert.
Great.
**Daniel Dyla (Dynatrace)** 09:49 Okay.
**Josh Suereth** 09:50 That was it. The descriptions of how it works, all the same.
Okay, the other thing I did, and this was for, like, Daniel, this is something that you had, we said.
I put a note that priority with entity merging is generally chosen implicitly by user configuration. For example, the order of resource detectors configuring the SDK, implicitly create an order of priority for merging entities. The proposal that you had for, like, how we deal with async and all that, I think belongs in the SDK specification itself.
So I'd actually like to take this snippet you had exactly and put it in the SDK.
**Daniel Dyla (Dynatrace)** 10:26 That's good, because I copied it exactly for my PR. This was part of the work that I thought I was duplicating from you. Okay.
Yeah, so I do have that wording.
**Josh Suereth** 10:37 Beautiful. Yeah, I think… I think, like, your comment was right on, but I think it belongs in the SDK side, so I put this note here to make sure that people understand how… because that was the other confusion, was like, everyone asked, where does… where does the priority come from?
cool.
I think there was also, like, just as an aside, there was a confusion on one of the entity… one of the examples, I forget which one it was, but basically all I did was add a second… yeah, there's this one here.
So, if you have a conflict where someone's using loose attributes and entities, and there's a conflict with the loose attributes, so, like, the host ID of the loose attribute conflicts with this, and you merge, you would keep the entity that doesn't have a conflict and get rid of the one that does. There was confusion that we didn't show keeping an entity, even though… Implicitly, it's in the rules, so… We added it to the example.
Cool.
Anyway, you're working on the SDK spec, which is awesome, because I was just rebooting my SDK implementation to try to get some prototypes out, so that's… that's beautiful. That goes into the next… Next steps.
**Daniel Dyla (Dynatrace)** 11:51 Yeah, I'll open the PR, for… or, yeah, I'll rebase and open the PR. It looks like I'm actually quite a few… commits behind, but none of them should have affected it, other than yours. But I had duplicated some of what you had, so to avoid confusion, I'll… I'll remove the duplicate and then push.
Yeah, and we can talk about it.
Next week, probably, if that's okay?
**Josh Suereth** 12:21 Yeah, that's fine, that's fine. If you… if you have a preview of it, and you want, like, if you think it's ready for me to start implementing an SDK prototype against, I would be happy, because we have all the prototypes we've built so far, we built so many. I'd be happy to start, refreshing them against what you have so far, so that we can… Yeah, for sure. …a bit quicker.
Cool.
All right. We don't have anything else on the agenda, but I do think we need to go through our backlog and do next steps.
**Dmitrii Anoshin** 12:49 Congo.
**Josh Suereth** 12:49 But, yeah.
**Dmitrii Anoshin** 12:50 Bring one more PR for OPAMP, from OPAMP spec. It's interesting, given that we mentioned SDK. I'll just, Posted here… Okay, yeah, BMPR is here. It's like, just FYI, there is a spec that proposed how to… set an identity for OpAMP, tech service.
And yeah, it's… originally, it was, like, let's take the whole resource from SDK and make it an identity, because in our pump.
In a PAM protocol, there is only one set of identifying attributes and one set of non-identifying attributes. There's no way to put several entities, essentially.
And yeah, I guess, I was suggesting let's just put service identifying attributes as a set of identities, and everything else, all the other identities attached through the detectors on anything will be non-identifying attributes, and I think that's the way to go. But if you have some other ideas, thoughts, feel free to comment there.
**Josh Suereth** 14:02 I… I don't have any other things. I absolutely agree with what you're suggesting here, and that's… that's what I… what I think needs to happen.
**Dmitrii Anoshin** 14:08 Okay. And I think our Tigran on board, so it's… it's gonna… this pair are gonna change then.
**Josh Suereth** 14:15 Cool.
Anyone have any topics they want to discuss first?
**Daniel Dyla (Dynatrace)** 14:27 Last week, Michele joined and had a question about, When, like, different telemetry observers disagree on the identifying attributes.
He said he was gonna open an issue. Did anybody see that issue, or… I never went back to look for it.
**Josh Suereth** 14:50 I have, an AI automated thing that gives me all the feed from OpenTelemetry every day, and I didn't see it pop up in there. Let me… Let's… let me just open a thing right now to take a look. Would it be in the specification, you think?
**Daniel Dyla (Dynatrace)** 15:06 Yeah, that's… he asked where to do it, and I told him the specification, but I'm looking at… Issues… yeah, here we go. Entities information from dash zero on how we solved some merging issues without entities like system. 52… er, 502.1.
**Josh Suereth** 15:23 Yeah, I got it, thank you.
Do not merge conflicting namespaces or sub-namespaces… wait, this is about how to resolve where people disagree on… the ID.
But different significant details because different SDKs predict different processes. Okay, do not merge conflicting namespaces or sub-namespaces. If resource R1, at least similar contains a key… dot with the value A, another resource contains the same.
Yeah, but this is… okay, we… This is what the entity merge algorithm does, effectively.
**Daniel Dyla (Dynatrace)** 15:59 Yeah, this is… it looks like he's…
**Josh Suereth** 16:02 reimplementing it.
**Daniel Dyla (Dynatrace)** 16:03 advice here more than asking a question. Definitely, he had a question in the meeting.
**Josh Suereth** 16:10 Yeah, I mean, so this is, like, again, this is one of the motivating problems that led to the entity merge algorithm. So it's good to confirm that, like, the merge that we just submitted actually solves a real problem, because what he's doing here is reinventing entities with namespaces, or sub-namespaces. Okay.
Uncertainty principle, this is interesting. If resource… hash R1 of a piece of telemetry contains no key from the namespace, and resource R2 and R3 with the same dasho resource ID contain conflicting values for the namespace. We should treat… R1 as either The entire… values of R1, or from R2, but not mixed. I don't understand what.
**Daniel Dyla (Dynatrace)** 16:51 You can't merge… you can't merge two attributes of the same type, I think, as the… Like, you have to choose one or the other, is the way that I'm reading this.
**Josh Suereth** 17:00 Oh, which… don't… don't we do that in our merger?
**Daniel Dyla (Dynatrace)** 17:04 Right, because I think namespace… When he uses the word namespace, you can substitute type, like, entity type.
**Josh Suereth** 17:11 Yeah, it's like host, or process, or whatever.
**Daniel Dyla (Dynatrace)** 17:14 Yeah, so R1 does not have a key that… from some type. R2 and R3 both have it, but they're conflicting values.
**Josh Suereth** 17:25 Yeah, okay, okay.
So, so again, our entity merge algorithm would, would kind of solve this if we.
**Daniel Dyla (Dynatrace)** 17:32 Well, we solve it by saying, not allowed. You can't have two entities of the same type.
**Josh Suereth** 17:37 Yes.
Any of the known ones, very sort.
**Daniel Dyla (Dynatrace)** 17:42 But I guess… Yeah, there are some questions…
**Josh Suereth** 17:46 don't know.
**Daniel Dyla (Dynatrace)** 17:47 He had a question about what if you detect an entity in your SDK, and you send it off to some external, like, a collector or something like that.
that is also detecting the entity externally, and one or the other, like, the ID attributes disagree, because, you know, one of them has a more accurate view of your system or something like that.
Like, maybe your SDK is sandboxed and doesn't know that it's running in some sort of container.
Yeah. I told him… that, If they're the same entity type, you essentially are going to have to choose a winner, but that ideally, they would not be the same entity type at all.
or, you know, that they're viewed as separate entities. You can't have… if the IDs differ, they are different entities by definition.
**Josh Suereth** 18:42 Yes.
**Daniel Dyla (Dynatrace)** 18:43 And that answer was what prompted him I think to… like, write this whole issue. So, either it didn't work for him, or he… yeah, I don't know. Because this Rule 1, it sounds like a rule that we already have encoded.
**Josh Suereth** 19:00 I think the main problem that we'll have to address is, you know how we have the local identity with the telescope?
**Daniel Dyla (Dynatrace)** 19:08 Yeah.
**Josh Suereth** 19:09 Yeah, that… that's the thing we have to figure out over time.
Like, that… Yeah.
**Daniel Dyla (Dynatrace)** 19:15 I mean, that's kind of omitted from, I think, the data model stuff right now, right?
**Josh Suereth** 19:20 Right, because we, we actually don't… we haven't encoded, like, how we want that to be exactly. You know how we… like, if two entities show up in a resource together, this is, like, one of our open questions. If two entities show up in a resource together, we know there's a relation between them.
But we haven't defined what it is.
**Daniel Dyla (Dynatrace)** 19:42 Yeah.
**Josh Suereth** 19:44 That… that is the thing I think we probably need to work on next, but I do think we need to get to prototyping, where entities show up in resource, where we have the merge algorithm and the conflicts, because my guess is, and we'll keep reading through this issue, my guess is it comes down to, the higher order problems that show up from that issue.
Right? Like, making sure that, like, you don't overwrite host.name when host.id is… is different.
or the same, you know? Like, you have to agree on host ID and name being the same, that kind of thing. Great. Like, we… that's… that's something we can… we can figure out. But, if this goes into, like, the more complicated things… let's read this, because I think this might be related, right?
A conflict in telemetry namespace.
implies a conflict in process namespace, right? That's… that's the kind of relationship we're talking about here, like, how one entity might impact another.
Because there's some sort of implicit relationship.
The SDK implements Temtree SDK attributes out of the box, but not all implement process. The lack of support for process in the SDK would cause leaking of process attributes from another SDK.
What does leaking mean?
**Daniel Dyla (Dynatrace)** 21:02 I think… Said we assume the process contains…
**Josh Suereth** 21:10 To prevent the leak in the process. I don't know what this means.
**Daniel Dyla (Dynatrace)** 21:13 I think he's saying you can't distinguish between… two different processes.
But I'm not sure. Like, if you have… Yeah, I don't… actually, I don't know.
**Josh Suereth** 21:35 Maybe, maybe we'll have to bring him back and talk to him again. So the… I mean.
Here's the thing, if you have different telemetry SDKs, but the same process, it means you have two SDKs running in that same process that are of different languages.
**Dmitrii Anoshin** 21:54 And why is this a problem, given that we have separate entities?
can…
**Daniel Dyla (Dynatrace)** 22:00 They're the same type.
**Josh Suereth** 22:02 That you'd have… you'd have two separate resources, and we're actually going to keep the resources separate. We're going to say, cool, here's the Java resource, and here's the, you know, C++ resource, or the native re… maybe a better one would be Python. Here's the Python resource, and here's the Rust resource, right?
Because I'm using Python, but I have, some embedded, you know, Language in there.
I don't… I kind of don't understand, like, again, how do you get two different SDKs in the same process?
Or is this foot about that?
**Daniel Dyla (Dynatrace)** 22:40 Well, two SDKs in the same process is totally possible. Two SDKs in the same resource is not.
**Josh Suereth** 22:49 Two SDKs are the same process with the same language. The telemetry SDK namespace, if you look at it, it's just what SDK language I am and what version of that language am I using.
practically.
I guess you could have two instances of two different versions if you're very careful in some languages, but in most languages, that'd be really frickin' hard to do.
Yeah, I'm not… I'm not sure what he's trying to get at here. Let's read the next one quick.
Subordination to container and Kate's container. A conflict in the container namespace or the Kate's container namespace implies a conflict in telemetry namespace. Kate's container and process namespace. That is, if we know it's a different container, we know it cannot be the same process, and thus the same… Oh, oh, okay, this is just the hierarchy order. So this, this does, the subordinate state thing, this is what I kind of expected.
The subordinate thing is kind of the relationship hierarchy, right?
If the container's… since the container owns process, and the process runs on a container, I know that if the container's different, I don't have to look at anything else. I know they're different entities, or I know they're different resources.
Right? I don't have to look at the rest of the identity. I just… I know that container's gone.
So, yeah, like, so I have a container that's running two processes.
Right?
if I get data from process 1 and from process 2, I would first check container and say, cool, they're from the same container. Then I check the process ID identity and say, okay, cool, you know, they're from the same… they're from different processes, they're different.
I think what he's saying here is if I see that the container is actually different, so I have a container 1 and container 2 running 2 processes, I don't have to look at the process ID, I know because the container ID is different that they're actually different entities. That just sort of, again, makes sense in the entity world.
**Daniel Dyla (Dynatrace)** 24:53 Yeah, this is the global ID. You can have… he's looking at this from the perspective of, I have a bunch of telemetry already dumped into a backend. It's not like the SDK collection and processing pipeline. He's like, I queried a bunch of data. Some of them have the same process ID, but that does not necessarily mean they were the same process, because they're in different… Posts, or whatever.
It's the global ID versus local ID that we talked about a long time ago, but I believe is not… encoded anywhere. Maybe it's in the OTEP, I think, but it's not in any spec.
**Josh Suereth** 25:30 We probably need to add that to the spec. It is kind of in the spec, I'll show you where it shows up.
**Daniel Dyla (Dynatrace)** 25:36 It might be in the data model.
**Josh Suereth** 25:37 It is in the data model spec. We also talk about telescoping and resource.
Okay.
But I think this is all the same, it's basically he's saying there is a… like, how the global ID works. Like, if I have… if OS is different, that means that these have to be different, so I only have to look at that to figure it out.
Subordinate to system. Conflict in system namespace implies all the other ones have conflicts.
Okay.
Depressed case, depressed… yeah… Well, I'm gonna… I'm gonna put this in one of our to-sort things.
in Phase 1, but… I'm gonna churn on this a little bit more. Let me… let me show you guys… I think we do have some of our local ID stuff in the specification, but we do probably need to expand on it, so there's probably a to-do here.
Inside of resource, We talk about telescoping here.
That doesn't specifically call out, like, the local ID bit.
However… I think in the data model.
Right here, we talk about how it's minimally sufficient.
**Daniel Dyla (Dynatrace)** 27:22 That's… that's for a single… and, like, choosing attributes for a single ID, though.
**Josh Suereth** 27:27 Yeah.
We did mention about it being in some context, but we didn't really talk about local IDs, did we? Versus global IDs. Where's the context bit?
It's just been able to… Yeah, interesting.
I think we do need to add that, add more information. Like, we talk about what telescoping is, but we don't actually talk about how This works.
So… I bet.
**Dmitrii Anoshin** 28:10 I can work on that. I've been thinking more about that, and… It's so…
**Josh Suereth** 28:15 Awesome. Do you want a new task for that, or do you want me to assign you the one, here? We'll go over here.
**Dmitrii Anoshin** 28:22 Probably take a new task, create a new task.
**Josh Suereth** 28:25 Okay.
an item… And the… Local.
versus universal.
ID, D2C entity.
data modeling.
Document… okay.
**Dmitrii Anoshin** 28:45 Because it doesn't necessarily mean that that issue will be resolved by this.
**Josh Suereth** 28:51 Yep.
Why is it doing this to me? Okay, cool.
**Daniel Dyla (Dynatrace)** 29:00 It's because these are the issue templates that are set on the spec. You're gonna have to do, yeah, blank or resource.
**Josh Suereth** 29:07 Yep.
By the way, our, OTEP, the document from Splunk is dead now? It got deleted.
I don't know if you guys saw this, so we actually lost a bit of our writing. We do have to do more writing to get things more written down, so I think this is, timely.
**Dmitrii Anoshin** 29:27 code that I… those that I wrote, right?
**Josh Suereth** 29:30 The ones that you wrote and the ones that Tigrin wrote. Actually, the ones that Tigrin and I co-wrote, like, I literally edited the document, I had edit access to it and all, and it's just gone. Like…
**Daniel Dyla (Dynatrace)** 29:39 Wait, what happened?
**Josh Suereth** 29:41 Splunk got rid of… not… well, Cisco doesn't have a Google account, and so after so many years of not having a Google account, the documents are all deleted.
**Daniel Dyla (Dynatrace)** 29:51 the Google… the Google Docs, not…
**Josh Suereth** 29:53 drive down.
**Daniel Dyla (Dynatrace)** 29:54 Yeah.
**Josh Suereth** 29:55 But some of the stuff we had was only in those docs, not in GitHub, and wasn't owned by the governance committee, so we need to take that lesson to heart and kind of fix that.
Yep. Okay, describe the difference between… Using the local ID entities.
Versus requiring… Every C2 would be universally unique.
specification.
describes.
Telescoping… the data model.
It's not described.
this aspect of entities, right? So it's… I don't see the field with it. Okay.
Cool, and then I can assign it to… come on.
Dimitri… I can give it a label of… What's… do we still have triage accepted?
maybe accepted ready with sponsor, I think, is actually what we want.
And… what else do I have to do? Entities… Okay.
So we don't kick off the automation. This is a task.
MCG's Phase 1, cool.
Alright.
But we're here, should we move on to going through next steps?
**Daniel Dyla (Dynatrace)** 31:31 Sure.
**Josh Suereth** 31:33 Wait.
In progress. Generate entity configuration interface for metric scrapers. Do you want to talk through anything there, Dimitri?
**Dmitrii Anoshin** 31:49 Yeah, actually, this is merged, and kubernetes Cluster Receiver now, the first component in the collector that emits entities within the resource, and I haven't… Hear any complaints, or…
**Josh Suereth** 32:03 That's awesome.
**Dmitrii Anoshin** 32:04 Yeah, I think this one can be closed, actually.
**Josh Suereth** 32:07 the whole thing. Do you want me to close it now? It's in the collector, I guess.
**Dmitrii Anoshin** 32:11 I'll take care of it based off here.
**Josh Suereth** 32:13 Okay.
Alright, here's another one in the collector. Add support for new resource entity references in the proto-message.
I think this one… if you're already emitting them, aren't you done, or you're still tracking stuff?
**Dmitrii Anoshin** 32:27 to do references… No, it's good. Like, there are some of the things that needs to be added to the different companies, so it's, like, an overarching issue.
**Josh Suereth** 32:38 Yeah, yeah, that's cool. It's amazing to see how much progress this has made so far, though. Lots of… Lots of little things. Alright, Entity SDK Prototype, we're gonna leave that one. I'm gonna eventually close that and open a new one.
Entity merge logic prevents fine-grained detectors. This is about the Go SDK.
Cool. I think… Daniel, if you're working on the SDK specification, this is one where, unless we have a Go developer step up, this… I probably will have time to get to this shortly. We're starting to get the, the hard parts of, Semconv Weaver stuff done, so I have more time to implement, starting probably within, like, a week or two.
**Daniel Dyla (Dynatrace)** 33:25 This is where you have a detector that only detects, like, one attribute.
**Josh Suereth** 33:31 Yep. Where's the example?
Does it… does it show this? Yeah, so basically, like, in Go.
there's this thing called, like, a host ID provider.
And all it returns, that's the thing that gets the host ID. Where's the detector?
The host ID detector takes detect and literally just provides the host ID with a schema URL. That's it.
**Daniel Dyla (Dynatrace)** 33:59 Okay.
**Josh Suereth** 34:01 So, this is where we were talking about for Go, inside of resource would be, like, returning partial entities.
And we would collapse to either a complete entity or a incomplete entity.
like, specially in the Go. Like, Go would actually understand this from all these different sub-detectors to not break existing users. However.
I'm actually still tracking, this might become moot. If you look at config.
Let me… actually, here, we'll do it over here.
if we've seen… is it… do you remember if it's… is it called configuration specification, or is it, like, OpenTelementary config?
We'll just search.
**Daniel Dyla (Dynatrace)** 34:42 I think it's OpenTelemetry Configuration.
**Josh Suereth** 34:46 configuration.
Come on, come on.
I want to search for a repo. I don't want… okay, fine, we'll do it this way.
Repositories.
**Daniel Dyla (Dynatrace)** 35:05 It's just OpenTelemetry-configuration.
**Josh Suereth** 35:08 Yep. You guys see what I'm presenting?
**Daniel Dyla (Dynatrace)** 35:11 Yep.
**Josh Suereth** 35:12 So, if we look at the actual schemas, general documentation for schemas, organize for human. So, if we look at types inside of here, there is a resource detector.
Resource, detectors.
So, there's this notion, experimental resource detection, interesting.
We'll have to go through these eventually, but I believe… Yeah.
There's an experimental resource detector thing where you basically specify, I want to detect container, host, process, and service, generically, right?
And you're specifying what detectors are there.
These line up with entities 100%.
So, when Go supports this, we could basically say, cool, whatever Go is doing for the config side.
We make that thing entity-friendly, and we might be able to ignore the programmatic thing for now, and still kind of be okay, assuming people start moving to config-based.
That's… that's one of my… one of the things I've been thinking about.
I don't know if that's, too aggressive or breaking, but yeah.
Cool. And then these experimental detector things are basically.
**Daniel Dyla (Dynatrace)** 36:46 Yeah, cuz… I see what you're saying. So if they enable one of these… It implies, you know, maybe 2 or 3 fine-grained detectors that have to be somehow grouped together anyways.
**Josh Suereth** 37:00 Yep.
**Daniel Dyla (Dynatrace)** 37:01 And the grouping is the same grouping that we have.
**Josh Suereth** 37:05 Yep.
**Daniel Dyla (Dynatrace)** 37:05 Yeah, okay.
**Josh Suereth** 37:06 And we just make this new thing provide the entity, and, you know, if they have fine-grained detectors, great, they can keep them and keep them backwards compatible, but you're effectively not really going to use them going forward.
Okay.
**Daniel Dyla (Dynatrace)** 37:23 Do they have to be backwards compatible? I mean, the entity detectors… Are entirely different than the resource detectors.
And… If you detect a resource attribute.
We've already decided, like, that that essentially throws away… entity information. Like, if you just throw on a raw resource attribute.
You're kind of on your own.
**Josh Suereth** 37:51 Yeah, so here's another way to phrase it. Existing Go developers that write manual configuration are using those fine-grained things.
And so, how do they move to entities without it being a breaking change?
So, my thinking is… they already… they already need to do something to move to config. And config is a much more powerful, easy, easy sell for developers of, hey, you get a config file. It's consistent. It's better than just doing all this stuff in code, hopefully.
Right? So, if we align up with that, we can say, cool, if you move to new config, you get entities for free, nothing's breaking. If you keep doing stuff in code, you're gonna break all your entities.
Known problem. Won't fix, right?
**Daniel Dyla (Dynatrace)** 38:38 Well, not…
**Josh Suereth** 38:39 So it won't fix, but we could fix it later.
**Dmitrii Anoshin** 38:43 There is a similar…
**Daniel Dyla (Dynatrace)** 38:44 they almost need something that takes a resource that only has resource attributes and no… entities… And returns a new resource with all of the… entity refs.
Attached, and, like, drop, you know, tells you which ones were dropped or conflicted, or whatever, you know, or something along those lines.
**Josh Suereth** 39:06 That was what I was planning to build, actually, for Go.
Right.
**Dmitrii Anoshin** 39:10 We have a similar issue in the collector, because currently in the collector and the receivers, the interface allows you to disable, enable any resource attributes.
**Daniel Dyla (Dynatrace)** 39:20 specific attributes.
**Dmitrii Anoshin** 39:21 Yeah, specific attributes for receivers that actually produce several attributes. And what I've built is that… I just figure out whether… if you enabled… some of them are enabled by default, but you can disable everything. If, attributes… specific set of identifying attributes for a particular entity is enabled, it means that that entity is being emitted. If even one of them is disabled, that entity is just not emitted.
**Daniel Dyla (Dynatrace)** 39:49 You drop the whole entity?
**Dmitrii Anoshin** 39:51 Yeah, yeah.
**Daniel Dyla (Dynatrace)** 39:52 Yeah, I was gonna say, in the collector, it's like… I think the collector has historically… For, you know, for better or for worse.
it is, like, a collection of foot guns, and it might be okay to just say, like, you know what? If you disable one of these attributes, your IDs might not be unique. Like.
That's on you. Don't do that. But there might be valid reasons to do it.
**Dmitrii Anoshin** 40:19 I don't think we should… we should allow that. I would rather drop the whole entity, because… Yeah, I think we need to… Either… Provide backward-compatible data, or… The new data with the entity, but at least… Wait.
Northern Violet, right?
And… Reduced set of identified attributes of an entity is definitely… Invalid.
**Daniel Dyla (Dynatrace)** 40:50 So you're not… you're not dropping all of the attributes from the entity, you're just not creating the entity ref.
**Dmitrii Anoshin** 40:56 Exactly.
**Daniel Dyla (Dynatrace)** 40:57 Yeah, yeah, okay, that's fine. That's fine. You don't want to create inconsistent resources that have a ref that points to an attribute that doesn't exist.
**Dmitrii Anoshin** 41:06 Exactly, yes.
**Daniel Dyla (Dynatrace)** 41:07 Yeah.
**Josh Suereth** 41:08 Yeah.
Alright, let's… let's continue. So, I'll, I'll plan to take that if no one else signs up, but I think I can start making progress on that, actually. Okay, SDK startup specification. Daniel, you're… you had an update for us here, so… I understand why this isn't a clear config board.
**Daniel Dyla (Dynatrace)** 41:28 Yeah, that's from forever ago. It was on the wrong board. Yep, so I guess this is still in progress. I'll open a PR for this later today.
And I'll send it to you so that, because you said you wanted to work on… the prototypes, it already matches what my prototype does, so there shouldn't be any need to do… to change anything on the JS prototype, but next week we should have… More to talk about here.
**Josh Suereth** 42:00 Yeah, for Java, I just have to figure out how to put it in their incubating thing, where you make a whole bunch of classes private, and then you reflectively give yourself access to them, in, like, a separate jar?
So that you can, you know, break things in the private part. What's weird is Java made the mistake… resource current… I don't know how we do this without breaking compatibility and resource in some fashion, because resource actually exposes its class.
And it's exposing it as, if you're familiar with Google, Google Guaba has this, like, auto data value thing.
Apparently the way that's done, and the API compatibility version detector we have, you cannot use them together.
So, you break API version anytime you change how that thing works.
even though you kind of aren't changing compatibility, it's really annoying, so… I'll have to work with the Java maintainers on that a little bit. We had some approval to make this change, like, 2 years ago when we first did our prototypes. I don't know if they remember.
So, we'll have to have those same discussions again.
**Daniel Dyla (Dynatrace)** 43:17 Okay. Yeah, I… I suspect, you know, we had to make some changes in resource in JS, too. Fortunately, I am a JS maintainer, so I was able to just… kind of hand wave and say, like, you know, we're doing this for future reasons for entities, and we moved on, and everything was in the SDK, and we've been… doing major version revs there anyway, so it's been okay. But I suspect the hand-waviness of the resource specification from, like, day zero… is going to mean that a lot of the SDKs have implemented in, like.
Kind of weird ways, and inconsistent ways, inconsistent with each other.
**Josh Suereth** 44:03 Yes.
**Daniel Dyla (Dynatrace)** 44:04 Because basically, the entire resource specification boiled down to, it's a bag of attributes, it's immutable. Like, that was the whole spec.
And, you know…
**Josh Suereth** 44:17 Oh, and there's a detect somewhere. We're not gonna tell you what it looks like or how to use it, but you…
**Daniel Dyla (Dynatrace)** 44:22 Connect with no interface. Yeah. And then, like, nothing… like, the difference between synchronous and asynchronous, like, totally hand-waved, like, every… and all of these real-world problems that should have shown up in prototypes, because this was before the prototype process.
all the maintainers just made decisions based around that, including JS. We did the same thing.
And I suspect that that might come back and bite us when we go to actually do these implementations.
**Josh Suereth** 44:49 Yeah, the specification, I think, came from OpenCensus, which had the same thing.
But, like, in Open Census, it was the same people implementing it everywhere, so it didn't have the… divergence.
Ugh, anyway, okay, so… That'll be fun. That's why I want to get a jump on that, because I want to start getting to the point where we have prototypes out with the Develop strategy for asynchronous resources. I think these two are tied, right? That's like the same… this is the same problem.
**Daniel Dyla (Dynatrace)** 45:21 It's the same thing, yeah. I mean, we could maybe even merge these into one issue, or, like, you can't start up the SDK without doing, you know, at least in JS, you can't start the SDK without some… making some decision about asynchronous resources, because they exist.
**Josh Suereth** 45:40 Yeah.
No, I'm fine having them separate and just, like, tracking. Your one PR should probably fix both of those, great.
And then we just opened this one for Dimitri, so let's move on to, next step. Dimitri, show a demo of how the collector processors differentiate remote versus local.
**Dmitrii Anoshin** 46:01 This is the one that… I had to work on, and it's tightly related to the new one we created.
Okay, so, and I haven't done any progress on that yet.
**Josh Suereth** 46:14 That's fi- should I move those two together?
**Dmitrii Anoshin** 46:16 Yeah, I think so, yeah.
**Josh Suereth** 46:18 Okay, I'm gonna put them both to in progress as, like, next step, if that's okay.
**Dmitrii Anoshin** 46:23 Thank you.
**Josh Suereth** 46:24 then, track… oh, communicate breaking changes, specification around resource allowing non-immutable attributes. Until we actually have demos, like, until there's actually code that people can use to instrument things, there isn't a collector. I wasn't gonna do this yet. But.
So basically, Daniel, when your spec PR is there, and when we get our first merge of, like, the incubator Java stuff, the incubating JavaScript stuff.
that's when I want to actually start sending out this communication, to basically say, hey, here's what's changing, here's how you can try it with, like, JS in the collector, or with Java in the collector, so people see.
If I have a chance to get Go in the Collector 2, great, but I want to, like, let people see what this is. Hey, speak of the op-amp specification, remember we talked about this?
Oh, yeah, from last year. Cool.
Anyway, okay, so that's… that I'm still gonna hold off on. Finish SDK specifications so we can begin, not being, implementing entities and SDKs. I think this is, Daniel, you're working on that, so…
**Daniel Dyla (Dynatrace)** 47:37 Yeah, this is… that's a big issue. That's, like, step one, draw a circle, step two, draw the rest of the owl.
**Josh Suereth** 47:45 Yes.
**Daniel Dyla (Dynatrace)** 47:45 Let's draw the rest of the owl. I think maybe… You know, is that issue even worth… having an issue, like, we have to write spec, I think, is a bit, Taught a lot of people, right?
**Josh Suereth** 48:00 That's why draft, I think we need to split it apart into things that we… we need in there. Alright, so this one here from DashO, I'll take… I'll take this one.
I need to follow up with Michelle. I… I'm gonna re-read this and try to, like, continually figure out what's going on here and respond, but I think that, like…
**Daniel Dyla (Dynatrace)** 48:25 The key piece of information here is the following is a snippet from an internal PRD.
So, like, everything below that paragraph is in… is not… I think it's just copy-pasted and not necessarily written to be a GitHub issue.
So… It may… yeah, and that may be a cause of some of the weirdness of this issue.
**Josh Suereth** 48:53 That's fine, I'm just gonna re-read it and try to under, like, more internalize it, and then respond, but I think… what… what… there's two things I want to make progress on here. One is just make sure that what we've defined in entities solves this problem, or if there's anything we're missing. And the second is, I do think we need to start making some progress on, like, Dimitri, you're working on local ID versus universal ID?
I also want to do the same in semantic conventions, but this notion of, like, understanding the relationship between entities.
**Dmitrii Anoshin** 49:28 Yeah.
I think we need to bring relationships to the… to the Viva, essentially.
In some ways.
**Josh Suereth** 49:36 Yes.
Yeah, and I think that technically is all in… We put it in entity as a signal, but I actually think we might need to put… pull some relationship modeling things into Phase 1.
**Dmitrii Anoshin** 49:49 Right, right, I agree.
That's why I actually started that PR, because we need some understanding of relationship.
Yeah.
**Josh Suereth** 49:57 Yeah, and thank you for calling that out, because I don't think we would have done it otherwise, and I think we desperately need it. Yeah.
Cool.
Alright, anything, anything we need to add here that's not already there? I know that my name doesn't show up on anything here, but, this is… this is me here.
**Daniel Dyla (Dynatrace)** 50:17 It's okay, we know you're actually working. I actually have to drop off a little bit early today, so I'm.
**Josh Suereth** 50:25 Oh, that's fine, I was planning to end the meeting, if no one has anything else.
**Daniel Dyla (Dynatrace)** 50:29 Yes.
**Josh Suereth** 50:29 Cool.
**Dmitrii Anoshin** 50:30 Sounds good.
**Josh Suereth** 50:31 Alright. And next week, 30 minutes later, so…
**Daniel Dyla (Dynatrace)** 50:34 Alright.
**Josh Suereth** 50:34 Have a good day.
