SIG: Governance Committee
Date: 2025-08-27
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/P9eC7DS0qWbKX-prNH_zQczq04kPs4tiUK0L8w1Nx1qy4xybZxRB0DHv92_OVMc-.rp5QuhOYt_G6PmGA
============================================================

## Zoom Recording Transcript

**austinparker** 00:20 Whoa.
**Trask Stalnaker** 00:22 Hey, folks!
**austinparker** 00:24 I'm repping the hotel lab coats at GopherCon.
**Trask Stalnaker** 00:28 Nice.
**Juraci Paixão Kröhling** 00:31 What are you?
**austinparker** 00:32 I'm at Gophacon. I got….
**Juraci Paixão Kröhling** 00:34 Oh, my ocean.
**austinparker** 00:35 hotel lab coat.
**Juraci Paixão Kröhling** 00:36 Yeah, nice.
**austinparker** 00:38 So everyone knows which… so everyone knows who to, like, throw things at.
I've got… I've gotten less, feedback than…
than I thought I would, but…
I think that's mostly a lot of, And the acceptance of checks.
I actually just talked to someone that, was telling me about what they're doing with OTEL, which is really cool. It's, they're building, like, a data lineage system on top of OTEL.
**Trask Stalnaker** 01:12 We've had that request.
**austinparker** 01:16 Yeah, I'll…
Yeah, I was talking, I was telling him about, like, I think you should pay attention to the…
… event stuff, the typed event stuff, because I think that would be really helpful.
**Morgan McLean** 01:40 Austin, where are you?
**austinparker** 01:42 I'm a gopherCon.
**Morgan McLean** 01:44 Cool.
Where's it?
**austinparker** 01:45 It's at the Traffic Center.
**Morgan McLean** 01:49 The what?
**austinparker** 01:50 Savitt Center. It's out in New York.
**Morgan McLean** 01:51 Oh, cool, thanks.
**austinparker** 01:54 I… I didn't even realize it was in New York. This is, like, the first East Coast one they've ever done, actually, which is interesting.
…
But I saw, like, 2 weeks ago, I saw that it was posted, that it was in New York.
someone posted about a talk, and I went and looked, and I was like, oh, it's in New York, and oh, there's, like, a couple talks that involve OCEL, so, well, I should go and talk to people about OCEL.
And give out Snickers. I've been giving out, … remainder…
Do we Paris stickers? Paris? Yeah.
And then I had a couple of, … Charity major specials.
I gotta go from my kid.
**Trask Stalnaker** 02:52 Right.
**austinparker** 03:04 A lot of people talk about AI here.
**Morgan McLean** 03:09 Is anyone not talking about AI there?
**austinparker** 03:13 Those are people talking about, like, dope channels.
**Morgan McLean** 03:15 Huh.
**austinparker** 03:24 I'm gonna say, the stressing lack of smarts….
**Morgan McLean** 03:35 Did we want to get started?
**austinparker** 03:37 Yep.
**Morgan McLean** 03:41 I don't see….
**Trask Stalnaker** 03:42 We don't really have an agenda. I did put something in our,
Slack channel, but why don't we start with triage?
I can share…
Virtual Agenda, review, work.
Project board…
to do… In progress…
This one I just heard back from… we had tried to roll out the EZCLA, co-author checks.
And it caused problems, so we rolled it back, and they got back to me, this morning saying they had
Fixed those issues, so… I… Asked,
to… I gave them a list of, instead of rolling it out to all repos.
This time, rolling it out to a specific set. Specifically, I picked the ones that,
had requested either, I'm a maintainer in, so I can monitor, or, ones that had requested the co-pilot, co-author, I mean, the co-pilot.
Coding agent.
Where, which is where this discussion came from.
So I imagine it's okay now. we'll give it a…
few days, but if it kind of sticks, then, I think it will be… we can enable the… re-enable. Oh, I guess the Copilot coding agent was already
Enabled in some of these.
Or we had rolled it back for some. Anyway, I'll follow up, that's… I think it's… Progressing.
I don't think we have, definitely there's a bunch of new stuff in the roadmap stuff that, Dan's been working on.
And then graduation. Anything, Austin, that… We should be aware of.
**austinparker** 06:20 ….
**Trask Stalnaker** 06:21 working on….
**austinparker** 06:25 I believe we are… hot tub, …
I got the one of those tickets…
They have finally started to get some of the adoption reviews scheduled and done. …
It's like, yesterday, actually, they finished the first adopter interview, and I have 3 more scheduled.
**Trask Stalnaker** 06:51 Is that the very last thing, or is there anything else that….
**austinparker** 06:57 I think the next step after that is public comment?
But I believe the adapter interviews are, like, the… it's, like, the very last part of the…
I think it's the very last part of the POC process.
**Pablo Baeyens** 07:15 Is there anything we need to do with the, like, security thing you asked about?
**austinparker** 07:22 I think we should… I think the two things there is…
We should consolidate those. See, there were duplicates.
Or there was, like, dude, we should make sure there's a single source of truth, and then… I…
Just do, like, a status update.
On each of them?
Okay.
**Pablo Baeyens** 07:44 I can do the latter for the collector ones. I guess…
I don't know. I think they were off.
**austinparker** 07:49 collector ones, weren't they?
**Pablo Baeyens** 07:52 … there was… there were so many, like, the Go…
repo… I don't know, I can do it for all of.
**Trask Stalnaker** 08:00 Can you share the list?
**austinparker** 08:02 Yeah, ….
**Pablo Baeyens** 08:04 Yeah….
**austinparker** 08:06 I'll put it in the Zoom chat.
**Pablo Baeyens** 08:08 Okay.
**austinparker** 08:09 If you open that… Boss.
**Trask Stalnaker** 08:19 Okay, so they're all over….
**austinparker** 08:21 I don't know if these are…
I think maybe the SIG security ones are ones I opened, and then, like….
**Pablo Baeyens** 08:29 Yeah, some of the ones that you opened, I had already opened on the….
**austinparker** 08:32 Right, and I think it was just, like, I wanted… I think somehow….
**Juraci Paixão Kröhling** 08:35 Can you hold?
**austinparker** 08:36 I wanted them to be in, like, one place.
**Juraci Paixão Kröhling** 08:39 And maybe as long as, like, the….
**austinparker** 08:42 … Maybe as long as the ones in 6 security just link over to the other ones, that's fine.
**Juraci Paixão Kröhling** 08:51 So, there were a few comments on… about those ones. We have a thread on, perhaps, Slack about those, like the dialib, I know that we talked about it before.
the hardening recommendations, we talked about it as well. They ultimately said, it's okay, there's nothing to do, because the way that we are doing things is…
is… Not open to those attacks.
…
We have to go back to that thread. I think we had a Slack channel, or a specific channel with them.
But those are all handled, so everything that was on that report was handled.
**austinparker** 09:31 Yeah, as long as those issues… then those issues need to be updated with that and, like, closed.
**Trask Stalnaker** 09:42 And it does look like, they're all collector ones. These 5… there were 5 in SIG Security, and 0 through 5, and there's 5…
… 0 through 5… 1 through 5 across collector releases and collector repos.
**austinparker** 10:04 Training.
….
**Pablo Baeyens** 10:09 I can deal with those. Can somebody else decide which of the duplicates we keep?
Like, sick security, someone from Sikh security.
Or us, I don't know.
**austinparker** 10:19 I think as long as… I think it's fine for them to be… I think just the SIG security ones need to link to the other ones.
And then
Then the other ones need to be updated and closed, and then we would close the security ones with the…
Nothing's inside.
**Trask Stalnaker** 10:42 So do you think it's okay for me to close this as a… and say that it's being tracked over….
**austinparker** 10:49 Oh, yeah, that's probably also fine, just as long as there's, like, a pointer to it. Again, this is all documentation, and…
Yeah. Okay.
**Trask Stalnaker** 11:01 I'll take care of the, SIG security.
**austinparker** 11:04 Security ones? Thank you.
It sounds like we have two different private things. If you want to go ahead and….
**Trask Stalnaker** 11:17 Yeah.
**austinparker** 11:17 Privacy.
**Morgan McLean** 11:22 Yep.
**austinparker** 11:22 I can go ahead, I'll start a call. I'll definitely introduce some chat.
**Trask Stalnaker** 11:26 Thanks.
**Morgan McLean** 11:27 server.
