SIG: Specification SIG
Date: 2026-11-03
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:10 Hello, Limina.
**Liudmila Molkova** 01:15 I don't know.
**Steve Rao** 01:17 Okay.
**Trask Stalnaker** 01:20 Hey!
**Steve Rao** 01:22 Hey, Traska.
**Liudmila Molkova** 01:26 Even bots disappeared from this one.
**Trask Stalnaker** 01:29 I think the bots disappeared ever since we moved to the LFX Oh, but you said this is the old… oh, this is a… this is the Specification SIG meeting?
**Liudmila Molkova** 01:44 Oh, Specification?
Oh!
**Trask Stalnaker** 01:46 That's what it says on the Zoom.
**Liudmila Molkova** 01:50 Oh.
**Trask Stalnaker** 01:52 Oh well, who knows where… categorized under, recordings, but I'll, whatever. Doesn't matter, yeah.
How are you doing, Steve?
We're not.
**Steve Rao** 02:03 Of course, thank you.
Yeah, good afternoon, yeah.
I also sent the link to Huxing, I'm not sure whether he can join today or not.
Yeah, he, told me the link is, expired today.
**Trask Stalnaker** 02:24 Yeah, sorry about that. That's, those… I'm not used to the new meeting, system.
we have with the Linux Foundation.
**Steve Rao** 02:37 Yeah.
Yeah, I leased, PR, on the agenda today.
**Trask Stalnaker** 02:55 Well, I will share… let me… Pull that up.
Agent skill identity attributes. Yeah. Yeah.
So, I don't know if… nobody else has seemed to be… Interested in this right now.
you know, Ludmila and Ira, Pushing on the, the stabilization stuff.
**Steve Rao** 03:35 Okay.
**Trask Stalnaker** 03:38 But I'm kind of curious, do you know, like, why it's a… I'm just trying to think how we can, you know, if you can… Find other people in the community who also need this, whether other… That can help.
To get, you know, the ball rolling, if you can get somebody else to review it who needs this kind of thing.
**Steve Rao** 04:04 Hmm, okay, yeah, you can scroll down, and I also found us… Similar PR… scroll down, yeah?
Yeah, tell you to, yeah, tell you to… Oh,
**Trask Stalnaker** 04:20 Okay, good.
**Steve Rao** 04:20 And, Yeah, you mean, yeah, I can discuss with, with them, and, yeah, to review the, its other, skill-related PR, and, But, I think, maybe he doesn't have the permission to approve the PI, how to…
**Trask Stalnaker** 04:48 That's okay. Anybody can approve it, it just… if you don't get a, You know, you'll get a gray checkmark instead of a green checkmark.
But it's more about trying to get, kind of multiple perspectives.
from people on the PR, because it's hard for us when there's only one person who seems interested in something, it's hard for that to become, you know, a priority.
**Liudmila Molkova** 05:24 Yeah, I think for the ADK folks are interested, and they added the skill name and the skill resource here, right?
And I think it works with the… Google Cloud Agent Registry. I'm looking into, also, Azure, skill… Inventory.
And it sounds like the URI would be the ID for this use case, where you kind of have this giant place where the skills are stored or registered. What is the story for ID? Why… what is it?
**Steve Rao** 06:10 You, you mean, yeah, why… why is… it's, necessary to add the ID, scale ID? Yeah.
Yeah, because, you know, I, I think, yeah, maybe, it's necessary to recapture the, identify of a skier.
Yeah, skill ID can identify the unique skill.
**Liudmila Molkova** 06:45 Yeah, but in the same way, the URI… Would identify it, where the name can be unique.
**Steve Rao** 06:55 Yeah, maybe it's, unique, but in some scenarios, yeah, maybe, it will come across, Collision with others, skill, StalNet, maybe.
**Liudmila Molkova** 07:19 Let me ask it in a different way, so… from GCP, and it seems, Azure perspective, there is no ID.
And what they have mapping to the name and your array. Is there, use case… existing one for ID. I see how it can be here.
an appearance somewhere. Is there a specific example where there is an ID?
**Steve Rao** 07:51 Hmm… Yeah, you, you can, you can go back to the description.
And I list some, examples.
Yeah.
Fantastic.
**Liudmila Molkova** 08:06 But for… for ADK, there is an attribute for this, for OpenAI… okay, let me see…
**Steve Rao** 08:12 Yeah.
**Liudmila Molkova** 08:43 For OpenAI, it's the idea of the skill version.
Oh, there is a SKU ID.
Identifier of the skill for this version.
**Trask Stalnaker** 10:20 It might be worth, I mean, you can reach out to… you could try pinging Felix, who's been participating in the SIG from Anthropic.
Hmm.
I'm trying to think of… Yeah, just to try to get more, like.
from what Liudmila's saying, this might not be… the best example here.
**Steve Rao** 10:56 Hmm… Okay.
**Trask Stalnaker** 10:58 And what, go ahead.
**Liudmila Molkova** 11:02 Pointropic and OpenAI, it seems, yes, there is a skill ID. For ADK, it's the… another attribute.
**Steve Rao** 11:10 Hmm.
**Trask Stalnaker** 11:12 And so this is different in addition to the skill name.
**Liudmila Molkova** 11:19 It… it seems so… it's the… if I understand the anthropic case is that You register as Keel.
And you probably can give it a name, but then it returns the identifier of the skill on the entropic side that you can later reference.
And it's, it's not the URL, and it's, it's, it, it's, like, some ID.
So this,
**Trask Stalnaker** 11:50 I see, it's like a hostage.
**Liudmila Molkova** 11:51 I've posted.
**Trask Stalnaker** 11:52 A hosted skill.
**Liudmila Molkova** 11:54 Yeah.
**Trask Stalnaker** 12:23 Okay, so, oh no, but this is, agent name skill… I see, so you don't have a skill name, you have a… you referenced by a skill ID.
**Steve Rao** 12:35 Yeah, maybe, skill name, just, it's listed, yeah, on the top of the… Yeah.
Yeah, there is a skill name, yeah, financial…
**Trask Stalnaker** 12:51 Where's the skill name?
**Steve Rao** 12:53 The first light.
Amazing.
**Trask Stalnaker** 12:56 This one?
**Steve Rao** 12:57 Yeah, I guess.
**Trask Stalnaker** 12:58 I think this is… I think this is the agent name.
**Steve Rao** 13:01 Agent…
**Trask Stalnaker** 13:04 And these are the skills you're… Supplying to the agent.
**Steve Rao** 13:09 Oh, okay.
**Liudmila Molkova** 13:11 So it may be in a name, it's just… ugly itself.
**Trask Stalnaker** 13:32 I mean, IDs and versions make sense, broadly.
**Liudmila Molkova** 13:44 Yeah.
**Steve Rao** 13:47 Yeah, sometimes, in some scenarios, yeah, maybe the scale name is not a unique, unique value, yeah, in some scenarios, I guess.
**Trask Stalnaker** 14:09 Yeah, I, I, I just don't know if, we'll get again, this week and next week with KubeCon.
Whether we'll… Have time to really… for the two of us to necessarily… I don't want to speak for Limila, but to… Review this, understand this, so if you can, find some other people who are interested in.
**Steve Rao** 14:35 Okay.
**Trask Stalnaker** 14:36 discussing and… trying to move it forward, that would be great.
**Steve Rao** 14:41 Okay.
Yeah, I can, it's… Out to the Felix, yeah, you mentioned.
In the Slack.
**Liudmila Molkova** 14:52 Yeah, and mind adding it to the agenda for tomorrow's call, just there is this next… topic, at the top. I'll put it there.
So, we'll just call out that there is this PR, and if people are interested, they can share.
**Steve Rao** 15:09 Okay, thank you.
**Trask Stalnaker** 15:10 Yeah, I advertised it last Tuesday.
**Steve Rao** 15:14 Senku.
**Trask Stalnaker** 15:16 And, yeah, we'll try again.
**Liudmila Molkova** 15:22 I remember you had a PR about the user ID, and we didn't come to any conclusion. Is it still something that you were…
**Steve Rao** 15:31 Yeah, yeah, yeah, I had, some comments, yesterday, and, yeah, I think I can… If, if you have time, yeah, you can, take a look, and, yeah, I can, provide more some… content, I plan to do it today.
Yeah.
**Liudmila Molkova** 15:58 Okay, so send.
**Steve Rao** 15:58 I left the comment. Yeah, you can scroll down.
A scroll, yeah, here.
**Trask Stalnaker** 16:26 So, I forget what… So we have user ID… Did we end up… we also have… And she's your deprecate, okay.
I just forget if… okay, so we do have end user IDs separate, so user ID… Is sort of available.
But we have kind of a general semantic convention question always with Around user idea of, like, which… user… That means…
**Steve Rao** 17:15 Yeah, yeah, after the discussion last time, yeah, maybe, I think it's necessary to, to add a new ID, yeah, JNI user ID, and we can narrow the scope of this ID, and don't, Related to the, general user ID, yeah, just like a local set, maybe in some scenario also. So user ID, reference, always user ID, something like that.
**Liudmila Molkova** 17:57 And then what it means is whatever the framework has cost user ID we would put here.
**Trask Stalnaker** 18:14 Yeah, so, I mean, is it… Steve, is it the user who is… Running the… Agent, or is it the… User that the agent is running as.
If that makes sense. Like, the… like, is it the permissions?
That the agent is running as.
Or it's the end user, or it's the user, like a… end user… sorry, I'm probably confusing things, because I haven't read this, so I will…
**Steve Rao** 18:52 Yeah, maybe, my idea is, yeah, it's, yeah, it's, It's, it's maybe, like, Yeah, in the agent system, and there are a lot of users, they, yeah, use the agent to, invoke the LIRM, and, yeah, in some, in the agent, I want to calculate, how much token, its users use.
And, so, yeah, maybe in some framework, if they can pass the, user… if the user of the agent, ID to the system, and we can, capture the user ID and, to calculate the, token, how much they used, yeah.
This is my… okay, yeah.
**Trask Stalnaker** 19:52 Yeah, yeah, okay, this makes sense to me, yeah, and it's… That's more, like, the thing I was confusing it with is more the, like, identity.
Versus user.
**Steve Rao** 20:07 Yeah, maybe, if I remember right, yeah, in JNI semantic convention, there is a, attribute to capture the Asian identity.
Called, Agent Nan, if I remember right.
JNI agent N.
**Liudmila Molkova** 20:25 Yeah, I guess we… we don't… we need a proper story for authentication, authorization, agent identity used for this, but it's not… it's our diagnostic to this. Part of that, yeah.
Yeah for this, it seems like this user ID, it's just that the frameworks have the property for it, it doesn't… necessarily even imply any logic, it's just part of the context.
It doesn't need to participate in inference, it's the context key you can Propagate along with your conversation state.
And it's just that we… Needs someplace to record this useful.
Information.
**Steve Rao** 21:19 Yeah.
And, yeah, I also found in some, scenarios, yeah, the, the requirement, told by our users. They, they… they can provide a user ID, and, from the REST4 API. And, they want to, they ask us to, propagate the user ID in all, spend, something like that, and, they want to, capture the user ID provided by them.
even though the framework don't provide these, attributes, they want to, have an attribute in gene isomantic convention to store this, attribute.
**Trask Stalnaker** 22:19 Ludmila, is it wrong to use enduser.id?
Server side?
Like, if… end user?
**Liudmila Molkova** 22:31 Yeah, I don't think it's wrong, it's just that… We don't know what it is.
there… You know what I mean? Like, we wouldn't…
**Trask Stalnaker** 22:42 Like, we don't… we wouldn't even necessarily need to model that in Gen AI semantic conventions.
what Steve is asking for is, like, not even instrument.
Integrating it into instrumentation, but just customers want to be able to propagate something And have it attached.
Basically, like, a context-scoped attribute kind of a thing.
**Liudmila Molkova** 23:06 Right, for this.
End user ID seems totally valid.
**Steve Rao** 23:20 Yeah, you meant, yeah, in this, case, yeah, maybe end user ID, it's, is valued.
Oops.
**Trask Stalnaker** 23:33 Possibly.
Right, if that's what the… People… that's what… people are wanting to, like, split up token usage by users.
this is, you know, the end user of a system. If they're not asking for integration into, like, frameworks.
And just asking to propagate, like, a context attribute down and stamp it on everything via, like, a span processor or something.
It's an option. Like I said, it's probably… more complicated than when… I don't know that I can… tackle this week or next week, but maybe after KubeCon, we can… Okay. More about it.
**Steve Rao** 24:26 Okay, makes sense.
**Trask Stalnaker** 24:34 Yeah, sorry we don't have the bandwidth. Too many Gen AI… too much… too many Gen AI things.
**Steve Rao** 24:45 Yeah, thank you.
**Trask Stalnaker** 24:47 But yeah, we'll… we'll advertise. Do we have adverta… yeah, we can advertise that one also.
Oh, and Huxing, you have a topic?
**Huxing Zhang** 25:02 Just a quick question about the blog post. I see it is ready to merge, and I'd like to know what we're gonna do next.
Yeah, you look forward, Mike.
**Trask Stalnaker** 25:16 Looks like you have the approvals needed, looks like… They added, ready to be merged, so… They're probably… they get a lot of blog posts, so they try to, like, not… They try to… Not have them, you know, all in one day and spread them out.
**Huxing Zhang** 25:37 Okay, I got it.
**Trask Stalnaker** 25:38 Probably in the queue.
**Huxing Zhang** 25:40 Okay, and just wait.
**Trask Stalnaker** 25:42 I think so. That's my understanding of ready to be merged here.
But if you need, you could reach out in the OTELCOMS channel.
**Huxing Zhang** 25:54 Okay, thank you.
**Liudmila Molkova** 25:57 Thank you.
**Trask Stalnaker** 25:59 Alright, well, we will see you in 2 weeks, at this time.
**Steve Rao** 26:03 Okay, yeah, thank you. See you then.
**Liudmila Molkova** 26:05 Huxing, are you coming to the KubeCon?
**Huxing Zhang** 26:07 Oh, not… probably not this year. I got too many stuff… stuff to do this year, so… Maybe next year. Have a nice CubeCon.
at Salt Lake City.
**Trask Stalnaker** 26:23 gonna be there again next year, too? Is that, like, permanent now?
**Huxing Zhang** 26:28 Oh, really?
**Trask Stalnaker** 26:29 I don't know.
**Liudmila Molkova** 26:30 Mexico, I heard.
**Trask Stalnaker** 26:34 Mexico.
**Liudmila Molkova** 26:34 Heck, yeah!
**Huxing Zhang** 26:37 You mean, next year, the Cubicon North America will be held in New Mexico?
**Liudmila Molkova** 26:42 Yeah, that's what I heard. Maybe I'm wrong.
That's one deal.
**Trask Stalnaker** 26:45 27.
**Huxing Zhang** 26:46 The team.
**Liudmila Molkova** 26:47 November.
New Orleans.
A little bit better, but still…
**Trask Stalnaker** 27:00 Alright.
**Huxing Zhang** 27:01 Alright.
**Liudmila Molkova** 27:02 Good to see you all.
**Huxing Zhang** 27:03 So, you open up.
