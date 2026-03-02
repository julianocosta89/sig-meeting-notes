SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-09-17
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:12 Richard.
**Morgan McLean** 01:19 Hey, Ruger.
**Ruediger Schulze (IBM)** 01:34 Indeed.
Let's here.
Meeting notes.
So, what do we have for the agenda? Let's look.
Hmm.
So, I've seen from…
From crack, the issue to request organization membership, this needs to be processed, so this will… but it's… it's been submitted, it's open. So this is good.
On the PR1898, our TPS one, there are a couple of additional… Updates by, Ludmila.
From the semantic convention SIC,
I need to still respond to them. I think some of these comments that she had, they actually reflect aspects which we also have seen internally.
There was one that I wanted at least to mention here. Let me just briefly find that, and then I share my screen.
Right. Where's the screen sharing?
Here.
Hey, Craig.
Thanks for joining.
So,
You… so I'm on this TPS PR. There's a couple of comments, some of them, they are more generic, some of them are also more informational.
But there was one which, I think is, interesting. So initially, we have been…
putting here… the… in this case, the KICS-specific protocols.
Into network protocol name, and as well in rp e.system.
But, if you think about that.
In some way, this is very much specific, in fact, to TPS, or to, in this case, KICS.
And, It might actually be reasonable to put this under a more TPS-specific attribute.
And,
this is something that I just wanted to briefly mention. I will… when I update this, I will put in what we internally discussed, and on the next week, I would suggest that we take a look at this from a SIG point, a mainframe SIG point of view, just that everybody has seen this.
I hope that's okay with everybody.
Okay.
Let me see what else Right.
Yeah, there's also the, you know, we had this discussed here, this is for OTME, this is the IMS. I mean, these are very specific ones, obviously. Again, maybe reasonable to put this on the… not our PEC system, but other…
attributes.
Right.
Okay.
Yeah, so, I put the updates in, Mike will also post this to the Slack channel, and everybody can take a look at that.
So,
This is this,
Yeah, I said this last week, so we are looking to submit a PR for MQ and DB2.
DB2 isn't sitting in my inbox, MQ is, with some… somebody else, but that will come in the next days.
Survey has been sent to me. I think it hasn't been published yet on the OMP website yet. As soon as it's being published, I will open the PR, but I wanted to take her edits in. Usually, May also has, from an OMP site, some edits, so I didn't…
I wanted to lose them. And then in terms of metrics, semantic conventions.
As we also discussed last week, we also, throughout the week had a discussion around that.
So… Let me open this.
What we are thinking is, and also wanted to briefly discuss this, it's probably best if we, you know.
submit small PRs, and, you know, we can go here by… by these different processor types, as we discussed the last time. It's probably the best if we submit a couple of small PRs to the semantic conventions, first of all, discuss them here in our group, but…
You know, it's not visible here on the screen, but this would be the CPU type attribute, and it's probably reasonable then to discuss should be this system CPU type. I think, Richard, you asked last week, or was it Craig, how…
GPUs are being represented. I think this is still one question to be answered. But…
by doing so, by adding these… these… you know, it's not many attributes to start with, but I think by putting these small PRs in, I think we will get a better understanding of how to represent these concepts with different processor types, and we could also have,
memory might be an example. Here we have some hardware-related environmental parameters, or in fact, in this case, metrics, but then I think we get a feel of how to move forward with these activities.
Okay, that's it from my perspective today.
Anything else you want to discuss today?
**Morgan McLean** 08:35 I didn't have anything immediate, though, like Rudiger's or anywhere where…
like, I or others can assist with things?
**Ruediger Schulze (IBM)** 08:43 Exactly, yeah, I mean, this would be, you know, these small PRs would be one topic, right? I mean, they kind of like…
You know, this is about two attributes to put in and.
**Morgan McLean** 08:55 Yeah.
**Ruediger Schulze (IBM)** 08:56 Get a feedback on… Should we do it this way, or, you know, we could also start with…
system… I think this is the entity type, because I didn't want it to look at yet. Entities is, you know, the next step, but, you know, is this system CPU type, or is this maybe mainframe CPU type? As I also mentioned last time,
we… we had this discussion around terminology, I mean, where it's… and obviously semantic conventions also go in this direction, where it's possible to apply common names and common schemes. We wanna… we wanna follow that as well here.
Right.
Exactly.
Good.
Yeah, so yeah, for those who are on the call, please feel free to crop one of these, and we can also, you know, help and assist to get this ready.
Good.
Then I think we, you know.
Don't have any other thing to discuss today, so maybe we just take back some time.
**Morgan McLean** 10:15 Okay. Well, I will take a look at the PRs. I know nothing about mainframes, so I don't know how useful it'll be. I will probably just blindly approve them.
**Ruediger Schulze (IBM)** 10:24 It's.
**Morgan McLean** 10:25 Better than nothing.
**Ruediger Schulze (IBM)** 10:26 Yeah, but then we, at least we, you know, we get feedback from the Somatic Convention Center. I mean, as you know, Morgan, we were discussing this, I believe, last time. There's a lot of things happening around entity, and we still try to get our, kind of, like, head around what that really implies.
But I think it's good that entities will be there with also these additional ways of expressing relationships, and also the identifying attributes, I think this will help us.
to be more specific in the description, so it's good. It's just, you know, as a… as a sick year, I think we want to follow this where the community is currently moving with this, and then…
Put our peers forward as well.
Okay, good. Then talk to you next week, and yeah, then hopefully we have a little bit more next week. Okay.
Thank you.
**Morgan McLean** 11:23 That's good, guys.
See y'all later.
**Ruediger Schulze (IBM)** 11:26 But…
**Greg Shriver** 11:26 Bye.
