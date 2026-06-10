SIG: Network SIG
Date: 2026-06-09
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang** 00:24 Right.
**Sven Cowart** 00:26 Hey, Steven.
**Stephen Lang** 00:37 Mario should be joining shortly.
**Giuseppe Ognibene | Coralogix** 00:51 Hi, everyone.
**Sven Cowart** 00:54 Hello.
Wait a few minutes.
Hey, Braden.
**Braydon Kains (Google)** 01:55 Hey, how's it going? I unfortunately only have a few minutes. This time slot's not great for me in Eastern Time.
**Sven Cowart** 02:01 worse.
**Braydon Kains (Google)** 02:02 I just wanted to come and introduce myself.
**Sven Cowart** 02:05 That sounds good. I think we don't need to take the whole hour, for sure, here. I think that the introductions will just make a little bit of sense, put faces to, the… GitHub usernames that we see. Yep. I think… I think, as far as… next steps here go. I think we just need to figure out what time does work.
And then, maybe catch up a little bit on what the conversation that was had in the semantic convention SIG call on Monday.
I don't know if you got a chance to catch up with Josh or not.
So…
**Braydon Kains (Google)** 02:42 Yeah, I missed that meeting. There's a collector-related meeting that happens at the exact same time that I have to go there.
I usually miss that one. I did… I was just in, just before now, the specifications sync meeting. Okay. Because… and I actually added as, like, a final topic, like.
should this new networking sig be a broad hotel project with, like, a full proposal, or should it just be within the scope of SEMConv?
And I got sort of a… Like, a two-pronged answer.
for, like, if we were talking about, like, developing entire new networking observability, or, like, much, like, a much broader level solution, then it probably should be, but if it's just about the SEMCOMF, then, it's okay for it to just be approved by the SEMCOMF maintainers. That seems to be the answer.
from my personal perspective, I don't do a lot of networking, at least not to the deep level that everyone else does. My… my networking expertise doesn't expand outside of Slash Proc for the most part. So… the… from my personal perspective, I'm mostly interested in the SAMCOF portion. I mainly wanted to organize a space where we could actually move these semantic conventions forward outside of the system group, because we just didn't have time to help, and we were accidentally blocking things. So… Personally, I only care about the ZENCOM.
I don't know how everyone else is feeling, whether… This is… like, a new, broad push for new instrumentation that doesn't already exist, or if this is mostly about, like, standardizing within SEMCOF.
What is everyone's perspective on that?
**RC Robert Cowart** 04:24 So, so our intention actually, was that we, have some… you know, call it collectors, call it whatever when you say instrumentation, you know, essentially a, a flow collector, a SNMP trap collector, and when I say flow, I don't mean the work going on in the, in the OB SIG around EBPF, that is also a source of flow-like data, but I'm talking about, like, NetFlow, Sflow, IPFix, stuff from switches, routers, firewalls, etc, right? Yeah.
a SNMP collector and an SNMP trap collector. Essentially, what you're getting there is metrics, logs, traces from the network perspective, more or less, would be the way we would see that mapping, so…
**Braydon Kains (Google)** 05:16 Right. I believe there are collector receivers for… well, there is one for NetFlow, for sure. I don't remember if there is one for SNMP stuff.
But either way, it's like, it's mostly… we want to standardize the SEMCOMF to make sure everyone agrees, whether it's coming from a collector or we're building something new, everyone agrees what the attributes and metrics and stuff should look like. Does that sound fair?
**RC Robert Cowart** 05:45 Sure, Sorry, I just paused on what you had just said before that, so… I actually think, I think there's a… Prometheus has an SNMP scraper, but again, you know, my thing would be on whatever's existing, is that it doesn't… wouldn't support semantic conventions that we would be creating, so…
**Braydon Kains (Google)** 06:05 Well, yes, we would need to, like, make updates to the… anything that exists.
Based on what we decide here. We're kind of doing the same model in host metrics with the system group, like… The host metrics exist.
The receiver already exists to collect all the data, but it's not standardized, so we're coming up with the standard, and then we're going to go update the receiver to match the standard, and so we probably follow the same…
**RC Robert Cowart** 06:27 You'll just have to forgive me for being a little pessimistic on, Whatever might be existing, so… yeah.
**Braydon Kains (Google)** 06:34 It was likely, like, committed by people whose, like, employer told them to do something and not by someone's, like.
entrenched in the environment. That is typical with these receivers.
**RC Robert Cowart** 06:46 Okay, so we could maybe do a bit more significant work there, potentially.
**Braydon Kains (Google)** 06:51 I imagine… I imagine they would welcome it, in fact, Rob.
**RC Robert Cowart** 06:54 Okay, that's all. Like, whether it's in the official collector, whether it's, like, I don't really care where it lives, I'm just thinking about the data sources.
Combined with the semantic conventions we're working on here.
**Braydon Kains (Google)** 07:07 Yep.
**RC Robert Cowart** 07:08 Yeah.
**Braydon Kains (Google)** 07:10 You know, the, the…
**Sven Cowart** 07:10 I think.
**Braydon Kains (Google)** 07:11 Conventions group tend to care a lot about, like, reference implementations, which is why I'm thinking about what's already there.
**RC Robert Cowart** 07:15 Yeah, us too, exactly.
**Braydon Kains (Google)** 07:17 Yeah.
**Sven Cowart** 07:18 And I think there's two parts, right? There's the code for… traditional S&P trap, low.
And then there is the code for OBI, which is right now producing flow metrics.
And that's the stuff that Mario and… Goo… Guseppe? How do you say your name? I've been trying to figure it out.
Giuseppe? Okay, cool.
Cool, I've been working on, and then I've also been working on this project called Mermin, which really, I've said this before, should have been part of OBI, it was bad timing.
That at the time, OBI was still Bela, and… wasn't committed as OBI, so we were like, well, we don't know how to commit to Bela and all this stuff, and so it kind of happened, but more or less, what I did in Mermin is represent from the interface.
flows as flow traces, which is a new spec I want to propose, and then OBI, but I want to port that implementation into OBI so that OBI can produce flow metrics and flow traces And so, there's work that needs to be done there, but that also needs to be informed by the semantic conventions that we agree upon here. So, really, there's 5 different pieces of Code or instrumentation.
sources, whatever you want to call that, that are relevant to, I think, what would the, network SIG.
Obviously, OB already owns that other stuff, so I'm happy to collaborate in that sake of around… the things that Obi's doing, right? But the semantic conventions need to come from somewhere else.
So… I think… and I think that's, like, kind of the crux of this, is… because one of my questions here was going to be, okay, so… where do we… if we don't want to clobber up the semantic convention.
issue board and agenda on Mondays. Where's the best place to post about this stuff to not make it complicated for them to recognize this is… Network-related stuff that this new group that is by trying to be formed, trying to, Figure out.
**Braydon Kains (Google)** 09:30 So, I unfortunately only have a minute or so left.
the way I'm… I'm hearing it is that like, both things are kind of true, it sounds like there is instrumentation, new instrumentation to be developed and work there, but it needs to be informed by the semantic conventions, so, like, that already in itself is kind of a scoped project.
So I think the… the next step from my perspective is we… don't make a project proposal for just the semantic conventions group, because I think it's relatively scoped that we want to standardize the semantic conventions since they're informing the other things.
if there is new instrumentation being developed that is informed by the SEMConv that we're standardizing.
That's probably the point where we would make a larger project proposal.
I think. So…
**Sven Cowart** 10:27 The reason that the SIG came up, the networking SIG and reviving it, on Monday was that, This effort around standardizing SEMCOM is probably going to be a 2-3 year process to do in its entirety.
Just because of how large the S&MP-related side of all this is.
**Braydon Kains (Google)** 10:47 Yeah.
**Sven Cowart** 10:47 And that's where Josh mentioned, and that's why he changed the status to need SIG, is because he was… he has dealt and worked with S&P. He's like, I… this is gonna go on for a long time.
And we need experts outside of this semantic convention group to do that, so… I'm not sure… I'm happy to go either way.
Wherever there's more buy-in to go the route. But it does feel like something if, because of the scope being so massive for so long.
That it should be something that should have its dedicated SIG?
But if we want to go about it is, let's get the first phase out of the way without a dedicated SIG, and then when the other S&P thing become relevant and start the network SIG at that time, that could make sense too.
I don't know, that's just where my head's at right now.
**Braydon Kains (Google)** 11:45 Okay, yeah, I think I see what you mean.
Yeah, I don't have a good sense about the full… the full scope of this, since mostly I was only thinking about, like.
Introducing a semantic conventions vehicle for this.
if there is more to it, then it might make sense for a general project proposal. Probably… probably something I wouldn't be capable of writing, just because I'm not involved in the estimates. Right.
At the very least, I don't want to, like, block us getting started on this stuff.
On this sort of general, like, broader project, like, whether it should be a project or, like, what the vehicle should be exactly.
**Sven Cowart** 12:21 Yep.
**Braydon Kains (Google)** 12:21 I think at the very least, like, to get us started, like, boots on the ground, we… We can follow the model that the system group does, at least to get started, which is we have a project board, and various labels to assign issues that are in the semantic conventions repo specifically to our project board, and, like, things that we consider blocking our GA, or… or stuff like that.
And I can make up a Slack channel for network… either… unless you guys have a… is there a network Slack Slack channel of any kind?
**Sven Cowart** 13:00 There is a Network SIG Slack channel, but it's basically dead. It's OTEL Network, which is the Slack.
**Braydon Kains (Google)** 13:05 Okay, so we could bring that back, or we could make… or we could make a new one. It's easy enough to make a new one, it's not, like, blocked on being an admin or anything, so I can make a new one, or we can just revive that one.
At least so that we can get We can get started on… On… on work, because it… it seems like we have more than enough support to know that we're gonna start doing stuff, like, that's no longer a question.
so exactly how it proceeds, I'm not sure. I am in the specification channel on the CNCF Slack. I'm gonna… because my topic was last and we ran out of time, we didn't finish discussing it, but I'm gonna post there, and we're gonna keep discussing, like, whether this should be… a full project, or, like, exactly what… what shape this should take, so… People could follow along… follow along on there, that would help.
**Mario Macias** 13:57 Okay.
**Sven Cowart** 13:58 Send… does anyone have an opinion where we should communicate in Slack?
**RC Robert Cowart** 14:02 I'm okay with just reviving the hotel network. I was about to join it, actually.
**Mario Macias** 14:10 Yeah, not… not… I don't… I don't mind whether the auto network or a new channel.
**Stephen Lang** 14:17 Well, try the current channel. If they complain, we can always… Create a new one later.
**Braydon Kains (Google)** 14:22 Yep. Fair enough.
**Sven Cowart** 14:23 Yeah.
**Braydon Kains (Google)** 14:23 It's easy enough to make a new one if we really want.
**Sven Cowart** 14:27 Okay.
**Mario Macias** 14:27 Okay.
**Sven Cowart** 14:29 I suppose the only other question I have, and Braden, if you need to go, this is fine, we can Slack about it, but… If it's handled through the regular semantic conventions group, do we need any approvers or anything like that, like, people who could actually approve these things that won't… require… Constant pestering of.
Others that are less interested in this.
**Braydon Kains (Google)** 14:54 Yeah, that would be ideal, and I'll bring that up. When this first came up as, like, we should… as, like, I suggested in two semantic conventions meetings ago that, like, we should start this group up, and I said, I'm not a… I'm not a maintainer, though, should we… should we get, like, a maintainer or approver or something? Yeah. And Lyudmila said she was fine delegating to me at the time.
**Sven Cowart** 15:18 Okay.
**Braydon Kains (Google)** 15:18 I don't know if that'll still be true, because it sounds like this group may be growing to a larger scale than she realized, so I might need to bring this… bring this back up.
**Sven Cowart** 15:29 Okay. Alright. Yep.
Sounds good.
**Braydon Kains (Google)** 15:33 Cool.
Alright, yeah, I definitely gotta get going. But, great to meet everyone, and we'll chat more soon.
**Sven Cowart** 15:41 Sounds good.
**Braydon Kains (Google)** 15:42 Thank you.
**Sven Cowart** 15:43 Take care.
**Stephen Lang** 15:43 Thanks.
**Mario Macias** 15:45 Yeah, thank you.
**RC Robert Cowart** 15:47 Alright, bye.
**Sven Cowart** 15:48 Nice to meet you guys. I don't know, I've met some of you already. I think actually everybody here I've already met, but yeah.
Alright, take care.
