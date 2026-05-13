SIG: Ruby SIG
Date: 2026-05-12
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/j_vhA18dpeTs7wyIiyCFVs9lzPcX321weN2a9J5-stxR_YUZXfx8gOrcTY4yJw.5hwyFlFpbZk60OaC
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:35 Hello there. How you doing today?
**Arjun Rajappa** 01:40 the fingers.
Over time.
**Kayla Reopelle** 01:46 I think this might be a quiet meeting and a short meeting, because we don't have, Arielle, or Rob, I'm not sure if anyone else… He's planning to join us.
And I've been fighting some kind of bug, so I'm not quite as prepared as I… to be.
But, I put the link to the agenda in the chat if there's anything you want to add.
Give people maybe another minute or two before getting started.
Alright, let's go ahead and get started.
Okay, so for the spec sig… The big announcement is that OpenTelemetry is graduating, which just means it's no longer an incubating project within the Cloud Native Computing Foundation.
It's reached a different maturity level, which, just kind of gives it different guarantees.
And, I don't think that much is going to change for us day-to-day, but, it is an exciting thing for the project as a whole.
Stable by default, conversation continues.
The spec is going to get rewritten, so that it's kind of clearer what actions people need to take to… Kind of, like, approve or agree.
So that's… that's… it's still in flux, and if it's something that interests you, I recommend taking a look at it.
Let's see, I…
**hramadan** 05:26 Question on that. Does that mean that the Ruby agent would be, like, pushed to do, like, a major version, a one-auto type of thing?
**Kayla Reopelle** 05:36 Or not.
**hramadan** 05:37 Not really.
**Kayla Reopelle** 05:40 I feel like I can't answer that right now. Yeah, I'm not sure. Oh, okay.
**hramadan** 05:48 read about it.
**Kayla Reopelle** 05:49 Yeah, I feel like it's more… like, yes, I do think that that could potentially be the outcome, that we would be, like, pushed to do a 1.0 version of, like, all of our instrumentation and everything else, but the conversation has continued to churn so much that I don't know if that's actually the outcome now.
So yes, yeah, please read it, I'm curious, curious about it.
**hramadan** 06:13 Yeah.
Yeah, I'll take… I'll take a look at that, it seems like I… Yeah, the implications of that are, like, not immediately obvious.
**Kayla Reopelle** 06:23 Yeah, yep.
I think those are the main things… That makes sense for us. I forget what this one is.
Yes, the telemetry policies.
This is another one to continue to think through.
It's like a… different way of doing configuration, from what I understand, at a high level.
But, I haven't dove into this one yet.
And so… I think… the best way that I've had it described to me so far is, like, being able to apply metrics views to every other Signal and things like that. But… Yeah, this is another one that's had, I think, a decent bit of churn, so I'm… I don't know what exactly it is.
Okay.
So… Nothing right now to discuss. Oops, I don't know why that opened.
Is there anything before we just start looking at issues and PRs that people want to go over today?
**hramadan** 07:50 Nothing from me.
**Kayla Reopelle** 07:53 Alright.
I think the main thing that I wanted to share is that, like, there was a big backlog of a lot of PRs, that got addressed last week, and so that kind of cleared up our release system, which had been blocked. I'm hoping now that that means I can focus on more of the, like, substantive PRs this week, like, like the OTL PPPRs you opened are June?
So, that's… that's my current plan, but this release should go out later today. It needs some editing, because… It has some changes that aren't really… relevant, but, this includes… Interesting.
The event name field will go out.
Trace-based exemplar.
And… the NOAP exemplar, like, those changes will all be out today, so… things… Things to look forward to.
Let's see… One… Interesting. This is… New to me.
I wonder if this is a new… field.
In the matrix.
Okay, well, you can keep that in mind. It's helpful to know about.
And then we have decorative configuration, suggestion, event name… Constance… And then still that response body bug that we're trying to work through.
Is there anything, that people want to look at together from this list?
**Xuan Cao** 10:44 Just one comment about this, what, what are the gems?
Talk about the decorative, configurations.
Yeah, I'm not sure if you guys, have looked at this. This is, really not, like, a weak job. This is very… this is big, so big, because currently I'm, I'm, Kind of working on the… The declarative configuration that's, integrated into, Oracle Agent.
It's just, is… is… Because if you look at those, I think, YAML file. It has a.
**Kayla Reopelle** 11:22 hoodies.
**Xuan Cao** 11:23 Huge of a list of, options that users can do.
And then, as a language agent, then we have to, consider Aries, Every aspect of that configuration files.
Hello.
Put into some kind of, automatic, SDK configurators, something like that. It's just really… Huge project.
Just to say it's good.
**Kayla Reopelle** 11:55 Yeah.
Yeah, that's a good… a good call-out. The issue does make it sound… Possibly simple, Yeah, there's a lot of things that we don't have support for, and this feels almost as big as taking on a whole new signal.
So, I do think it's something we should work on eventually, and if anyone's, like, ready to lead it, that would be great, but if not, I feel like focusing on stabilizing what we have in progress is probably a better… Focus at the moment.
**Xuan Cao** 12:32 Yeah, and then I think maybe, -Oh.
Somewhere… some… some… someone… And, like, triage, what needs to be done, Like, like, have the, the tickets?
Yeah, but just… just saying, this is a big, big stop.
**Kayla Reopelle** 12:57 Yeah, yeah, that could be a good next step, is to just, is what you're suggesting, like, figure out what configs we already support, and what configs we would need to add support for.
**Xuan Cao** 13:09 Yeah, yeah.
Okay. Or, Make more of a… Actionable items?
Yeah.
**Kayla Reopelle** 13:22 Yeah, yeah, have that broken down, definitely.
Yeah, it would be nice to receive this, too, in the form of, like, smaller PRs that build. Those are a lot easier to review.
I guess I'll have this… talked about it.
Alright, let's see… What's going on in Contrib?
Got a lot of Renovate PRs.
Interesting. Something about toys… One thing… I guess I wanted to check, just because we've been moving towards it for a while, is how the… Auto instrumentation, pull request is going. I'm… I'm feeling pretty… good about it. I saw that you, Sean, looked at my comment.
And… I don't know where it is at the moment.
Yeah, down here.
Oh, okay, I'm sorry, I totally missed your follow-up.
I think… Yeah, I guess maybe what I'm, not sure about is, like.
Why create the resource on the outside?
Before, instead of letting the configure Method do it.
Is it just because of the resource detectors? Does the, does the configurator ignore those?
**Xuan Cao** 16:00 Hmm.
Do you mean put them into a single line?
**Kayla Reopelle** 16:08 Can you say that again?
**Xuan Cao** 16:12 I… do you mean, the line 126 and 127 into the 12… 120 to go, like, all together? Is that, what you're, suggesting?
**Kayla Reopelle** 16:31 No, I think… I think I just answered my own question, though, while I was looking at it again. I forgot that the resource detectors were part of… contribib, and so… That's not something that, the configure… the, like, standard configure call would necessarily set up. So you need to create that resource at some point, right? And so that's what you're doing before calling configure.
**Xuan Cao** 16:58 Whoa.
Y-yeah, yeah.
**Kayla Reopelle** 17:01 Okay, okay, sounds good.
Okay, then we can disregard that one, and I'll, mark it as resolved. But that was my only… Yeah, my only hesitation. I wonder what you think about, like, Arielle's reviews and James' reviews as to… Like, whether, do you want to wait for an approval for them before… We move forward.
**Xuan Cao** 17:37 I think most of the Ariel's comments are, like, from AI, I guess. I don't know.
**Kayla Reopelle** 17:42 Okay.
**Xuan Cao** 17:43 But anyway… I asked him again before he, on PTO, and then… And then, for other comments, I think, are… they are just more, more, like, suggestions, but nothing related to this, this, this here, this, this chair.
And, And again, this is… this gym won't… affect any other champions is, standalone.
The only thing would be, probably I should turn off those, dependent bots or renovate on, on this, Out of the gym, because… It will create a, create another, noise.
Oh.
And then, to be honest, I think I mentioned somewhere in the thread that eventually.
it's better to move this out of this country repo, but I don't know how to create this repo under OpenTelemetry. So… yeah, yeah, that's fine.
**Kayla Reopelle** 19:02 Yeah.
**Xuan Cao** 19:03 My own comments, yeah.
**Kayla Reopelle** 19:05 I can work on, getting… another repo set up for you. I think I might have the ability to do that.
Do you want the initial release to be, In this contribrib, or would you rather it be in a separate repo?
**Xuan Cao** 19:27 I mean, if you can make a separate repo, then we can do this thing separate, so we don't need to, like, upload the Git history.
**Kayla Reopelle** 19:36 Yeah, yeah.
**Xuan Cao** 19:37 Yeah.
So, I mean, if you can do it, yeah, I'm happy to, you know, move to the new, new one. But now we have, like, 3 reports to monitor.
**Kayla Reopelle** 19:48 Yeah, yeah, that does… Make it more complicated.
**Xuan Cao** 19:53 But I think that that's okay.
Yeah, yeah, I think the line of code is not that big, I think less than 100, so it's maintainable.
Yeah. Yep.
**Kayla Reopelle** 20:09 Yeah, yeah, I think so, and I think it… All of its renovate changes not showing up in the same… field as the rest of Contrib is going to make it more maintainable, too.
So, so yeah, I will look into that this week, and… see, see how complicated it is, and then I can bring that back for SIG next week, or let you know in Slack if it comes up more quickly.
**Xuan Cao** 20:35 Okay, okay, current cycles.
**Kayla Reopelle** 20:38 Yeah.
Alright, anything else in Contrib?
**Xuan Cao** 20:46 Oh, oh, sorry. Oh, one more thing. So, once you have… The new repo, is it possible to move this?
you're into that, because I kind of want to make, like, I don't know if, the, all the comments, like, those, stripes.
I'll be there to, to, to, to, for the reference, because, you know.
They're, they're kind of, helpful to,
**Kayla Reopelle** 21:15 I understand.
**Xuan Cao** 21:15 Why something happens in this way, so…
**Kayla Reopelle** 21:19 Yeah, that's a good question. Yeah, I'm not sure, but I'll see if anyone, else knows and can help.
**Xuan Cao** 21:27 Okay, thank you.
**Kayla Reopelle** 21:46 Let's look at the issues… Nothing new since last week.
Okay, yeah, is there anything else in Contrib that people want to talk about today?
Alright, well then, I think… We can call it early, and… Get to work on the to-dos, hopefully get that release going.
Don't know if we had a release this morning already for Contrue. No, it doesn't look like we did.
But I'm sure Contrib is almost ready for one, too.
So, we'll… yeah.
We'll look at that and get it moving, and yeah, my hope is to also review those, OTLPRs that you opened this week, Arjun, so… Cool. All right, well, thank you, everyone, for coming, and for, you know, chatting about this stuff with me today, and we'll see y'all next week. Love it.
**Xuan Cao** 23:14 Thank you. Yeah.
**hramadan** 23:15 I think I know.
**Kayla Reopelle** 23:16 Bye.
