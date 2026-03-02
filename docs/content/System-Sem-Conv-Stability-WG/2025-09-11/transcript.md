SIG: System Sem Conv Stability WG
Date: 2025-09-11
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:14 Hello?
**Pablo Baeyens** 00:18 Ayy.
**Christos Markou** 00:28 I think Roger, won't join.
So, probably… And Josh will be late, so probably we'll wait for Dimitri.
Only.
**Pablo Baeyens** 00:40 Boogie.
If you want, we could do the splitting of the project into the…
Tier 1? Does that make sense to you?
**Christos Markou** 00:54 Yeah, I'm… I'm not sure, because I don't have access to edit those.
this board, I mean, the roadmap thing. So, I don't know what we can… how those will look like, and if those will be meaningful.
But we can try, I mean, if we have concrete… oh no, I see the roadmap.
Okay Yeah, we can try.
If that y'all.
**Pablo Baeyens** 01:26 So… Yeah, for example, for the… collector, or the…
goesig. There are boards that track
Things, but they are, like, permanent.
Those do not show up here.
It's just like… projects within…
within a SIG, and the project within our SIG is, like, getting to GA.
**Christos Markou** 01:57 Yeah, a single one. Can this work with tabs, different tabs? So, each tab, for example, we have a GA tab, if I remember correctly.
So… Can't this be… There, go, good.
Can the roadmap use single tabs?
**Pablo Baeyens** 02:17 We could just do that, so… let me… give me a second, I'll… more of my tabs around.
Share my screen.
**Dmitrii Anoshin** 02:43 Packhawks.
**Christos Markou** 02:46 Hello.
**Pablo Baeyens** 02:52 Okay,
Do I think you can see my screen now?
**Dmitrii Anoshin** 03:01 Yes.
**Pablo Baeyens** 03:03 Okay. So, basically, in the roadmap, there's an issue…
The issue has a link to… our board…
Then it has a bunch of fields here.
And, what Don wants from us is…
First, do auto status update here.
And, then, like, a start and target date.
And ideally, for other projects, like, it's been…
Boards for specific things that have a start and an end.
If we want to…
use this board and have, like, just say, like, well, this is the view that the start and end refer to.
We can do that, I guess.
Or we can Wars.
**Christos Markou** 04:06 Could we use, probably… yeah, what happens if you create a page use there in the…
The single issue that… It's linked on the roadmap thing.
**Pablo Baeyens** 04:17 here?
**Christos Markou** 04:17 Yeah.
**Pablo Baeyens** 04:20 I'm not sure if we can do that, because there's, like, some automation… There's this…
script, and the script just, I think, takes the different…
projects, so I don't want to mess with that. The, like, the…
these issues in the end, I think, are…
auto-generated, so I wouldn't want to…
The thing we can modify is this.
**Christos Markou** 04:49 Okay.
**Pablo Baeyens** 04:50 We can change the automation, I guess, that's…
**Christos Markou** 04:55 Yeah, Python, thing, okay.
Yeah, so I think that…
In that case, I'm not sure if it… if that's useful. From… yeah, my thought was mostly about,
Trying to split the work.
And, depict the phases that we are on. For example, the things that we are targeting, for example, to stabilize process namespace.
Or process entity, whatever, to have a way to
show this, and commit to a date, probably, or something like this, and then have all the other pieces coming after something like this, but I'm not sure if we can do this based on this automation.
**Pablo Baeyens** 05:52 We can only have one… Start on target date, but I mean, let's…
My suggestion is, let's use the status updates for the thing we're focusing on right now.
And let's make that clear on the status updates. Okay.
Like… we can… keep updating that here. Like, once we finish the processing, we will…
Change the start and target date for the next thing.
Does…
like, I think that's an ad improvement, and we don't need to do a lot of work for that, just like…
**Christos Markou** 06:31 I'll be.
**Pablo Baeyens** 06:32 the steps update.
**Christos Markou** 06:36 Yeah, okay.
Sounds good. I have asked, on the issue for Kubernetes, just for your information, I have asked Daniel how we can,
because we have two phases, essentially, in Kubernetes. One is the first phase, which is the…
the initial definition of all the metrics, and then the second phase will… which is ranked now, then the second phase would be to actually work on stabilizing those. I wasn't aware of this automation, so probably, we'll get a similar answer here.
But yeah, if…
For this single issue, yeah, it's not really useful, because, this will be running for, for long.
So, I'm not sure we can use this tool.
Provide any meaningful content, yeah.
**Pablo Baeyens** 07:33 Let's see what Don says. I can…
bring this up on… on Wednesday.
Next week.
Since, like, we're doing this because of the… graduation.
We can… we can talk about it with the rest of the governance committee.
Not included.
Okay, yeah.
Since I'm already sharing my screen, is there anything we want to discuss with Josh?
Anything we want from… General semantical mentions, maybe… Or anything we want.
to be unblocked.
**Christos Markou** 08:26 I think, regarding the discussion we had last week about the status and state guidance.
Brayden shared his or… I saw that, he has updated the PR already, which is good. It's not really crucial for this system working group, but overall, it's a nice addition.
And, yeah, it would be nice to provide reviews there.
And, then, yeah, I was planning to start on…
To pick up the issue about, providing guidance.
Yes. Oh, it's, it's in progress?
Anyways, yeah, I haven't… started yet, but, I was planning to start.
**Pablo Baeyens** 09:19 Yeah, you moved into progress in June, but I guess, yeah.
**Christos Markou** 09:23 Okay.
Cool. So that would be my next thing.
But I'm mostly, yeah, my time is consumed from the gate sink, so… But…
I have to, find time for this group as well.
**Pablo Baeyens** 09:41 Okay, so then, you're going to work on this one. This one is blocked by… the entities… Process…
I don't think there's been any…
Any updates on this, right, Dimitri?
**Dmitrii Anoshin** 10:08 It's not really blocked. We, as a Sikh, we need to figure out.
**Pablo Baeyens** 10:16 Yeah, I guess, like, Diz 1…
define common attributes under research requirement levels is blocked on defining the entity. That's… that's the blockage. But yeah, we can… we can work on…
**Dmitrii Anoshin** 10:29 Okay, can you go back, please?
Is there… I mean, do you know if the framework VW itself supports defining, identifying, and non-defined attribute? If it does, we can start working on that and actually put definition in there. I believe it already supported
So we can just, go ahead and,
Set whatever is… what we believe is identifying attribute for the process.
And that definition would cause this issue.
I believe we discussed that and agreed that creation time and PID is,
**Pablo Baeyens** 11:12 Yeah, that's… that's what we have here.
**Dmitrii Anoshin** 11:15 Cool, yeah, we just need to define it.
I can maybe find some time to work on that.
I'll also…
I'm gonna work a lot on the entities implementation and the collector. I'm finishing something in… something in Splunk, and then I'm gonna switch to…
Actual implementation of the entity signal, at least, like, resource-related resource references in the collector, and then
Probably will touch on this one as well.
**Pablo Baeyens** 11:44 Hmm.
**Dmitrii Anoshin** 11:47 Because, like, currently, a status update from the ATT6 is that we have…
Like, a lot of hot apps merged, a lot of specifications work, etc, and now we are in a phase of,
actually implementing the prototypes that we had before. People are working on instrumentation libraries, and I'm gonna do a similar thing on the collector.
And for now, it will be only entities which are delivered within the resource definition, so it… no breaking changes, nothing like that.
Then maybe assign it to me.
This one.
**Pablo Baeyens** 12:34 This one? Okay, I'll assign it to you.
**Dmitrii Anoshin** 12:38 Thank you.
**Pablo Baeyens** 12:48 So I'll… I guess I'll tell Josh that we don't need him.
Peace.
Weak.
If that makes sense.
When I…
**Dmitrii Anoshin** 12:59 About what?
**Pablo Baeyens** 13:02 So Josh asked if, we needed him to come to this meeting this week, but I…
Don't think the things that we are discussing.
**Dmitrii Anoshin** 13:13 Yeah, probably not.
**Christos Markou** 13:16 What's the… yeah, one question. What's the, goal that we discussed about last week?
Yeah, maybe… I forgot, but it's about…
process is the issue that we discussed, specifically the entity thing, or process in general? .
**Pablo Baeyens** 13:36 We discussed the entity thing, I think for this to be useful in practice, we need to…
Deal with the other issues in the area process that are here, just because
Like, for this to be useful, we need to… .
**Christos Markou** 13:56 Oh, the metrics.
**Pablo Baeyens** 13:56 The process swiper, yeah.
**Christos Markou** 13:59 Yep.
Okay, okay, sounds good then. Alright.
I can look for people from my side internally, if anybody has time to.
I'll pick stuff from… from this. Probably Roger or somebody else.
**Pablo Baeyens** 14:34 So…
**Christos Markou** 14:36 We don't need Josh, I think, for today, yeah.
**Pablo Baeyens** 14:39 Yep.
This one is about renaming…
Okay, is the OS namespacing thing sold?
**Christos Markou** 15:15 I'm not sure. I remember.
**Pablo Baeyens** 15:30 Oh, dear.
Okay, so this is… Based on the discussion here, this should also be fair enough process…
It is also blocking.
Then…
So I just want to get the board on to…
Reflect what we need to do.
**Christos Markou** 16:12 Yep.
**Pablo Baeyens** 16:17 Logged on that, but that is closed.
Okay, yes.
Maybe… these VRs also, I haven't taken a look at them.
Okay, so, this one is… Review…
So I guess another thing to do is to review this… 2PRs?
This one… on this one, I can… Share that.
And then this is… Still under discussion.
Yeah.
Sorry, I've been… rumbling a lot, but, I guess the conclusion is…
Dimitri's going to work on the entities thing…
Krista is going to work on this.
there's two PRs reviewed, I can review those, and I can take one more thing, I guess.
Could be this…
Okay, and this actually is also… believe.
Okay, so then I'll take this one.
**Christos Markou** 18:43 That's a good one.
**Pablo Baeyens** 18:46 Okay, and then, yeah, we have…
this to review. I don't know if you want to go through them, we still have, like, 10 minutes, so we could…
Maybe look at these together right now.
So… 2… Go back to the issue…
there's some… guidance that I don't know where it is, where…
We have, like, underscore or periods,
Deciding where something is a namespace, or should be, like, an underscore.
And, this was blocked for a while because something in Weber…
Did not distinguish between dots and underscores, and so there were some collisions.
But that was fixed.
So now we just have to apply that rule, but I don't know what that rule is.
Do you know if that is written somewhere?
be good to… No.
**Christos Markou** 20:10 Not really.
**Pablo Baeyens** 20:24 Okay, maybe if I look for…
created… on October 21st…
No, nothing.
Okay, so then, I guess we'll just trust Braden.
Sweetie.
This one.
**Christos Markou** 21:39 Oh, it looks like Vishan adds a brief.
In their arms, or… Not, probably, because I see these changes in… From lowercase to uppercase.
**Pablo Baeyens** 21:53 Yeah, it changed the description as well.
**Christos Markou** 21:56 Yep.
Yeah, this, this briefing, the members.
I think this is blocked, so…
This is not decided yet to have, briefs in the numbers.
**Pablo Baeyens** 22:12 Okay, so then I can… I can comment on that,
Oda was…
**Christos Markou** 22:55 I can send to you.
Also, the comment, too.
100 million.
**Pablo Baeyens** 22:59 Okay, yeah, that would help.
But otherwise, I think the PR looks good.
I am going to… Seta from my side, if you want to review…
Or a vote or something, just let me know.
So it looks… Long ago.
And then… We have this one.
Which… It's related to that one, but also to…
So let's look at the issue first.
Okay.
Don't worry.
Okay, I don't remember why we agreed on system memory paging full-time.
But I guess that is something to mention here.
And then the brief thing again…
Okay, I'll… I'll mention that.
Does that make sense? Is there…
Is there any reason why we should do system paging full-time instead of system memory paging full-time?
**Dmitrii Anoshin** 25:32 I guess the reason is that Paigeon is
Well known to be associated with the memory.
And this is what we've been doing so far, right? We don't have…
Memory prefix for the patient in the collector itself.
I believe it's just, like, separate group of attributes, yeah.
**Pablo Baeyens** 25:56 Yeah.
**Dmitrii Anoshin** 25:57 That's what's…
**Pablo Baeyens** 25:57 No.
**Dmitrii Anoshin** 25:59 I don't think it's… something.
**Pablo Baeyens** 26:06 Yeah.
That makes sense.
And this isn't…
That makes sense, and I don't think we have an… Ish, or anything.
Change dot…
No, we don't. Okay.
So then I'll leave the same comment about the… Brief capitalization, and
Yep, we should be done so then…
We can make progress on those, and we have… This from me, these seconds, I can… Assign…
To you, Christos? Yeah.
The other one that is assigned to Dimitri, that is… Not listed here.
I will… Alright, thanks, brother.
Anyway, we are on time.
**Christos Markou** 27:27 Okay, cool. See you next week.
**Dmitrii Anoshin** 27:29 Thank you, Bobo.
Thank you, Chris.
**Christos Markou** 27:33 Bye.
