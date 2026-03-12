SIG: Python SIG
Date: 2025-11-13
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/GCHgJZNI3S_NOv5pu5RvYUWWOD8-eEoNkMRZa_PDKXkh5W0hNBqoq4j05GQg8tWu.1wxmowh9rueSq_l4
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:47 Hello, everyone.
**Hector Hernandez** 00:50 Hello?
**Riccardo Magliocchetti** 01:57 Welcome to this week's Python Seagal wiki call. In the meantime, but you're waiting a few more minutes for more people to join.
Present yourself as an attendee to the document I shared in the Zoom chat.
And also, if you have any topic you want to discuss, feel free to add them.
To the notes as well, thank you.
**Aaron Abbott** 02:54 Hey everyone, how's it going?
**Hector Hernandez** 02:58 Hello.
**lechen** 04:00 Hello.
**Riccardo Magliocchetti** 04:30 Okay, 9 people, I think we can start.
Welcome again to this week, this week, python, call.
And… yeah, please add yourself to the list of attendees in the… Sign notes, and also, if you have any topic, feel free to add them.
At the moment, we only have 3 topics.
So let's start.
Okay, just, an update on the lock stabilization work. We merged the first PR, At last, thanks again, Actor, for… Doing the work.
**Hector Hernandez** 05:16 Thanks, Rakar, for reviewing. It's also plenty of work.
**Riccardo Magliocchetti** 05:23 And… yeah.
So, yeah, first milestone, still, a couple more PR. Well, at least one, again, from Ekto.
To merge before the next release.
And speaking on… like stabilization, I had another topic.
But, what? Oh.
But, we had these issues… issue 5.
Some time ago. That is, but, it's strange.
From one that has a clue about omit telemetry.
that, when we are shipping logs, from Python application, we are duplicating, The context, some context attributes here in the, some context.
Stuff.
Here in the attributes.
And… and also some resource attributes.
And so… yeah, like… When they filled the issue, I thought it was just, like, the logging instrumentation doing some strange things, but I think the… The problem is a bit more, complicated, because, like, looking at the code, what the logging instrumentation is doing.
is just, adding some, some attributes to the Python log record, and so, like.
So that when using the instrumentation log, the logging instrumentation, you also, are adding to your logs also the context in which the log was created.
Which… makes sense.
The problem is that when you enable the log shipping part, but at the moment is in the SDK, Like, you see, A log, instance, but… SB's, with things that are coming from the Python log record.
And so my question is… Do you have any idea on how to handle that? Like, should we probably filter these attributes? These are, like, poor and well-known?
In our longing handler, or… It's fine as it is, or… I don't know.
**Aaron Abbott** 08:12 Yeah, I feel like… I feel like there's not a lot of value in this OpenTelemetry instrumentation logging anymore.
I feel like the easiest thing would be to just get rid of it, or at least for this user, to get rid of it. Was there a reason they can't do that?
**Riccardo Magliocchetti** 08:33 I think the issue comes from the… Like, from the OpenTemplary examples.
Because, like, this is how we behave out of the box.
**Aaron Abbott** 08:46 Only if you use, like, the bootstrap command, right?
**Riccardo Magliocchetti** 08:52 Yep.
**Aaron Abbott** 08:56 Yeah, I mean, that's my… my personal thing is I feel like it's now kind of… duplicative of the logging SDK to have this instrumentation logging thing. I know it serves a slightly different purpose, but… Maybe we could remove it from the bootstrap script? What do you think?
**Riccardo Magliocchetti** 09:21 But I think if the plan is to move the handler Inside the instrumentation, we can't do that.
Or, like, do you want to create, like, another instrumentation for the…
**Aaron Abbott** 09:34 Yeah.
**Riccardo Magliocchetti** 09:35 For the logging handle?
**Aaron Abbott** 09:37 Yeah, you're talking about the other issue?
**Riccardo Magliocchetti** 09:39 Yeah.
**Aaron Abbott** 09:40 the one I put, yeah.
I mean, I feel like… Calling it, OpenTelemetry Instrumentation Logging has been… very confusing for a lot of people, so I would be okay to call it something different, like… OpenTelemetry… Python handler or something like that, I don't know.
I know, I know I originally probably said in here we could put it into the OpenTelemetry instrumentation log, but… I just… I feel like this is, like, very confusing to people.
They don't know what to do, and the names don't really… Give the meaning that there's… of what they actually do.
**Riccardo Magliocchetti** 10:29 Yeah.
Like, I don't have any strong opinion on this.
Wow.
Yeah, like, probably we can.
Take a few more time to think about this thing, because, like.
I think that… as, like, a list for me.
I spent much time thinking about the SDK part more than this.
But when the logging gambler, I thought, yeah, so…
**Aaron Abbott** 11:00 Yeah, yeah, agreed.
I mean, I don't think we have to, like, get rid of it necessarily, but, yeah, it doesn't… especially if someone's doing auto-instrumentation, it doesn't make a lot of sense to have it included out of the box for just setting up the logging SDK, I think.
**Riccardo Magliocchetti** 11:20 Yeah, I agree.
So… Like, maybe, like… Just, we can think a bit more about this, and we can just update the issues if we have any ideas.
Oh, we can discuss it in the next weeks.
**Aaron Abbott** 11:56 Okay, sounds good.
**Riccardo Magliocchetti** 11:57 Okay.
**Aaron Abbott** 12:00 Yeah, this other issue about the logging handler with moving it out of the SDK?
I feel like we've talked about it a few times, but, if we're… Getting close to log stabilization, we should probably make a decision.
Mmm.
I don't know, are there any objections to this? Like, I agree, it is kind of convenient to have it in the SDK, but I don't feel super confident about marking this part stable, because You know, there's bugs with the infinite recursion, there's some issues with… the mapping not necessarily being, like, standardized, so it puts the extras, I think, in attributes, which maybe is the right thing, and then body… That's the message, I think, so… I don't know, I feel like we could avoid the problems for the stabilization effort if we put this somewhere else, but… It is… I agree, it's, like, convenient to have it in the SDK, so… Any objections?
**Riccardo Magliocchetti** 13:11 No, like, for me, it's fine.
Like… If we install… Like, if the package where this will be moved, will be installed by Bootstrapped out of the box?
So, like, for users of Bootstrap, it doesn't change anything, like…
**Aaron Abbott** 13:33 Yep.
I guess an alternative would be to just call it… put it in, like, an underscore package, and say it's unstable or something like that, but… Bill.
Okay, I guess we can move on.
**Riccardo Magliocchetti** 14:00 Okay, I was writing notes. Okay, next topic, still for me.
Like, we have VPR, around, since a few.
But he's handling the case where, Django logging, contains some stuff, but is not, of any value.
And so it's… Well, maybe… And so… We are getting, like, logs of the… Exception we raise when we are not able to, Clean up the attributes we add to the log record.
And so, like, I think the initial implementation was, doing some special casing of this.
in the SDK code.
But, when I… on the… or in the API code, not remember.
But, when I reviewed this, I suggested Since it was, like, importing Django stuff, suggested that probably it was an issue of the instrumentation.
And not by the general code, but looking, at the stack trace again, probably, like, A senior approach, like, at least a proposal.
Could be, like, to, try to stringify whatever is not, a type.
We handle, in that code.
And so, like, we don't add any dependency on external libraries.
But also, like, we made the thing a bit more robust.
Because the current implementation, I think it's… Doing a filter.
And just, like, during the stringify of the… Of the attribute inside the… the log record.
**Aaron Abbott** 16:16 Any idea what other languages do?
**Riccardo Magliocchetti** 16:22 Yeah, I have no idea.
**Aaron Abbott** 16:24 Huh.
Yeah, I mean, I think this is pretty insane.
I guess the only question is, like, string versus wrapper, like, REPR built in.
But I think… I think this is pretty sane because, if, if you, I think if you do this with, like, the logging… handler in Python, it will just call a string on the arguments, right?
**Riccardo Magliocchetti** 16:56 Well, it's not doing that.
**Aaron Abbott** 16:59 So, sorry, I mean…
**Riccardo Magliocchetti** 16:59 the issue.
**Aaron Abbott** 17:01 Sorry, I meant, like, basic config, like, with the default OTel, sorry, default non-OTEL.
**Riccardo Magliocchetti** 17:07 hook.
**Aaron Abbott** 17:08 Yeah.
**Riccardo Magliocchetti** 17:09 Yeah, I think it's doing that, yeah.
**Aaron Abbott** 17:12 Yeah.
Yeah, this makes sense to me, but, Do we… do we do this recursively?
**Riccardo Magliocchetti** 17:22 Yeah, like, the function that tries to clean up the attributes is recursive, so…
**Aaron Abbott** 17:31 Yeah.
I don't have any problem with this, and I think it's kind of nice, because people can wrap things also in a class that implements double underscore string.
For, like, purposes of.
**Riccardo Magliocchetti** 17:45 You know, lazily encoding it, so if the log gets dropped, they don't need to convert it to a string beforehand.
Okay, so, to clarify, like, you are okay in adding something like that inside the common code, right, in the API?
Or do you want to keep this code inside the other instrumentation that may have the same issue?
**Aaron Abbott** 18:13 Yeah, I think I'm okay to put it in the API.
**Riccardo Magliocchetti** 18:16 Okay.
**Aaron Abbott** 18:17 Yeah.
I would like to check what other languages do, though, because I feel like it's a pretty general problem.
**guptaradhika** 18:41 So, yeah, just to clarify, so you're saying to move this code to the logging API instead of putting in the Django instrumentation, right?
So that it works for, like, other families, requests as well.
**Aaron Abbott** 19:00 Not sure who that was, but it was very quiet, it was kind of hard to hear.
**guptaradhika** 19:04 Boom.
Can you hear me now?
**Aaron Abbott** 19:13 I can hear you, but it's just very quiet.
**guptaradhika** 19:15 Probably. Go ahead.
Yeah, my question was, like, so what you just discussed was to move this, logic into the login API instead of putting it in the general instrumentation?
So that, like, other requests can also use this logic?
And we convert it to Springs.
**Riccardo Magliocchetti** 19:37 Yes, something like that. And I'm sorry, but… I think, I did the suggestion to move it to instrumentation.
**guptaradhika** 19:46 Oh, that's okay. Yeah, Yeah, if everybody agrees about this, I can do that, and also I can check in, Node.js, like, if they are also implementing something similar, just to see, like, how other one works.
**Aaron Abbott** 20:02 Yeah, that would… that would be awesome if you could do that.
Thank you.
Appreciate it.
**Riccardo Magliocchetti** 20:23 Okay… I see, but… Tammy had some comments that I missed about the longing handler.
Is this something what you already…
**Tammy Baylis** 20:47 Hey, sorry, so… I'm having trouble following, but that's okay. We're moving… Issue 4330 is a question about whether we want to move the locking handler out of the SDK and into an instrumentation. I'm just wondering if we did move it, how that would, like, change the current example. If this example is even up to date, how it would change how users, use a logging handler? Like, is it just an extra import, or is it something else?
**Riccardo Magliocchetti** 21:28 Good point.
like… Or we can treat it as another… breakage?
Another break.
**Tammy Baylis** 21:43 Package, okay.
**Riccardo Magliocchetti** 21:45 Or, I don't know.
**Tammy Baylis** 21:47 Yeah, so… Yeah, if someone was doing a manual… instrumentation of… or manual setup of logging API usage, then… Yeah, they'd have to also install the, OTEL logging instrumentation package, and… do this differently.
Yeah, I was just wondering, I had a very late question, sorry about that.
**Aaron Abbott** 22:19 No, I mean, no worries. If you have concerns, we'd love to hear them.
**Tammy Baylis** 22:27 Yeah, I was trying to, on the issue 4330, the, like, the main argument against moving the logging handler Is that a high percentage of users want to set it and forget it?
I was wondering if that's… That's what this was, like a… very… not huge, but, like, a departure from how people have to set it up now. But I guess that it is a bigger question.
I'll just have a think about it.
**Aaron Abbott** 23:03 Okay, yeah, and feel free to comment on the issue, I'll, I'll try to… follow up there.
**Riccardo Magliocchetti** 23:13 Dan, thanks, Dan.
Okay… I'm curiously, I are against the OpenAI instrumentation.
And also, like, we have a bunch more of PR SMS that, sitting, in Contrib.
So, I was wondering if… Where is someone interested in reviewing it?
And eventually becoming a competent owner for that.
Because, again, like, I think that the, original GenAI approvers, Are not that active anymore.
And so… Yeah, like, since I think the OpenAI implementation is The most used we have.
Probably.
around Janae stuff.
It will, like… Would be helpful to have someone that… Can take a look.
Add that.
So, if you know anyone… Yeah, for example.
**Hector Hernandez** 24:40 for bringing this up. This is something that I have been trying to… review, there's too many Gen AI PRs these days. I have been trying to review plenty of them in JavaScript. It's nothing compared to Python, right? But, yeah, definitely happy to start helping with… with there, if we're getting overwhelmed here with all this OpenAI stuff.
**Dylan Russell** 25:09 Yeah. Sorry about that. I'm happy to review some of these PRs. I'm not… Sure, I want to commit to becoming an owner, but… Yeah Happy to review some.
**Riccardo Magliocchetti** 25:29 Thank you.
Both of you.
I think this was the last topic.
Any last minute one? I think what is so…
**Aaron Abbott** 25:53 Ricardo… I was gonna say, I can, I can… bring this up in the GenAI SIG. I know it's probably not… it's not at a good time for you, so I could bring it up next Tuesday and see if anybody's interested.
But I agree, we need… We need a healthy, like, review pool for some of these, because… I don't know, like, the collector is… the collector is doing this thing where they… Remove packages that don't have active cod owners and stuff like that, and… it seems like a lot of hassle to set that kind of thing up, but I also don't want to… have a bunch of dead code in our repo, but I can help review stuff here and there, but not sure I have a lot of context on being an owner.
Ricardo, you still there? You talking?
**Hector Hernandez** 27:23 Yeah, I think he had some internet issues, right? He was sharing the screen.
**Aaron Abbott** 27:27 Okay, okay, I was just… Is it me? Is it my speakers?
**Sergey Sergeev** 27:38 Yeah, I don't know if it's specifically related to Gen AI stuff, but it looks like everybody who works in this area Get so busy, and unpredictable, time allocation for… Previous flow requests, and etc.
By the way, do we have a policy that, pull requests can be… Should be reviewed by… People from two different companies.
Or is it only for semantic conventions?
**Aaron Abbott** 28:17 Yeah, we… we used to have something like that, and I think I think we relaxed it a little bit, maybe, like, 2 or 3 years ago, because it was… we weren't finding it super helpful, especially for, like, contrib with the whole component owners thing, because you know, if it's, like, AWS or GCP-specific thing in Contrib, So no, we don't generally follow that, yeah.
**Sergey Sergeev** 28:44 Yeah, one of the challenges, so it's relatively easy to motivate some coworker.
With whom you are in the same company.
To review your stuff, in a timely manner.
But, it's… Basically.
Exponentially harder if you need to get somebody else.
To review the stuff.
from another company.
**Aaron Abbott** 29:18 Yo.
Okay, well, I'll bring it up in the GenAI SIG for sure, this is… This is always a problem, but, are we?
I think Ricardo's back, but, that was the end of the agenda. Ricardo, do you want to say anything, or…
**Riccardo Magliocchetti** 29:37 No, like, I think I missed the… Most of the discussion on this point, so if you can recap a bit…
**Aaron Abbott** 29:49 Yeah, I mean, I think… I think Dylan said you could take a look at this PR. I said I could do the same, if needed, but I don't know about being a code owner, just because I'm not.
I wouldn't say I'm an expert in OpenAI.
And then I said I would bring it up at the Gen AI seg on Tuesday, because I know it's not a great time for you.
**Riccardo Magliocchetti** 30:08 Yeah, thank you very much.
**Aaron Abbott** 30:12 Yep, no problem.
Alright.
Alright, well, thanks everyone for joining. I guess we're, guess we're good.
**Hector Hernandez** 30:28 Thank you.
**Riccardo Magliocchetti** 30:28 Thank you. Thanks.
