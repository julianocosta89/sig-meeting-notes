SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matt Hogstrom (Broadcom Corporation)** 00:52 Hey, Jim.
**Jim Porell (Rocket Software, Inc.)** 00:53 Hey, Matt, how you doing?
**Matt Hogstrom (Broadcom Corporation)** 00:55 Good, how are you doing?
**Jim Porell (Rocket Software, Inc.)** 00:57 Can't complain.
Hopefully somebody shows up in this one.
**Matt Hogstrom (Broadcom Corporation)** 01:02 Yeah, we'll see.
Trying to figure out where I have a profile that's got Matt Hogstrom Broadcom Corporation, and just kind of make it a little more… palatable.
**Jim Porell (Rocket Software, Inc.)** 01:20 I think you could change it.
**Matt Hogstrom (Broadcom Corporation)** 01:22 That's what I'm looking for, I'll open all settings.
**Jim Porell (Rocket Software, Inc.)** 01:24 Where is that?
Here's the guy that's been on vacation for a year.
**Rüdiger Schulze (International Business Machines Corporation)** 01:35 Hey, Jim. Hey, Madge.
**Matt Hogstrom (Broadcom Corporation)** 01:37 Hey Rudiger, how are you?
**Rüdiger Schulze (International Business Machines Corporation)** 01:39 Good, thanks.
**Matt Hogstrom (Broadcom Corporation)** 01:42 How was your… how was your summer?
**Rüdiger Schulze (International Business Machines Corporation)** 01:44 Summer was great, so, went with the family.
To a lake and to the family to see the rest of the family, so this was good.
**Jim Porell (Rocket Software, Inc.)** 01:55 Nice.
Well, my summer got screwed. I came to… I wanted to visit you, but I blew out my Achilles in June.
**Rüdiger Schulze (International Business Machines Corporation)** 02:04 It's supposed to.
**Jim Porell (Rocket Software, Inc.)** 02:04 to go to the EOTC and see you.
**Rüdiger Schulze (International Business Machines Corporation)** 02:08 Yeah, I know. Next chance, next, next, next time, next time.
**Jim Porell (Rocket Software, Inc.)** 02:11 Next year, yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 02:13 Okay… So… let's catch up.
Hey, Jaeong Woo.
Good to see ya.
Okay, I think there's a couple of things we wanna… wanna at least mention today. Obviously, still in catch-up mode, but… Just taking notes next to her.
Speaking.
Hey, Greg.
**Jim Porell (Rocket Software, Inc.)** 03:03 Okay, Matt, you can drop now, Greg's here.
**Matt Hogstrom (Broadcom Corporation)** 03:05 Yeah. Well, thank you.
**Rüdiger Schulze (International Business Machines Corporation)** 03:11 I am.
So, a couple of things, and maybe let's start with… semantic conventions, Given that I was out, not much happened on the PR itself.
But, the feedback that I got was… in fact, and I… that we may have discussed this four weeks ago, the feedback that I got was really, if we can't look at aligning those concepts that relate to virtualization more into a… Own virtualization namespace.
And, reflect… obviously, you know, we are currently just looking from an HMC perspective on LPAS, but obviously this will further evolve in also representing, second-level guests and virtual machines.
So… I have a proposal on my laptop, which I obviously need to further flesh out, which would bring together a namespace for virtualization with the mainframe namespace that we started to define from an HMC point of view. I need to put this up.
And, I think I discussed this even on the semantic conventions stick once, what we should do about virtualization. I think what I took away from this is We keep that currently in our… and our SICK, because there is no virtualization SIC, we make the respective definitions, and eventually it may be other than transitioned or, even brought back to the base semantic conventions when… You know, when there's further adoption or feedback on that.
So, what I will do until next Wednesday is to put that out and brush up the PR from this perspective.
But let me ask, as we had this from the last meeting, was there any feedback of, you know, conversations of, you know, if this, what is currently out there is reasonable, or if we should be Kind of like adopting, changing it. Can also bring up DPR. Just give me one second to get there.
**Matt Hogstrom (Broadcom Corporation)** 05:38 Just, what I did is, internally, I shared it with a couple of different groups.
And we started to get some… some conversation going on it, but… Just given summertime and vacations and things like that, it kind of waned.
So, I suspect… I think we had a target to try to wind this up by the end of September, so, I'm hoping to have some direct feedback, in the next week or so.
**Rüdiger Schulze (International Business Machines Corporation)** 06:07 Yeah, that sounds good.
Right, so… Yeah, status is not visible yet here.
Let me just… Go here.
**Matt Hogstrom (Broadcom Corporation)** 06:26 So, Jim and I actually talked last… couple weeks ago. I think it was just he and I had joined.
And, one of the things we discussed was You know, I think our… general bent, when, as practitioners, we start thinking about all the data we could make available.
Versus really… Getting the, kind of, consumer perspective.
Meaning, you know, I'm an SRE, or I'm, you know, a systems programmer, etc, in an organization, what am I really looking for from OTEL? Because at the end of the day, in my opinion.
And it's just my opinion.
I'm gonna use the OTEL data that's being emitted to effectively be kind of a flashing beacon or a check engine light.
And… I'm probably not looking for all the data that I need to be present in the external system, it's just not feasible.
But I'm basically going to use and say, you know, kind of zone defense and basketball. Oh, looks like it's this area, now I've got a hint of where to go, and then I'm going to go back to my tools on the mainframe, or adjacent to the mainframe to really do my investigation. It's more of a… a leading indicator of what might be going wrong with enough information to help me scope where I go. That's how I think of the data we should eventually be documenting and forwarding off.
As opposed to the volumes of data that could be cataloged, because those are managed generally in context like capacity management software, like Mix, or MXG, or things like that. I'm not sure if you guys have your opinion on that.
**Jim Porell (Rocket Software, Inc.)** 08:14 Yeah, and as Matt said, I agree with him. I mean, it's… we gotta focus on a curated set.
Of metrics, because… or metrics, traces, whatever we do.
I'm dealing with a customer right now that was trying to send everything in the kitchen sink out there.
And then the next question, I said, why are you doing this? Well, we've adopted hotel.
And I said, everything you've asked for is subsystem metrics, not a single one was application-specific. So what's your real problem? Are you trying to focus on application performance in conjunction with distributed, or are you trying to do subsystem infrastructure?
And they didn't have an answer, and I'm like, let's go back to basics then, you know, because you don't… again.
Oh, and the other thing they were concerned about was, and the performance sucks.
Because they were sending so much outboard that, you know, and I think we got that one request a while ago, saying the collector couldn't keep up, but I think, again, if you turn on everything in the kitchen sink.
We're gonna add a lot of MIPS to ZOS, just in TCP IP alone, which isn't ZIP eligible, so… NetEffect is, it's a curated list, and we… as we go through the semantic conventions, we ought to focus on just those things, you know, and… Not trying to do everything.
**Rüdiger Schulze (International Business Machines Corporation)** 09:40 And I think I agree on this. I mean.
We've probably discussed this before, right? So there's this concept of the SRE versus the mainframe SME, and essentially the data, the hotel data that we see in scope.
would be solving the SRE, so the SRE needs to have certain indicators of Where a problem is, or if the system is healthy, the aspect of the system that they are looking at is healthy, and then they can move on to the next one if there's an issue in the overall application perspective.
And… the… The other aspect what I want to mention is, As we go, and it's kind of like what we… kind of, like, currently do with starting from the bottom, is we probably want to… established some… rules of how things should be named, even if we don't put them into semantic conventions. But if there is an intent.
By… as a customer or a vendor, to produce this data as… OpenTelemetry, then that there are some guiding rules of how to name things so that they are consistent in terms of How they should be made available.
**Matt Hogstrom (Broadcom Corporation)** 11:04 Yeah, I'd agree with that. I, like, for instance, if you grab data from SMF, I don't know what to… I always think of the, the… I call it the ugly name versus the pretty name.
So, for instance, you say, CPU. Well, okay, what does that mean? You know, CPU percentage of the whole box with 32 cores? Does that mean, you know, the average, etc. So, if you go back to the source of the data, there's generally a… an identifying source, right? Whether you got it from a control block, or you got it from an SMF record and whatnot. So, if you can convey that, I don't know if that would be metadata, or that would actually be the name.
But that would be helpful, I think.
**Rüdiger Schulze (International Business Machines Corporation)** 11:48 I think this goes to the point that we… Where we probably will have more discussions around in future is what entities or resources do we have?
So, getting the resource definitions right is probably more crucial, because then, you know, we can attach any of the data that, you know, is out there if needed, right?
**Matt Hogstrom (Broadcom Corporation)** 12:23 Were you able to pull it up, or…
**Rüdiger Schulze (International Business Machines Corporation)** 12:25 Yeah, I do have it here.
**Matt Hogstrom (Broadcom Corporation)** 12:26 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 12:30 Let me bring this up.
Sup.
Yeah, so this is what we currently have, and as you can see already… let me make this bigger, this is not readable.
Right, so this is due to… Damn.
area where I'm currently working on need to catch up myself, but obviously I started to put some, definitions in there already from a hypervisor platform NVM perspective for… for the virtualization, but I didn't put it on the PR yet, I think.
So… it goes into this area that we need to have identities, for instance, for partition, but in the same way, we would have to have this as well for the hypervisor, for the VM.
And so on. And that would be replacing what we had earlier. If you want to go down that path, Mainframe LPAR, I think we had been defining earlier.
And that obviously also takes us to some of these questions around how should things being named. Is ALPOS still the name to be moved forward with, or is this partitioned?
As an example, not sure if you have internal discussions around terminology, but obviously it's, you know, in the light of also a more younger workforce coming in, a topic.
Of how to name things and, You know, also learning from an… From an industry perspective, some of these names should be more… Interpretable for the broader community.
Right.
And then from a mainframe perspective, obviously, we had a… a set of attributes being defined, but let's take a quick look at what is currently there from entities. And entities, obviously, that goes very much with what is from a… metric group perspective out there, if you think about metric groups, they address different aspects, either in classic or in DPM mode.
And I think I also discussed the… Just as a helper here to look at… what the HMC premise source exporter is providing, because it gives kind of, like, some indications, but what actually this does is that… We get a naming scheme, and if we can agree on this naming scheme, and obviously also there's an intent to reuse whatever is… being defined in semantic conventions already, out there, so host is one of the examples, and, need to remind myself, but obviously there is a way then also to… you know, build up the… what would be a mainframe host, using the host concept. I think I need to go back and remind myself what the underlying concept was, but if… if there is already an entity being defined, we don't want to redefine that, essentially, in our scope.
And that's also the tricky part, obviously, is still some overlap, so I started with virtualization, but… so I'm somehow in the middle of getting this done.
Right.
And if you look at, just as an example, some of these… I mean, you mentioned CPUs, right? So CPUs is a perfect example. There is, Also, what I try to do is just to, from HMC point of view, is not complete, and might actually have other representations if you move into operating system and so on, but in semantic conventions, you can add annotations, which help to… Explain where data is to… supposed to be read from.
So… Personally, thinking we should use that, because it will help us to interpret also the data, or a consumer to interpret the data.
Where this is coming from.
**Matt Hogstrom (Broadcom Corporation)** 16:59 Just a… so it's just, like, a question on this. So, I think you've got Mainframe, right, .cpu as your, your, scope.
But this is really more of an HMC perspective on the CPU.
**Rüdiger Schulze (International Business Machines Corporation)** 17:15 Yeah, currently, yes, yeah.
**Matt Hogstrom (Broadcom Corporation)** 17:17 So, I think it goes back to, you know, Or the data item.
What is the context? So I think Mainframe is too coarse-creened.
We talked about this a little bit earlier. I would almost go with, you know, S390x.hmc. Right, CPU. Now I know exactly what CPU I'm talking about. S390x.
zos.usss, or zOS.MVS. So as you… you're kind of breaking your namespace into contextual domains for the items.
That, I think, is helpful. I don't know if that's too granular, but, you know, like, USS is distinctly different in terms of process threading, etc, from MBS.
And having that… Distinction is useful in my mind, but again, that gets back to the who's the consumer of the data.
But I think that the namespace is going to be something critical we have to make a decision on, how we want to do that.
**Rüdiger Schulze (International Business Machines Corporation)** 18:20 Right, and un… kind of on the flip side on this, so the example I like to just give here, right, that would be somehow leading to… within this particular mainframe-specific namespace, we give a definition of a CPU, right?
The flip side to this is there is a system CPU utilization being defined in the semantic conventions.
And there's also a concept of refining what is available in the base semantic convention, so we could.
**Matt Hogstrom (Broadcom Corporation)** 18:54 odd.
**Rüdiger Schulze (International Business Machines Corporation)** 18:54 additional attributes.
And, also be more prescriptive in this way. Now, the concept here is, just generally, right, you associate a metric with an entity.
And, okay, in this regard, it's just a mainframe CPU, or it could be… if we come up with other entities, be more fine kernel eventually as a CPU definition, so… where I'm going is, there is this… you define entities.
as part of your system, and these entities, they carry attributes, and I need to go back to that one, let me do that.
The CPU… here we have the host.
Here, right? So then you define… I mean, obviously, we can have different types of CPU on… on… on… even on the HMC level already, right? So, you would, somehow partition your namespace using these… these required attributes to say, okay, this is a GP, or this is a SIP, or similar, right?
And that's kind of like the tricky part, where we need to define and identify the right model, and where probably also feedback from Antoine and the other observability vendor represents By the way, Guillaume Wu, we haven't met yet, maybe you're from one of the observability vendors, so that would be questions that… where we also need to reconcile Back, what, you know, What's actually the expected format that they would like to get?
In terms of… Getting this partitioning of the namespace right. And, similar to this ray use. Actually, as I said, right, we might keep the resource CPU, mainframe CPU, because it has a very specific definition, but it might be… And I think I started to look at this as might be a refinement of this… I'm not sure where the CPU is sitting, maybe a host.cpu, I would have to look this up in the base semantic conventions.
But that'd be a refinement for the mainframe.
And then additional attributes being added. The key here is that with these refinements, actually what happens is you can keep also the name of the underlying entity, I think, and also metric, but you add additional attributes. So the way how far that would be coming out on any of these dashboards is, in the end, you see a host CPU, but you see, okay, this is associated with some mainframe Characteristics, so… obviously, you know, coming from a mainframe system, and this is what we need to get right.
**Matt Hogstrom (Broadcom Corporation)** 22:04 Yeah, I agree. I, I think if, As my gut says, the more attributes you have.
The too coarse-grained your resources, because you almost have to qualify it a ton.
**Rüdiger Schulze (International Business Machines Corporation)** 22:17 Yeah.
And there's another aspect to it, right? We have the CRNA being defined on the… on the resource.
I also have seen examples where the same set of attributes actually peeled back on the… on the metric.
But that would be then actually replicating information, and…
**Matt Hogstrom (Broadcom Corporation)** 22:39 True.
**Rüdiger Schulze (International Business Machines Corporation)** 22:40 So, this is another question that I still need to solve in order to get this right. So I think we, we will have a couple of iterations to get this overall naming scheme right for our domain. Once we got that, I think we are in a good shape to, you know.
Build this up in a way that we are not conflicting and are actually, from the broader ecosystem perspective, well consumable.
**Matt Hogstrom (Broadcom Corporation)** 23:24 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 23:27 Okay, yeah. So let me, let me put this up for next week, and maybe we can get Antoine or anybody… from the other vendors to look at that as well. I mean, the idea is also to have some prototyping done. What we discussed earlier, there is the Wivo tooling, which is actually able to produce some sample data, so it's maybe something that we can then also… Try to have some… somebody to validate from the other vendors to look at if this makes sense. It's probably the best what we can do.
Okay.
**Matt Hogstrom (Broadcom Corporation)** 24:11 Would it be useful to, provide any kind of ranking about, importance?
**Rüdiger Schulze (International Business Machines Corporation)** 24:19 So…
**Matt Hogstrom (Broadcom Corporation)** 24:20 Just, for instance, if you're gonna try to define everything in one fell swoop, that's a big ticket item.
I would say, quite honestly, channel adapters and partitions are… I'm just using them as examples, I'm not picking on them, but are probably less relevant to consumers of the data.
Right? Unless you're actually looking at the HMC or CAIC performance, then they're very relevant. If you're looking at any of this data from application perspective, like Jim was talking about, these are kind of irrelevant. So, the real issue then becomes what Out of the items that we could put out.
If we rank them by, you know, kind of Tier 1, Tier 2, Tier 3, that might help us Manage the volume of definitions.
**Rüdiger Schulze (International Business Machines Corporation)** 25:09 I mean, just going by the example of CPU, right? Maybe we should really narrow down the scope here a little bit to say, let's get the virtualization concept from, at least up to LPOR, right?
And, let's focus maybe on CPU and memory.
Very, very simple things, obviously, in some way.
But have them correctly being defined, and then broaden it.
**Matt Hogstrom (Broadcom Corporation)** 25:38 Yeah, I think that those would be Tier 1, right? Everyone's gonna be interested in… in that.
**Rüdiger Schulze (International Business Machines Corporation)** 25:46 And the broader we actually take it, there is also certain questions, then, from an underlying concepts on… network is an interesting area, generally. There are certain definitions out there. There's also a network definition out there now that creates new base definitions.
I think we had issues… don't remember, I exactly need to go back, but there were issues in terms of representing NICs correctly, and even using the base definitions currently. So, there are certain And also falls and back with a base definition, obviously, that we… in this way, I think a tiering will be good to… to… to do.
That's all nodes.
I think we discussed, Hi.
What else for today? So, thanks, Greg, if you're still on. Oh yeah, you're still on, right?
I'm just dropped.
Greg, thanks for putting out the other, doc PR.
Bank.
**Greg Shriver** 28:11 Oh, yeah, that got merged.
**Rüdiger Schulze (International Business Machines Corporation)** 28:13 Yeah, I think this one here, actually.
**Greg Shriver** 28:15 Finally.
**Rüdiger Schulze (International Business Machines Corporation)** 28:17 we can… I think this is Razor for notes, I think we can.
**Greg Shriver** 28:20 Yeah, we can… we can pretty much delete that.
**Rüdiger Schulze (International Business Machines Corporation)** 28:23 Okay, good.
**Jim Porell (Rocket Software, Inc.)** 28:25 Sorry, I lost all sound for a minute, I don't know why, but…
**Rüdiger Schulze (International Business Machines Corporation)** 28:29 assigned all the work to you, Jim.
**Jim Porell (Rocket Software, Inc.)** 28:33 Excellent.
**Rüdiger Schulze (International Business Machines Corporation)** 28:34 Okay.
The, Anything else from this regard, I think on the 9th or 10ths, and I think everybody has the invitation. We have the OMP.
Tech meeting on the… on the… was currently stood at the… let's see, I think the… hotel, but also for CUS, I think, that's the… Still alive.
the working name.
**Jim Porell (Rocket Software, Inc.)** 29:07 By the way, I want to make sure, again, no guarantees, but Morgan sent out this updated meeting notice a couple weeks ago.
**Rüdiger Schulze (International Business Machines Corporation)** 29:16 Yeah.
**Jim Porell (Rocket Software, Inc.)** 29:16 I tried to dial in last week.
And it was for a September 2nd meeting.
And so, I'm hoping to God next week.
isn't for September 2nd also, I don't know.
But it was weird.
**Rüdiger Schulze (International Business Machines Corporation)** 29:30 Kind of…
**Greg Shriver** 29:33 It looked like it was every 2 weeks.
**Matt Hogstrom (Broadcom Corporation)** 29:35 It's every other week, yeah.
**Greg Shriver** 29:37 Every other week.
**Matt Hogstrom (Broadcom Corporation)** 29:38 I sent Morgan a note to say it should be… the title should be changed to bi-weekly so it's more clear.
Because I think it still says weekly in the title.
**Jim Porell (Rocket Software, Inc.)** 29:47 Okay.
**Matt Hogstrom (Broadcom Corporation)** 29:48 The question is, is it supposed to be bi-weekly, or did you… do we… do we have enough work to actually work through? Because we only have, like, 4 weeks before we get to the end of September.
**Rüdiger Schulze (International Business Machines Corporation)** 29:59 I think it's weekly on here, so this is… well, it actually did… Per previous and current plans, I think we are meeting weekly, always at…
**Jim Porell (Rocket Software, Inc.)** 30:08 I thought so too, but…
**Greg Shriver** 30:11 I mean, we've been… I… I… and I… we've always been meeting weekly, and I didn't know… I know I've missed a couple meetings, and I wasn't sure whether we changed it to bi-weekly or not.
**Matt Hogstrom (Broadcom Corporation)** 30:23 No, so I think the reality is it's currently on the schedule as bi-weekly, and it should be weekly.
But Morgan never responded back to my… my comment.
**Rüdiger Schulze (International Business Machines Corporation)** 30:35 So this is then a scheduling issue with the… with the Zoom meeting, maybe. At least here on the calendar, it looks like OKH and the Google Calendar.
**Jim Porell (Rocket Software, Inc.)** 30:47 Yeah, mine looks alright, but… Like I said, since last week.
Which was… see, I didn't realize, you know.
once it… once it said that Rudiger's out until September 2nd, nobody showed up anyway, so it didn't matter. So that's what kind of power you have, Rudiger. There you go. But when I tried to click on the link, it was for a September 2nd meeting, even though it was the week before.
**Matt Hogstrom (Broadcom Corporation)** 31:13 No, so I can confirm, because I talked to the CNCF folks that were scheduling it, and she said, this is bi-weekly.
But it says weekly, what do you want to do?
And I said, Rudiger was changing it, so I think we can adjust it, but I think the intent was weekly. She says, well, let me know, and I'll change it for you.
**Jim Porell (Rocket Software, Inc.)** 31:33 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 31:33 If you have a contact to her, if maybe you could drop her an email or a message.
**Matt Hogstrom (Broadcom Corporation)** 31:39 I can do that. Sure.
**Rüdiger Schulze (International Business Machines Corporation)** 31:42 Okay, yeah.
**Jim Porell (Rocket Software, Inc.)** 31:43 So, just…
**Rüdiger Schulze (International Business Machines Corporation)** 31:43 reconfirm this. We want to meet weekly, that's the cadence that we had before, and that's actually what we want to… Wanna stay on.
**Matt Hogstrom (Broadcom Corporation)** 31:52 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 31:53 Okay.
Good.
**Greg Shriver** 31:57 And I also have something.
**Rüdiger Schulze (International Business Machines Corporation)** 31:59 Yeah.
**Greg Shriver** 32:00 Or whenever a good time… a good pause time is.
**Rüdiger Schulze (International Business Machines Corporation)** 32:04 Go ahead, go ahead, Craig.
**Greg Shriver** 32:06 So, I… I saw that there was a… a message out on the hotel mainframe Black channel.
And it was from, Colin Pace. I don't know if I'm pronouncing that correctly. And he was asking about, has any work been done on scalability and availability for OTEL on ZOS?
And, so… I did put a reply out there. I wanted to let you guys know that I did put a reply out there. My reply is really kind of from my perspective, but I wanted you guys to be aware of it.
In case, you know, you have some other stuff that either, you know.
In case you have other opinions or… or… you know, visibility into other areas of this that I don't.
So, I, I… I guess I can.
Sure.
**Jim Porell (Rocket Software, Inc.)** 33:05 Yeah, I'm reading what you wrote, so…
**Greg Shriver** 33:07 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 33:08 Yeah.
**Greg Shriver** 33:08 So, the net and net is that my contention is that, you know, that… that much of this is still, at least on the ZOS side, still is sort of vendor-specific, and really isn't vendor agnostic yet.
And I think we have… we kind of have a ways to go before… if we realize that completely vendor agnostic, I take an OpenTelemetry collector, drop it on ZOS, and boom, I'm good, you know?
there's… so that's kind of my assessment of the state of affairs and where we are. I mean, there's… obviously, there's a lot of what I would consider to be enablement work by, you know, all the vendors, including Broadcom.
You know, and the work of this group.
So, But anyway, that… that's sort of… that was… that was my… my take on it, so feel free to chime in.
Or reach out to this guy, because I don't know why he's asking the question. That would be… that would be kind of interesting to know why he's asking the question. When you were speaking, Jim, I was thinking, wow, I wonder if this guy was working with Jim.
**Jim Porell (Rocket Software, Inc.)** 34:24 Any strong?
**Greg Shriver** 34:24 to set.
**Matt Hogstrom (Broadcom Corporation)** 34:25 And,
**Greg Shriver** 34:25 This stuff out, you know.
**Matt Hogstrom (Broadcom Corporation)** 34:26 Colin is, Colin's a retired IBMer, and…
**Jim Porell (Rocket Software, Inc.)** 34:30 Fuck, yeah.
**Matt Hogstrom (Broadcom Corporation)** 34:31 And he, I guess the danger is when you're a Z guy for a long time, even in retirement, you've got a ZD&T at home, and you're playing with it, and he does a lot of blogging, he's really productive. I can ping him, I talk to him periodically.
**Greg Shriver** 34:49 Oh, that's awesome. Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 34:51 Good, yeah.
**Jim Porell (Rocket Software, Inc.)** 34:51 Yeah, I recognize his name, so…
**Matt Hogstrom (Broadcom Corporation)** 34:53 Yeah, he's a good guy.
**Greg Shriver** 34:57 And then… and then the last thing, I guess, is just sort of an awareness for the group.
is that, you know, my priorities have kind of shifted here at Broadcom.
And, I will probably be able to attend these meetings less and less.
So, you know, given that, you know, Matt and I have talked About this, and, you know.
Matt is way better at this stuff than I am. But, you know, all the other stuff that we have, you know, that we have in place, like, I guess I'm part of the… what the… Maintainer's group for the repo, we might want to consider transitioning that off to someone else in the group.
You know, but anyway.
I just wanted to throw that out there and let y'all know.
**Rüdiger Schulze (International Business Machines Corporation)** 35:47 Yeah, so, Greg, first of all, thanks for all your contributions that you've done.
And second, you're always invited to come to these meetings. In terms of maintainers, I think we definitely need to have a second one from a, you know, one other company than mine.
And, we can make a voting, or, you know, Matt, if you would be willing to handle that, Yeah.
**Matt Hogstrom (Broadcom Corporation)** 36:18 I'll be coming to all the meetings, so Greg and I talked about it, and I'll keep him in the loop, and I'm sure he'll be out keeping track. He's checking out Slack at the CNCF, so Greg will forever be connected.
**Rüdiger Schulze (International Business Machines Corporation)** 36:34 And, Jim, and also any other on the call, obviously, I suppose what I ask, you know, if you're okay with this, then, you know, we… would nominate Matt as a second.
Or…
**Jim Porell (Rocket Software, Inc.)** 36:48 Follow that, yeah, no problem.
**Rüdiger Schulze (International Business Machines Corporation)** 36:51 Okay, good. But I will add you, I need to check, but I will add you as maintainer, you should. And it starts from, probably, we need to invite you to the organization, OpenTelemetry organization. So that's a couple of, Administrative things that we need to…
**Matt Hogstrom (Broadcom Corporation)** 37:06 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 37:07 Both on the way.
**Matt Hogstrom (Broadcom Corporation)** 37:08 I'm with you, I'm… It's a process.
**Rüdiger Schulze (International Business Machines Corporation)** 37:12 Yeah, right. I will send this over, later, either today or tomorrow to you.
What needs to be done.
**Matt Hogstrom (Broadcom Corporation)** 37:22 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 37:23 Good.
Just to this reply, I think you're right in terms of, you know, scalability and also vendor-specific solutions. COS, I think we had this earlier, you can build the collector, the OpenTelemetry Collector in COS.
**Matt Hogstrom (Broadcom Corporation)** 37:43 Successful.
**Rüdiger Schulze (International Business Machines Corporation)** 37:44 done, but it's largely incomplete, given the specifics that you have on the Unix system services.
I don't know if you… it's more a question, right? We don't see… really requests for the collector itself on COS. Linux is obviously more interesting here, Linux on C. Sure. But, if ever this becomes a real requirement from somebody, then, you know, we might actually invest in this from a SICK point of view.
**Matt Hogstrom (Broadcom Corporation)** 38:18 Yeah, I got this at the collector running in USS, and we're looking at including it as part of what we're doing with Hotel, but, you know, we'll… we haven't… We haven't pushed 50,000 records through at a second yet, so…
**Rüdiger Schulze (International Business Machines Corporation)** 38:35 Yeah. Which…
**Matt Hogstrom (Broadcom Corporation)** 38:36 It seemed to be a little too high, but, you know, we'll see.
**Rüdiger Schulze (International Business Machines Corporation)** 38:39 Yes.
Good.
**Matt Hogstrom (Broadcom Corporation)** 38:41 But I was really surprised. It was clean. The compile was, like, painlessly easy.
**Rüdiger Schulze (International Business Machines Corporation)** 38:47 Yeah.
if you… especially if you start from the core collector, I think.
This runs pretty quickly through.
**Matt Hogstrom (Broadcom Corporation)** 38:56 It does.
**Rüdiger Schulze (International Business Machines Corporation)** 38:56 From a compilation perspective, but then you have issues like the host metric collector that doesn't work, and I think we had also tests with Contrape, and obviously there's various reasons why Contrape won't work.
**Matt Hogstrom (Broadcom Corporation)** 39:09 Yeah, maybe you can talk with your friends in ZOS land and get them to start including Go and other Other languages as part of the base operating system.
**Rüdiger Schulze (International Business Machines Corporation)** 39:19 Yeah.
annoying.
**Matt Hogstrom (Broadcom Corporation)** 39:22 It always feels like I'm… I want a car, but it's in the shop, and I've got to assemble it each time I want to use.
**Rüdiger Schulze (International Business Machines Corporation)** 39:28 Do you use… I asked this for specific reasons, also OTIL-related, do you see interest in Rust on CUS?
**Matt Hogstrom (Broadcom Corporation)** 39:38 You know, I… I don't know, actually, it's funny you say that. Given the NIST's push for, you know, memory-managed runtimes, as opposed to C. That might actually be interesting.
**Rüdiger Schulze (International Business Machines Corporation)** 39:52 Okay.
**Matt Hogstrom (Broadcom Corporation)** 39:53 I don't have an immediate need for it, but, we've talked about the, you know, some of the how do we manage Steve versus Assembler, etc, and just try to confine things a little bit more appropriately into the right runtime.
**Rüdiger Schulze (International Business Machines Corporation)** 40:06 Okay, yeah, interesting. Good.
Okay, anything else? Let me just add this, what we just said, so, add.
Good.
Yeah.
Anything else you want to discuss today?
**Matt Hogstrom (Broadcom Corporation)** 40:39 Not for me.
**Jim Porell (Rocket Software, Inc.)** 40:40 No, thank you, and like Matt, I'll get this PR routed around as well to get… Couple more eyes on it, so…
**Rüdiger Schulze (International Business Machines Corporation)** 40:48 It's for sure still in a working state, but yeah, let's get some comments on it.
Oh, good.
Thank you. Bye.
**Matt Hogstrom (Broadcom Corporation)** 40:56 Thank you.
**Jim Porell (Rocket Software, Inc.)** 40:57 Thanks, everybody.
**Greg Shriver** 40:58 Bye.
