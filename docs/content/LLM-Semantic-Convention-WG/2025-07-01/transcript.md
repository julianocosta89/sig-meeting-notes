SIG: LLM Semantic Convention WG
Date: 2025-07-01
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/L-eQeVhcmE6bBNhPk0ger9l2IVz9EvTGO2dJIypmxRjYTLPutPTUhA2i93k-GflN.brDbLt0mpYl4-T7z
============================================================

## Zoom Recording Transcript

shiprajain 00:00:59 Hi! Everyone.
Liudmila Molkova 00:01:25 Hi, folks.
okay, let's give people a few minutes to join.
and then let's get started. I'll pull up meeting notes.
Okay, here we go, so if you have anything.
please add it to the agenda, I'll create it in a sec.
Welcome to July. By the way.
please add your name.
I'll spend a little bit of time on the triage, and let's see what we had from the past.
Giovanna Carofiglio, Cisco 00:03:19 Hi! Everyone.
Liudmila Molkova 00:03:21 Hello.
okay. So we are almost at 5 post hour. Let's get started so let's take a super quick look at our Project Board. We'll spend more time on the project planning later.
There is nothing new in the issues which is wonderful.
And let's move on.
Shipra, I I intentionally wanted to leave some space before the long discussions. Can I put your first.st
shiprajain 00:04:41 Sure.
Liudmila Molkova 00:04:48 I'm wonderful So do you want to get started? And folks, if you have some small topics to discuss?
Some prs to bring attention to just add them to the agenda. We'll see what we can get to.
Yeah. Then, Chipra, go ahead.
shiprajain 00:05:17 so here is the document that I had created 2 weeks ago. And I have also given edit access, I hope, you all will be able to.
Now, share your comments.
Okay, I think you're sharing. So should should I share or
Liudmila Molkova 00:05:37 Do you want to go through it? Then feel free to share.
shiprajain 00:05:40 Yeah, yeah, let me do that.
Okay.
so I think I've covered a quick background on this work already. But this work is basically focused on improving the tracing and observability needs to enable white box observability for multiagent system. We have seen a couple of standards available for single agents in open telemetry, semantic conventions already, but not to capture the patterns, and how the multi agents interact within a multi-agent system.
and to be able to capture the traces at each level, so that we can enhance and use that for white box observability and maybe evaluation. Going forward, we saw some gaps, and that's what we intend to cover in this document.
So that's what I'm mentioning that the goal of this document is to identify the gaps or fill the gaps of the server side telemetry while building multi-agent system.
This work was, basically inspired from you know, a 2, a framework on agentic systems. Also, we looked at the existing telemetry from different agentic frameworks. Some of them are listed over here which we initially reviewed, but now we have actually seen quite many others, also autogen, semantic kernel from Microsoft, azure AI services from Microsoft, and some of the other non azure agentic frameworks like small Agent Lang Graph Agno very recently, crew AI, so on and so forth.
and we also looked at how the visualizations can be achieved with the help of aggregators like Arise and Langfuse. So from looking at you know what is being spoken in the industry, and while we worked with some of our external stakeholders, who came with very specific asks of enabling white box observability at the server side. This proposal came in the picture.
Now there are 2 parts of this proposal. We wanted to ensure that we can leverage as many conventions and science which are available in open telemetry already. So as part of this proposal, we also wish to give the standardization on how we can reuse the open telemetry existing conventions. At the same time we are giving a proposal on what should be added, as new spans, attributes, and events to the existing Jenai namespace.
Now, in order to also materialize this proposal, we have been you know, doing pocs on a real time inspired travel bot multi agent system. We will come to that in a short while.
At the same time we understand that there can be complexity involved when we're talking about multi agent system. Hence we would want to scope it out. So right now we're talking about building a multi agent system where you know an agent calling an agent or agent calling tool how that entire depiction should be converted into tracing it could soon grow into conversational, which is, multi turn multi agent system.
And again, how we would want to achieve the tracing with different patterns involved. Some of the common ones, like orchestrator based concurrent, hierarchical, and and then each of the agentic frameworks have some specific patterns like swarm or iterative planning.
so on and so forth. So our intention is to be able to come up with the unified, tracing mechanics for which which is applicable for different patterns.
Now, having said so, I would quickly flash on what we can reuse. So currently.
Liudmila Molkova 00:09:58 Ship, I think, just for the sake of time, I think we we can review most of the tiny details offline. I just wanted to bring up that there is another doc from Cisco.
It's actually the same discussion between for the multi agent system. Right? So I wonder how we can organize this work so that you folks can maybe collaborate together and come up with something in common and agree on this and we we really don't need to go into the tiny details during this meeting. We can do this offline. So maybe you want you, wanna check did. Have you? Did you know about this effort. Can you share your goals? And maybe we can merge this 2 work streams together.
shiprajain 00:10:51 Sure.
Pavan 00:10:52 Oh!
shiprajain 00:10:52 So I'll stop sharing. Then.
Pavan 00:10:56 Yeah, I think I've basically looked at it. you know, we read through it during the last sort of proposal. But I I believe that our proposal sort of differs a tiny bit. With respect to what? Microsoft, where?
Proposing with respect to the whole multi agent observability. But you know definitely, I think we could probably see what could be some of the overlaps, and then, you know, give a combined proposal if needed.
Sergey Sergeev 00:11:33 Yeah, maybe we could use some application which both Microsoft and Cisco are using for basically to define in the spec and see what's different in both proposals specifically, which attributes I introduced I introduced, which are different from semantic conventions.
Pavan 00:11:58 Yeah, are you able to see my screen.
Liudmila Molkova 00:12:01 Yep.
Pavan 00:12:03 Okay?
So just to give a very short intro, I think. We as a part of Cisco we have been working on a collective open source collective called Agency which you know, has been going on for some time. Where? We have been working with a number of partners and collaborators to effectively, you know, like sort of help, reshape the whole multi agent space as you as you may. As you imagine. So we felt that, you know, going forwards, there'll be a lot of different individual agents that do specific work. But there isn't necessarily, you know holistic stack, or, you know, like a solutions that will basically help the developers.
you know, have, like a unified view into how the agents have been working. Give them, you know, some sort of a idea about or rather, you know, ensure that the agents are able to collaborate, you know, with together seamlessly. And you know, basically have, like a directory service of sorts where discovering agents trying to identify, you know, like agents depending on a use case or a skill becomes easy, so on and so forth. So there have been some few efforts in that regard. I think Cisco has been one of the founding members of the a 2 way, you know, project that recently went into Linux Foundation.
So we have been trying to figure out how best to, you know, collaborate some of the efforts there. So we, you know, inside Cisco, along with Giovanna and couple of others, and you know, with Sergey as well, very recently have been trying to work on this multi agent system observability. But this proposal would probably be multi agentic. But I think you know it could be.
you know, extended, or rather, you know let's say, expanded to the single agent system as well. So I think you know, what we initially wanted to do was okay. The current existing like sort of metrics. The events traces. That sort of, you know, collect individual Llm operations today. Would probably be like, you know, could be insufficient, you know, for some of the diverse needs for agentic, you know, systems as a whole, and we have been trying to figure out how these could be, you know, like sort of augmented, the semantic conventions be augmented such that theoretically all the sdks could sort of have some of these instrumented optionally which will give the developers, you know, like a holistic idea about how their.
Sergey Sergeev 00:15:10 Bye, bye.
Pavan 00:15:10 Have been. Yeah. Sorry.
Sergey Sergeev 00:15:12 In the interest of time. Again, let's publish this document as well in the Gen. A instrumentation channel, once work and have the review. So my, my immediate feedback, we need just side by side, comparison between those 2 proposals, basically what already is present in open telemetry.
semantic conventions, and what's introduced new.
I think it's great that agency as a project already created, some of the applications, and etc. We can just identify how the telemetry will look like with agency proposal. And what's missing in semantic conventions? Let's do this work and publish it in the Channel, so we can review it side by side.
Liudmila Molkova 00:16:07 I. I also wonder if you folks can can kind of work together. And in the smaller feature, crew as a part of this, or because just maybe you would have more things offline, and you would compare notes. Would it be interesting to Microsoft folks and Cisco folks.
Sergey Sergeev 00:16:26 Yep, it would be great. I think it's.
Liudmila Molkova 00:16:30 Hey? Deal.
Pavan 00:16:34 Sounds good, so.
shiprajain 00:16:36 Yeah, Lyudmila, I had a question like, I think one of the starting points can be to review each other's talk and start sharing comment.
What other? What is the usual way for intercompany folks to come together and.
Liudmila Molkova 00:16:53 Work together.
you can use slack. You can use any of the like there is, for example, huddle. You can call each other in slack. There is no protocol, right? So like, if definitely, there is some private information we can share from Microsoft side. I'm sure Cisco folks would have the same limitations somewhere, but we just don't share what we can't, and we share what we can.
I'm like, if you want to include me, I will be happy to facilitate those discussions between you. But if you don't me, then just go without me like slack. Are you on the Cncf slack.
shiprajain 00:17:36 I I think I'm not. I have raised a request to join a slack today. But I'm not sure if I I'm there yet.
Liudmila Molkova 00:17:45 Oh, okay, you you usually don't need any permissions to join slack.
so you can just go ahead and sign in, and then let me find the link. Yeah.
Sergey Sergeev 00:17:58 Link is in the Google Doc. For this open telemetry. Lm. Sig.
Okay, let me use that.
The links may not work.
Well if you just try to link to the channel.
Liudmila Molkova 00:18:15 Right. So because I'm signed in, it will bring me to the slack. But for you it will ask you to sign in and then it will bring you here.
So you should not see any roadblocks for for joining slack and or starting to collaborate. This is our genie Sig. Instrumentation. So, Jenny, I channel feel free to post here.
comment and anything else. And you can definitely chat with other folks.
shiprajain 00:18:47 Awesome.
Liudmila Molkova 00:18:48 Horos! On slack.
shiprajain 00:18:50 Cool sounds, good.
Liudmila Molkova 00:18:54 Is there any anything immediate we can do here to help you folks work together, or any immediate concerns you would like to figure out during this call.
shiprajain 00:19:09 I think I would like to understand the expectation when we talk about like converging the idea right? We we both of our documents. So we I think initial days would be to go over the documents and understand the commonalities and the differences, and then how we can bring it together the other part would be what is the expectations for in the next call? Should we try and come up with some kind of a Poc which shows how the proposed trace is actually emitted from any of the agentic framework. So yeah, in terms of expectation to take it ahead. Also, I want to understand. So we'll work together to achieve that.
Giovanna Carofiglio, Cisco 00:19:50 Yeah, I just wanted to mention that. Our proposal is mirroring the code that we have released with some sample apps in this agency open source initiative. So this is 1 1 way to to seeded implementation in case.
Liudmila Molkova 00:20:14 So I think the the thing I would like to see is a consensus on the high level.
What are we doing? What are the key pieces of work.
the attribute naming core metric naming.
That's not make sure I'd done this yet.
I, personally, I take it, with a grain of salt. I would like to see a some sort of a demo that shows an agent talking to each other, and how it works, and maybe some code. And ideally, if it's some prototype of the instrumentation that's that's not like. It's not the application which emits spans or events. It's the the instrumentation library of some sort, because it it it proves that it can be done in in some agnostic way. But that that's my thoughts. I think you folks have the common goal, and you together can develop like a plan how you get to the the commonplace and semantic conventions. Again, if we want to spin a 1 off meeting, or a series of meetings on a 2 a and in in a generic manner, and feel free to invite me, I'd be happy to facilitate and help you as as far as I can. But I have very little skin in this game comparing to you folks.
shiprajain 00:21:42 Sure. Yeah.
Giovanna Carofiglio, Cisco 00:21:45 We can definitely have a meeting and at least high level share, and maybe compare and maybe produce a summary about where we align, where, where there are different opinions, and then come back to this Forum to to see how to move it farther.
Liudmila Molkova 00:22:16 And yeah, I think the 1st great step would be to just look into each other's documents and see where we are, the same where we're different.
Cool. So then, who who is going to organize it? Can I put a name on this? So it's not get lost.
Giovanna Carofiglio, Cisco 00:22:33 I I can do that. Is there a way to organize it? I mean, is just a separate meeting, or do you want us also to to put the details here in case someone wants to join or.
Liudmila Molkova 00:22:47 It it. However, you wanna handle it if you can post here in this channel and for example, we can have a if you want me, I can schedule a meeting on the auto calendar, or otherwise. There is a huddle here. People can huddle have a video call in slack.
Giovanna Carofiglio, Cisco 00:23:07 So it's the same if you want to schedule.
Sergey Sergeev 00:23:10 Yeah, I am starting a thread in this channel right now. I'll post a message and we can coordinate in the Swat Channel. Make sure that everybody who is interested join the Swat Channel.
I'll start the trend over there.
Liudmila Molkova 00:23:30 Wonderful. Thank you.
Okay, anything else.
Any immediate Questions concerns thoughts.
Okay. So I wanted to bring up the chat discussion we had.
That started by Aaron raising a great question of what we do with uploading content.
So I want to give a super quick overview for the folks who are not familiar or forgot. We are doing somewhat big refactoring on the current events and the way we capture chat history.
and one of the ways we One of the things we want to address is content, size, and sensitivity.
So we would record chat history in a different manner. And let's say we put it in the span attribute.
and it would contain, like, essentially the chat history. Right? So the system message. Or maybe maybe it's separate. Let's let's forget about it for a second user message assistant to a message to response and maybe multiple back and forth.
This is large.
It's large, anyway, it's large. Today. It could be large.
So, but it's also useful to have those things in one place and but we wanna have a pass forward for the backends that cannot or users who cannot store all the history on the telemetry.
and one of the ways to achieve it. We've been thinking that, okay.
this is a complex object.
we can store it as Jason somewhere else and just record the reference. So instead of all this landscape chat history, it's stored separately laters can access it. Some of the users can access it. But not necessarily. You can limit the audience to only those who can.
I don't know. You can limit the audience to audit reasons and and legal reasons.
Okay. So now the concern comes.
The moment we store the whole thing we lose some part of the information.
can I can. I make it full screen. Does anybody know.
Aaron Abbott 00:26:49 I think there's a way to do it. Maybe if you click on the date.
Liudmila Molkova 00:26:55 Oh.
I'm like, Oh, wow! Nice.
Okay.
So one way, would be uploading this whole content somewhere and just recording the reference the other way would be to just uploading the sensitive part, so doing something like this.
So you would still have the chat history.
But you won't have any content.
I added. The vote. I I think voting should be the primary mechanism. But anyway.
and it seems the foxy is winning this guy, and I wanted to talk about it.
I I personally, if I voted on each of them. But my personal preference is the cat and why?
Because I don't think that the the attribute like this is useful on the telemetry by any means as a user. I would look at this as a pure waste of my money.
but it seems there is.
The other people have different opinions. I think, Alex, you you are the most vocal one.
Can you share.
Alex Hall 00:28:24 So none of none of these are necessarily deal breakers in either direction. It's just that. It does seem that you can do a lot more things with the individual reps that you can't do with the big graph. It's it's it's more flexible.
It lets you include, like a truncated version of the content as you mix between different kinds of content. Like.
you know, maybe user content is sensitive and model content is not, or the whole thing about images versus text.
It lets you see the tool names.
It lets you upload each part separately and deduplicate them.
It lets you view the structure as it's still downloading the parts.
You can.
Liudmila Molkova 00:29:18 That allows you to do more.
Alex Hall 00:29:21 Sorry.
Liudmila Molkova 00:29:22 That allows you to do more, be more flexible.
But does it result in any improvements for the user experience.
Alex Hall 00:29:36 So, and all this.
If if the content is really big, it'll take longer to download the whole thing, and until it's downloaded the whole thing you can't see anything at all, whereas if it can download things, either as the use, you scroll them into view in the browser or just in parallel.
Then the user sees like a skeleton wallet that, like gradually gets filled in.
Liudmila Molkova 00:30:00 I'm pretty sure downloading 10 small files is way slower than downloading one file of 10 x size.
Oh, no, it doesn't matter in sequence or not. It's like the the availability problem. When you have, when you have 10 dependencies, your availability is worse than if you have one like if you download 10 files, and one of them takes longer than you slow down everything, and you have spending 10 times more resources, and your PP. 95, or p. 99 would be much worse if you don't, than if you download one.
Alex Hall 00:30:40 But also, even if you download them in sequence, if you're downloading them from top to bottom, you, you can start seeing the top before it finishes downloading all the way to the bottom.
Unless we can do the same as Jason right?
You want to maybe use Json lines for this.
Liudmila Molkova 00:30:57 Yeah, I mean, you can do the same as Jason. You can also use Jason lines. You don't need to deserialize Jason in order to render it.
Alex Hall 00:31:06 Does this mean that we have to base 64 encode all the content, whereas we could otherwise left the images as binary.
Liudmila Molkova 00:31:13 Oh, we we can. We can upload this Jason. However, like it's it's the upload. The goal is that the uploader decides how to upload it right and how to download it.
My concern is seeing this in your attribute is not helpful. First, st second, when you actually need to download this.
this will result in the it's just more difficult implementation of downloading and uploading as well.
Alex Hall 00:31:40 It's definitely more difficult for implementation.
Liudmila Molkova 00:31:50 So. My.
I don't know perfect answer to this question, but my main goal is to make progress, and I'm thinking about different ways to make progress. The 1st way would just not document either of this ways yet.
And then we can proceed with the rest of the spur request. We can do it as a phase, 2 like after we figure out all the other details.
The second thing we agree on one way, and maybe leave a room open for the other way.
I don't personally think we should have both ways documented, because.
it's just enormously difficult for anyone to implement anything on top of it when there are so many different ways to achieve this.
Alex Hall 00:32:46 I think that implementing both ways is only marginally more difficult than implementing the foxy way.
Liudmila Molkova 00:32:55 Oh, it's not about the difficulty of implementation, right? It's a difficulty of using. So if I'm implementing a back end, I will need to support. If I'm implementing a back end that that takes Otlp directly I need to implement.
Alex Hall 00:33:11 No, I mean.
Liudmila Molkova 00:33:11 All the ways and just the the combinatory explosion of different ways is is problematic.
Alex Hall 00:33:23 I think that if we were to go with the the foxy way, whether you're thinking about the back end or the instrumentations, it's not hard to also support the cat way.
Liudmila Molkova 00:33:38 I'm saying that for the consumers it's hard. Let's say you're writing a query. What do you write in this query?
You need to support everything possible in this query.
Alex Hall 00:33:48 I think if you want to write a query, I don't think there's anything you can do if you're if you're looking at the cat way.
unless your query can download from S. 3.
Liudmila Molkova 00:33:58 Either way. The query cannot do anything unless you download from S. 3.
Alex Hall 00:34:02 No, that's not true. You can query like number of messages, names of tools, possibly truncated versions of messages.
Liudmila Molkova 00:34:12 So that I think this is this little useful. Like very tiny useful, we can record it as metrics. We can record it as something else.
Aaron Abbott 00:34:25 Yeah, I have to say I'm also really on the fence about this. Still, I feel like I could see the benefits both ways. I I am. I've shared the same concern with no about like the explosion of different possibilities between spends logs, and then 2 different styles for recording the content.
I do think so. So. Assuming that this structure, like the this, is the normative part, right.
the part in the in the log or the span attribute.
Assuming that ends up in some kind of database instead of cold storage.
it is marginally more useful for queries. I feel like to have some kind of information here.
but I I see all the flip sides. You said, too, like downloading a bunch of refs is typically harder than just one we're creating like, creating a bigger data problem, maybe, or or increase complexity. So I I also like keeping the instrumentation more simple, like single single upload but I did hear this concern from back end folks at Google about the limited amount of information in the current proposal, where you just have 3 blobs, or whatever. Yeah.
Liudmila Molkova 00:35:42 So then let's let's do this. I'll I'll take this part away from the current. Pr.
I would probably still keep the information about uploading hook and then we can come back to this and talk more. We can also think about it in the background.
Yeah, Ryan, go ahead.
Aaron Abbott 00:36:13 Yeah, I wonder? So I think we've got votes. I I kind of abstain from voting since I brought this up. I'm still a bit on the fence.
I don't think. Did we get a vote from anybody from Cisco? I'm wondering if we could put them on on the hot seat right now.
if not, that's okay, too. But yeah.
okay, yeah. I think we know what you said is fine, like, we could punt the the rough thing a little bit, and maybe we can prototype more. But it shouldn't block your.
Liudmila Molkova 00:36:54 Cool any other thought on this.
Okay, so let me, oh, yeah.
okay, cool. So we are exactly at our time box to discuss the project, planning that we started less dime.
So we've had some discussions on what's interesting. What's less interesting for folks.
I remember leaving some names on some data. Where was it be here?
No, not here.
Did I dream we talked about assigning work items to people.
Okay, maybe I drowned.
Aaron Abbott 00:38:31 No, no, we didn't.
Liudmila Molkova 00:38:35 But it disappeared.
Oh, here we go. Yeah. Oh, okay. So this is the parts we talked about.
Okay, so what did we cover? Some of the biggest achievements we've done. What are we planning to do in the next 12 months?
And we talked about the the Pr we just discussed.
we talked about the common package in Python. The.
Sergey Sergeev 00:39:05 Poc in progress. So agency project from Cisco they built the whole observability. Observe, SDK, so we are trying to figure out how to merge it. To implement the designs and ideas.
I still need to document to extract internal documents into public documents about the design proposal.
So work in progress. Stay tuned
Liudmila Molkova 00:39:36 Therefore.
Sergey Sergeev 00:39:44 Aaron. Once I have something publishable and reviewable, I'll ping you. But hopefully it will be a Poc demonstrating the SDK in instrumentation, SDK, evaluation, SDK, and how instrumentation or integration can use it.
Aaron Abbott 00:40:05 Okay, yeah. And I'm happy to. If you want to talk, talk it through before it's completely finalized, you know. Just.
Sergey Sergeev 00:40:11 No, no, no, it's just a Poc and nothing finalist.
Aaron Abbott 00:40:15 Okay. Cool.
Liudmila Molkova 00:40:21 Oh.
yeah. So we talked about general concern. Aaron, did you have a chance to sync with python folks? Do you know if anybody is planning to work on this. No, not related to Jenny just in general.
Aaron Abbott 00:40:37 Yeah, yeah. So I brought this up. People didn't, really. They wanted some time to think about the kind of I basically took this template. They they weren't really ready to answer it in last week. Sig. I think this week is a holiday, at least for for me, so I won't be there. But yeah, I guess not yet. Sorry.
Liudmila Molkova 00:40:58 Yeah, no worries, But essentially what? What's what might take on this? Nobody is actually interested. And we, if we are interested in the seek. We probably should help you folks.
Aaron Abbott 00:41:16 Yeah, I mean, I'm I'm interested.
Liudmila Molkova 00:41:19 Yeah.
Aaron Abbott 00:41:20 I will say that.
Liudmila Molkova 00:41:32 I'm interested, too.
Okay, so the other thing we discussed is evaluations.
I know that somebody from Microsoft is looking into this but they cannot talk about their commitments.
Sorry I'm lost.
okay. And now let's get to the fun part the one that we don didn't talk about.
this part.
So for the multi agents, it seems we have a separate work stream for it now.
I wanted to chat with folks here and think, Tyke.
do we think it's the same sick?
Would we splitting our efforts too much?
Do folks have any thoughts on how we should handle all the new things like multi agent, plus the other stuff.
Sergey Sergeev 00:43:21 For me personally, it's way easier to understand the problem when we have something to play with, something like a demo application which shows.
oh, for example, we we chose a multi-agent specifically, I think it would be great not only to have telemetry, but also to have a sample application of instrument before just an idea. So if we also have on file sample application for proposed instrumentation and proposal for instrumentation, and we can make progress probably faster.
I I don't know. Probably it was the same way before.
Just wondering if it's a typical pull. Request for semantic conventions includes a sample application and telemetry all the time.
Liudmila Molkova 00:44:29 It. It doesn't. But it's definitely something that would.
It feels necessary in case of multi agents, because otherwise it's too abstract.
It's like it. We we are the signature site when the pull request is ready. Right?
And so one thing I wanted to to discuss in terms of the project planning is okay, let's assume multi agents being somewhat there is a focused group within the Sig that works on it.
We have a bunch of other stuff to work on as well.
Right? I didn't even bring everything up.
So we we have all of those work streams. And I'm thinking if something new happens which does in the world where I don't think how we we will be able to make progress on the new thing.
And I want us to kinda agree to a set of projects we are working on going forward so that we don't over extend ourselves.
which I feel is already happening.
So maybe we can do some exercise of deliberately throwing things away. That or on our plate. We can do it. Now. We can also have game. Let's say we will.
Well, but maybe let's do it now.
and we will continue offline, because not everybody is here.
So we will. We have this all these stuff things that I think we are working on or are talking about.
and we can put it in excel. And I would give you, let's say, a budget of 10, and you can each distribute your 10 points among this items. However, you want to.
You can put 10 for one of them. You can put one to each, but you have a budget of 10, whatever you want to do.
and we'll collect some votes, and then we will just take top. I don't know 3, 5 things.
I'm slightly worried about this because Cisco and Microsoft are working on multi agent story, and you would work on it. Anyway. I cannot stop you from doing this. I I want you to make progress in often telemetry.
Sergey Sergeev 00:47:21 Should we? Should we just create a slack channels for each of the initiative and basically group people offline in those groups and to add those groups to set up something like ad hoc calls to make progress.
Liudmila Molkova 00:47:40 I think.
Oh, each of this groups should come back to semantic conventions right? We should know about each other. We should have something in common.
Sergey Sergeev 00:47:51 Yeah, this Doc may be kind of central.
Buy it in where everybody reports back.
I don't know.
Liudmila Molkova 00:48:04 It's still there is a handful of people who actually work on anything in in this, for in this, in the genie space, and if if we also have 5 different slack channels where they talk to each other, I think we will not make progress.
A.
But I I kind of want to get a sense on how much interest there is in each of those topics.
And I want to come out with the agreement that this is the list of things we are working on. And in order to start working on something new, we need to drop something else.
So, Jay, I see you enabled Video, do you want to share something.
Sujay Solomon 00:48:47 Yeah, I mean the you know, we were chatting. And I think that the point here is we.
We have limited number of folks building things, and we are spread too thin. And if we try to focus on far too many topics, we're just not gonna actually get to the finish line with any of them.
So I think.
you know, doing this exercise here, which gives us an idea of like where people's priorities are from, you know their perspective. Their company's perspective, maybe, will allow us to choose, like 3 or 4, 2 to 3 topics that we can focus on for some time period and really get that across the finish line, like, I think it would probably be important for us to still keep some buffer time for other urgent things as they pop up, but that would be from the perspective of like. We can do some reviews and such. But if you want a new topic to be worked on in the Sig.
like you probably need to bring staffing to help you know. Run that, and then we can possibly help with with the reviews. But I think as a Sig, we need to figure out like, which are the top topics for us to really focus on and get across the finish line because Sigs can only achieve things if you are delivering, you know, concrete things right? So we need to. Probably, you know, work towards actually getting things into at least experimental state, so the rest of the world can use it and give feedback and move things on.
So I'm I'm all for narrowing down that list to a few topics that we really focus on, and maybe define some milestones for them.
and say, Hey, once we get to this point and deliver this. We can now, then, look at expanding our scope to include other things.
just a proposal to to make us effective and actually start delivering things.
Liudmila Molkova 00:50:50 Thank you. As as you can guess, I'm all in on this proposal.
Okay?
So I feel we don't have time for the budget exercise right now.
Let's do it offline. I will have something prepared by the next time.
And let's see where it brings us.
I'm looking at the I'm I'm actually I think you're you're bringing a good point that the buffer things. So I would dimension that if somebody comes and sends a Pr to define tool definitions. It's a small enough work that we we would be happy to review.
Regardless of whether we have a work strip dedicated for it. So big feature works are for giant areas like multi-agent for evaluations.
Quite sounds good.
does anyone before we call it a day does. Let's again quickly go through this list and make sure I capture every work stream we are already working on.
Does anybody wants to bring something.
Okay?
So do we do, refactoring their active pull requests evaluations.
I think everybody is interested. Nobody is sending Prs.
Sergey Sergeev 00:53:07 Yeah. I I think key difference from some open source. Libers are that they are not connected to spans and traces. Maybe I'm wrong, but I think it should be defined in context of the span. Otherwise most of the open source libraries, like openlid, deeperval, and etc. Provide some basic evaluation scores, I would say, structure.
We need to turn it into metrics.
Liudmila Molkova 00:53:47 Okay, I'm just just wanna go through the list without going into the details. For for the for the moment.
we have people interested in new instrumentation libraries think we never proceed on this. But my main thought that if we want to make progress we'll just take link chain and go as link chain. And I think, Sergey, you folks been looking into the link chain right.
Sergey Sergeev 00:54:25 Yeah, and I think there is a pull request already in review with the basic so the team he's trying to break down it to smaller pieces because the pull request is big.
Liudmila Molkova 00:54:40 Oh, there is one for Python Contrip.
Sergey Sergeev 00:54:42 I think so.
Liudmila Molkova 00:54:44 Oh, yay!
Pablo Collins 00:54:45 Yeah, it's just a. It's just a skeleton right now.
Sergey Sergeev 00:54:47 Yeah.
Liudmila Molkova 00:54:53 Bring it on.
Oh, sorry!
Sergey Sergeev 00:55:00 I'm working on that Poc to use instrumentation. SDK, on land chain example to show how instrumentation can be simplified in parallel. So hopefully, we can use it.
Liudmila Molkova 00:55:26 I will take a look. This is wonderful.
Okay.
So here I hope we can do the same exercise for it. We don't need to bring everything we will bring. What we care most about are.
So I'm going to maybe move this to the Misc because it's a tiny feature. If we get the 1st Pr in so like adding the image part would be a trivial change that doesn't need to separate work, stream or much work for the frameworks.
It sounds like we are.
We actually needed to make progress on other things. So the agents or multi-agents depend on the frameworks. It's the same topic.
Sergey Sergeev 00:56:59 Yeah, I'm wondering what it is specifically, how is it different from trace hoop existing instrumentation?
Is it just to build a new instrumentation for some frameworks like Openai Agent SDK, or.
Liudmila Molkova 00:57:18 I I don't think we can make good progress on link chain until we know how to do certain things for the frameworks, right how to record the framework spent like we know how to record. Lm, span. But do you have an add a higher layer that also calls it to tools and tool calling is also part of it.
Sergey Sergeev 00:57:40 Yeah, so framework span types basically got it.
Liudmila Molkova 00:57:47 Right. But we can also limit this feature. We don't need to boil, though, should we can limit this feature to what we need, based on the instrumentations we are working on.
Okay?
And that's maybe the multi agents.
Again, I I feel we already have people working on them and super interested in this specific effort.
So I don't, though.
I would imagine that you folks will just put your budget up on on this work.
Yeah, okay? And there, there is Mcp. We already have conventions. I don't have approvals, so I can. Happy. I can happily show. Put this work on shelf until there are people who are interested in putting into it into semantic conventions.
And the server side by think there is interest, but there is nobody working on it, so I would just imagine it won't get any budget.
We are at time.
If we put an end goal of having 2 or 3 active working projects, we will be in the hard spot. So we I think we we should discuss it further. How we can tackle it cool, so I'll I'll do the excel. I'll share the details in the chat. Let's play the exercise we'll hopefully have some results. And others PE other people joining the call next time.
We'll continue doing this. Thank you. And happy 1st of July week for folks who take vacation.
See you on the next week.
Aaron Abbott 01:00:04 Thank you all. Later.
