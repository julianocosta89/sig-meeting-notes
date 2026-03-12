SIG: Developer Experience SIG Meeting
Date: 2026-02-18
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 01:06 Hey, you're kind of…
**Juliano Costa | Datadog** 01:07 No.
**Johanna Öjeling** 01:09 Yeah, me too.
**Juliano Costa | Datadog** 01:10 Opt out… This is annoying.
**Johanna Öjeling** 01:14 Yeah, so how do we actually count?
**Juliano Costa | Datadog** 01:20 So, you, you just…
**Johanna Öjeling** 01:21 Oh, sweet.
**Juliano Costa | Datadog** 01:21 Opt out in it, yeah. But, like, we should find… Hi, Nico. We should find Bogdan Nikolai and ask him to remove Rid AI from the meeting.
Because… Read AI is just a tool.
He configured it to join the meeting, so, yeah.
**Johanna Öjeling** 01:44 Yeah, I wonder what the feedback has been, if, like, everybody else is annoyed.
**Juliano Costa | Datadog** 01:50 Yep.
**Johanna Öjeling** 01:53 Hi, Nicola.
**Juliano Costa | Datadog** 01:53 Nope.
**Nicolas Wörner** 01:54 Hey guys, nice to meet you.
**Juliano Costa | Datadog** 01:57 in Overflow.
Nico, you guys use Read AI at, Olegarden, no?
**Nicolas Wörner** 02:08 Yes, we use REA, I believe.
**Juliano Costa | Datadog** 02:13 Is there… A new way to opt out forever as a, like.
**Nicolas Wörner** 02:22 That's a good.
**Juliano Costa | Datadog** 02:22 And main… so, like, can someone actually kick?
Read AI.
from the meeting?
That's a good question. Like, not geek, but, like, how to frame that? I don't know.
ideas.
**Nicolas Wörner** 02:37 Thank you.
**Juliano Costa | Datadog** 02:37 Cool, yeah, yeah, go ahead.
**Nicolas Wörner** 02:38 When I join a meeting, I always see, like, a pop-up if I want to invite Read AI to the meeting, and then I can accept or decline.
But I am not sure, to be honest, because Chirassi set it up at Oldie Garden, so he took care of all the configuration. For me, I just see the pop-up, and that's it. I either accept or decline, and that's all I need to do.
**Juliano Costa | Datadog** 02:59 Yeah, the calls that I have with Yuri, Rida always joins.
But as… as on those calls, I'm the owner, I simply remove it.
but I wonder if there is a way to, kind of, block… From even joining.
Anyways, yeah, I just, thinking out loud here.
How are we on the MCP stuff? Any, any news? So, like.
**Nicolas Wörner** 03:32 That's a great question.
So, I was writing with Pavel a few days ago, and what's happening right now in the proposal is that the initial proposal was approved by the government's committee.
But there was not somebody from the technical committee who sponsored, the project or the proposal, and that means it was not merged or not approved in total. And now the suggestion was to re-scope it, which means that we only focus it on the collector side of things.
And, the open question right now is how or what that means for the project. If it will now be moved to the collector's sake, or if it will not be moved and will continue here, that's what I don't know. So, I sent Paol a message, but it seems like he cannot make it today.
But he was in contact with… somebody from the collector, and talked with somebody from the… with a maintainer from the collector, but there we need to find out what that noun means for the project. But yeah, it's a bit unfortunate, I think.
**Juliano Costa | Datadog** 04:38 Yeah, I saw the message for… from Ludmila on that.
And I was like, huh, okay, yeah, that's interesting.
**Nicolas Wörner** 04:48 Yeah, because, no, we basically start again from scratch, but okay.
**Juliano Costa | Datadog** 04:52 Yeah.
That's… Yeah. I also saw that… I don't know if you are in sync with Pavel outside this meeting, but I saw that the new Jaeger comes with MCP integration as well, or server, or whatever, like, I… I haven't looked into it, I just saw on the changelog.
Because… I just actually saw from the PR from Renovate, and I have the changelog, so I just opened the drop-down and saw, okay, yeah, MCP, whatever, and oh, yeah, cool.
Something to future, Julian, take a look.
**Nicolas Wörner** 05:37 Yeah, I need to check it out, it sounds interesting.
But, no.
**Juliano Costa | Datadog** 05:41 I wouldn't care anything.
**Nicolas Wörner** 05:42 from Pavel about this.
**Juliano Costa | Datadog** 05:45 Okay, cool. Yeah, because I also know that Jaeger is running a collector within it.
**Nicolas Wörner** 05:53 So…
**Juliano Costa | Datadog** 05:54 maybe there are… I don't know what it… what are the capabilities of the MCP, of what the MCP was configured for?
In the project, but, maybe it's something that we can… Use the header.
**Nicolas Wörner** 06:08 LinkedIn, by any chance, because I just searched for it, and I only find a project which is already a bit old, like, 10 months.
**Juliano Costa | Datadog** 06:16 Give me a second.
**Nicolas Wörner** 06:17 it's installed.
**Juliano Costa | Datadog** 06:19 That would be very interesting.
**Nicolas Wörner** 06:20 alternate.
Here I see something on X.
I found it, I found it.
So apparently they are using the MCP server to, for example, retrieve spans from Jaeger.
Or two… to basically manage Jaeger instead of the UI, you would maybe hook it up with a coding agent, and then ask the coding agent to give you relevant spans about a certain Query you might have.
**Juliano Costa | Datadog** 07:04 Oh, okay.
**Nicolas Wörner** 07:05 I think.
**Juliano Costa | Datadog** 07:06 So it's not about, configuration, but rather…
**Nicolas Wörner** 07:10 That's how I understand it, based on the few lines of the changelog, so maybe there is more in that, and I'm not seeing it right now, but here in the changelog, they are, for example, mentioning they are adding a tool to get span names to discover span names in Jaeger. So I assume it's more like operating or retrieving something from Jaeger.
Instead of actually configuring it, but… Might not be everything.
**Juliano Costa | Datadog** 07:35 Oh.
Oko.
**Nicolas Wörner** 07:37 I can send a link here in the chat.
**Juliano Costa | Datadog** 07:43 Thank you. Clearly, I saw it, but I don't remember where. I have a couple of repos that I have renovated on it, and… I'm, like, drowning in notifications.
**Nicolas Wörner** 07:57 I need to.
**Juliano Costa | Datadog** 07:58 To figure out how to survive this.
That's a thankful for this.
**Nicolas Wörner** 08:08 You can search for MCP, you will see a few tags and a few items, which is about… I think the MCP is already…
**Juliano Costa | Datadog** 08:17 Nice. Nice.
I'll add that to the… BT notes.
I've been using… Mac, or 2 years now.
And if there is one thing that I would love to change is, can I get back CTRL-C and CTRL-V?
**Nicolas Wörner** 09:23 I can understand this.
I now changed my muscle memory after many years of using it, so now I'm kind of used to it, but whenever I'm using a Linux PC or a Windows PC, because some of my friends have different PCs, it's terrible for me. It's really terrible.
**Johanna Öjeling** 09:43 Yeah, it's, amazing how fast you get used to… I also, I switched over to Mac.
maybe, like, 8 years ago or so? And now I can't, like, I feel completely, like, disabled when using a PC.
**Nicolas Wörner** 10:01 And what I'm doing these days, quite a lot, so I'm not typing anymore, I'm speaking now, I started to use the Whisper AI, you maybe have heard of it.
And then I just press a button, and I speak. It's a little bit crazy in the beginning, but after some time, I got used to it. And now, especially when I work with AI, it's so easy to create a prompt, because you speak for, like, 5 seconds, and you're able to produce much, much more words, and sometimes even more precisely, because it's easier to speak instead of write everything out.
And I find that very useful, at least for that kind of work. For creating, like… blog post or technical documentation, I don't find it too useful, because sometimes it gets the words wrong, and then you need to go back and correct them. But when you write a prompt, I will usually understand even if something is not correct, and that's really, really a time saver for me.
**Juliano Costa | Datadog** 10:55 Cool.
Yeah, I had a chat with Jurassi during Fosden about how you guys are using AI internally, and yeah.
I was surprised how lean you guys are.
That's…
**Nicolas Wörner** 11:09 Yeah, yeah, we use AI a lot. We think that it can help a lot, or facilitate a lot, but of course, it needs to be taken with care, because if you rely on it too much, it's also getting a bit complicated.
So I tried, I'm not… okay, I'm not sure if this is too off-topic, but as we are just three persons right now, I tried the Ralph Wiggum technique. I'm not sure if you have heard about the Ralph Wiggum technique, but essentially what you're doing there is… you're putting the AI agent in an endless loop, and you, always give it one task, you let it complete the task, and then you start a new session.
And the advantage, or the promised advantage of that, is that you call the AI agent every time with a new context window, which means that Probably the results would be better, because it only knows the specific task it's supposed to work on, and the way the technique works is you basically plan, like, 20 user stories in advance, very detailed, with very detailed verification instructions, and then you start the for loop, and it sometimes runs the whole night, and you see how it goes.
And, according to some people on social media or other platforms, the results are very, very good.
So I gave it a try to develop something internally at Ollie Garden, but I have to say, either I used it the wrong way, or it is simply not there yet, because it produced some stuff, which was also kind of working.
But as soon as you run into an edge case, or into more complex behavior, it just falls down, or falls short.
Yeah.
So, we are not there yet.
**Juliano Costa | Datadog** 12:53 what I like to think about it is that this is the worst that's gonna be. We're gonna only improve from here, so, yeah.
**Nicolas Wörner** 13:03 That's awesome.
I kill myself, always.
**Juliano Costa | Datadog** 13:05 Yeah.
Now… coming back to the… to the SIG itself, Johanna, have you heard back from anyone on anything?
**Johanna Öjeling** 13:16 on the blog.
Yes, so new I'm still waiting for, but Bogdan has, approved the Adobe blog post.
And I asked him if there were any snippets or images that he could share, but he didn't send me anything. And then, yeah, he went into the document and, like, changed his status to approved, so I… yeah, it seemed also, like, during the interview that He couldn't, like, disclose any… Details, really, so… I'm, hesitant.
To… yeah, I think he may not be able to send us any images or config snippets.
But, he was happy with the blog post, so, yeah, please. That's good.
**Juliano Costa | Datadog** 14:12 Okay.
**Johanna Öjeling** 14:13 image, which, yeah, after we spoke last week, I updated the Excalibur diagram, so at least we will have that.
**Juliano Costa | Datadog** 14:25 Cool, and talking about that, I had… I want to ask something to… to you?
**Johanna Öjeling** 14:34 One sec…
**Juliano Costa | Datadog** 14:35 I think it's on the… Yeah, so I, I took, I took your approach as example, And… Because I had this one before, and then we… You used this other one here on the top.
**Johanna Öjeling** 14:59 Mmm,
**Juliano Costa | Datadog** 15:00 And I was like, okay, let me give it a try. And I think it's nicer because we explain what type of collector it is. I think it makes Makes more clear that this is a sidecar collector, and not, like.
like, here you may need… I think you need to understand the image to actually understand what it… what is representing. Here we state.
**Johanna Öjeling** 15:24 -
**Juliano Costa | Datadog** 15:24 So I think this one is, more clear.
**Johanna Öjeling** 15:28 Yeah, yeah, I agree, yeah.
**Juliano Costa | Datadog** 15:32 Okay, so… so just, change to… to all of them. Now I have a question for you.
This logo is there on the hotel, repo, But… I rarely see it being used. Should we just, as we are using the hotel logo anyway, should we just go for the… for the telescope itself, from the hotel IO.
What do you think?
**Johanna Öjeling** 16:00 You mean the, like, colored…
**Juliano Costa | Datadog** 16:06 Well, we can use the white one, or the black one. I think we have that on the… We'll tell logos…
**Johanna Öjeling** 16:17 Okay.
**Juliano Costa | Datadog** 16:18 Icon… black.
We have PNG and SVG, but yeah, that's the image.
**Johanna Öjeling** 16:27 Okay.
**Juliano Costa | Datadog** 16:29 Oh, a potion.
**Johanna Öjeling** 16:29 Ta-da!
I mean… Yeah, I think because I… why I used the… the icon, I thought I was… because the other one, yeah, became, like, too… like, when minimizing it, you couldn't really see that well, and then I.
**Juliano Costa | Datadog** 16:50 Something else.
**Johanna Öjeling** 16:50 okay, like, people are more familiar with the telescope than with the, yeah, icon for the auto collector. So I think, yeah, what you're suggesting might be even better, that, yeah, it will become Even clearer, yeah, that it represents kind of flow collector.
**Juliano Costa | Datadog** 17:09 Oh, okay. Yeah, so let's go… so I'll just add here…
**Johanna Öjeling** 17:22 Yeah, then we can update those posts, and I also have on my to-dos to review the, Danskate blog post, fix this.
**Juliano Costa | Datadog** 17:34 I haven't… I haven't reviewed yet, because I was doing the images, but I need to do that, and also review the Adobe, because that's the only one that we have approved.
**Johanna Öjeling** 17:46 Yeah, -
**Juliano Costa | Datadog** 17:48 So, maybe we can start with it.
**Johanna Öjeling** 17:51 - Yo.
**Juliano Costa | Datadog** 17:53 Yeah, I, like, Tim told me that he would come back to me and approve by last week, and he didn't, because I would love to start with his story, because it's the smallest one,
**Johanna Öjeling** 18:07 Yeah, -
**Juliano Costa | Datadog** 18:09 So… But anyways, if we get Adobe first, then we go for Adobe. I think we just need to rephrase the beginning of it.
just to… Give the readers a context on why we are.
**Johanna Öjeling** 18:23 Yeah, - -
**Juliano Costa | Datadog** 18:26 And then… because, yeah, that's what I think I have on the first paragraph of the Mastodon one.
**Johanna Öjeling** 18:33 Yeah, yeah, I think that's good to start with, yeah, whichever blog post comes first.
**Juliano Costa | Datadog** 18:39 Yeah, yeah.
**Johanna Öjeling** 18:39 Yeah, to give some context. Yeah.
Awesome. But we can also, I mean, if you want to ping Tim and ask, yeah, then if he approves, then we can start with that one. But yeah, if it still drags up on time, yeah, we can go with the Adobe.
**Juliano Costa | Datadog** 18:59 I'll do it right away. blog post.
Hello, team.
So, like, I… I don't mind.
like, nudging or bumping you once or twice. Like, when it's, like, five times already, I feel.
**Johanna Öjeling** 19:18 Oh, okay. I didn't know it was already 5 times.
**Juliano Costa | Datadog** 19:25 Yeah, maybe he's busy, yeah.
**Johanna Öjeling** 19:28 Yeah, okay, no, but then, I will update the image for Adobe, and then, yeah, once you have reviewed, then I can also ping Tristan and ask him to review, then, yeah, if it's all fine, we can move it over to the open telemetry I.O. VPN, yeah, that one.
**Juliano Costa | Datadog** 19:45 Awesome. Okay. Cool.
Cool, cool. Great! Then… Yeah, I think we can wrap up for today.
Yeah, and let's see how MCP, unfolds.
**Nicolas Wörner** 20:07 I'll keep you posted when I hear anything.
**Juliano Costa | Datadog** 20:10 Thank you.
**Johanna Öjeling** 20:11 too.
**Juliano Costa | Datadog** 20:11 Cool. Ben, see you all next week.
**Nicolas Wörner** 20:13 Have a good day. Bye.
**Johanna Öjeling** 20:14 Good day. Bye.
