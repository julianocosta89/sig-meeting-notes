SIG: Python SIG
Date: 2026-01-08
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:19 Hello, hi everyone.
**Riccardo Magliocchetti** 01:25 Hello.
I'm definitely real, everyone.
**Liudmila Molkova** 01:32 Happy New Year!
**Riccardo Magliocchetti** 01:51 So, welcome everyone to this week's Python Weekly.
SIG code.
We're waiting a few more minutes for more people to join, but in the meantime, please add yourself.
to the sign notes.
And I'm not sure I shared the link on the chat.
Maybe yes?
Maybe don't.
Okay, I have an empty chart, but I pasted the link. Okay.
What else?
**Liudmila Molkova** 02:37 Not empty for you, then.
**Riccardo Magliocchetti** 02:40 Okay, thanks.
And, of course, if you have any topic you want to discuss.
Also, feel free to add them to the agenda.
Okay, it's a 5, I think we can start.
Okay, I added a couple of…
Items here in the topic list.
I don't know if Lyudmila, maybe to let move at them above, but anyway, just quickly…
Thanks. A couple of quicken… Announcement? Or reminders?
And… yeah, like, this end of year.
I haven't time to work on the block stabilization task we have left to complete our… Planning?
Yeah. If anyone want to tackle them, feel free.
One, I think it's a bit more complicated than the other. This one, 4330.
It is about, like, moving the…
Logging handle outside of the SDK module.
And the issue is… is… there is…
How not to break, compact?
for user home.
Obi.
But no need to go into discussion. If anyone is interested, you can either comment on the issue, or just chat on Slack, or the next will be cool.
And when the last, request, if any one of you have time.
We have plenty of PRs, to review, both in country and core.
And any well-paced welcome, as usual.
Aaron?
Yeah.
**Aaron Abbott** 06:28 a year.
**Riccardo Magliocchetti** 06:30 Clip here.
Yeah, this was it for me.
Yodimila?
Do you want to share the screen?
**Liudmila Molkova** 06:40 Yes, please, thank you.
I'm actually…
unrelated, but I'm super excited to see all the log stabilization efforts. Thanks a lot for driving this.
I wanted to chat about… Life checking and, check-in, automating the… some kind of compliance.
I've started… I've done the POC in GenAI, I shared on the GenAI call, but essentially we can…
validate, Pretty much arbitrary instrumentation.
compliance against semantic conventions. It has some limitations for spans, but we can work around it, or at least start with validating metrics.
And… logs?
this is proof of concept, and I know, Ricardo, that you've been also looking at this. So I wonder, maybe we can chat about how we see this in general?
And, for example, Ricardia, you mentioned that you're interested in more, like, end-to-end data instrumentation. So maybe you can share your view on this, and we can, try to make it happen?
**Riccardo Magliocchetti** 08:07 Yeah, sure. Like, I started looking at Weaver, like, yesterday, so this is, like,
really new to me, but I can share…
non-working branch. I worked on it today.
I'm adding it to the…
To the agenda, and my idea is… like… I see, like, running Weaver and,
And testing against it, more something like… End-to-end, or integration tests?
And…
Because, like, one thing, the first time I tested it, I found a couple of issues we have.
One in the… System matrix package, and this branch also varies the fix.
And,
And one in, the Flask HTTP instrumentation, a trivial one. But, yeah, like, in this branch, I've stolen your, Weaver container.
Just for testing, but, like.
The Benji is not working, and…
like, I do fix other issues around that, but my idea is that, like, to provide, just a bunch of examples of
real… real word is a big, like, DIM application we want to install.
And run out instrumentation around them.
And then check that… The stuff with… the telemetry we support is valid.
So it's, like, really high level.
And the idea is that Yeah, like… we test… Something that looks real.
And hopefully, one day, everything will be without warnings from Weaver, I hope.
**Liudmila Molkova** 10:18 I see. So, like, you would, run something like this?
Use Fest API operate.
And you would just let…
forward whatever telemetry from it to Weaver, and it would validate.
The compliance, you're not particularly interested in validating that certain metric was omitted, but whatever was emitted was compliant.
Sorry, have I… have I lost everybody?
**Aaron Abbott** 11:01 No, I still hear you.
**Liudmila Molkova** 11:04 Okay.
**Riccardo Magliocchetti** 11:05 No.
I think I lost you.
**Liudmila Molkova** 11:10 Oh, sorry.
**Riccardo Magliocchetti** 11:11 But.
**Liudmila Molkova** 11:12 Yeah.
**Riccardo Magliocchetti** 11:12 Yeah, but…
Please go ahead, sorry.
**Liudmila Molkova** 11:19 So I was just confirming my understanding that you would rather run the application and do a bunch of things and then,
just let Weaver complain if it sees something not compliant.
**Riccardo Magliocchetti** 11:31 Run the application, do a request, and then tear down the application, and check the… Whatever we were reported.
**Liudmila Molkova** 11:46 And we would have the integration tests, which are, like, the combination of different instrumentations, rather than a single one, like Flask. It would do more than just one thing.
Sorry.
Ricardo, I think I'm… we are losing each other.
**Aaron Abbott** 12:19 Yeah, I can hear you still, Luna.
**Emídio** 12:21 If you are muted, Colin.
**Riccardo Magliocchetti** 12:24 Yeah, I think the issue is on my side, but, like, I'm missing…
Some audio from Julie de Miller.
And so, like, I don't know how to answer, because I missed the most of the questions.
**Liudmila Molkova** 12:39 Yes, and maybe, maybe let's chat on Slack, I'm, I'm…
**Riccardo Magliocchetti** 12:43 Yeah.
**Liudmila Molkova** 12:43 Definitely, whatever we can do to automate, but let's do this, and let's chat on Slack on
How to move it forever, time up, and any suggestions.
**Riccardo Magliocchetti** 12:54 Yeah, thank you.
**Liudmila Molkova** 12:59 Thanks.
I wanted to, use, your Precious time to… Help me… Love.
this front… However, there are some trivial changes to GenIOTLs.
And I think the only thing that's… Sorry.
This one.
The only thing that's not resolved yet is… the… the comments… Here.
Is this the right way to write comments? Should I write them in some other way? The comment goes under the property. Is there a better way?
**Aaron Abbott** 13:59 This is like a doc string, right?
**Liudmila Molkova** 14:02 Yeah, this is, like, a dog string.
**Aaron Abbott** 14:04 Yeah, no, this is… Right, I think maybe the question was which one it's attached to.
But yeah, it goes underneath.
**Liudmila Molkova** 14:16 Yeah.
Okay, then I'll leave a comment. I… I think it… yes, it's kind of confusing, but if it's the common practice, then…
Let's keep calling it.
Leave a comment, I would appreciate the review.
And…
The only other thing I wanted to share that I would like to switch to Gen AI OTLs from the OpenAI, once it's in.
We would need to… release Gen AIO tools?
And then, well, we don't have to release if we…
don't release OpenAI, but before releasing OpenAI, we'll need to release Gen AI tools. Any concerns with leveraging Gen AI tools?
**Aaron Abbott** 15:09 Nope, not at all.
**Keith Decker** 15:10 I think the one I have is that we still have events pending. Would you need events for…
Opening our yard.
Or do you just need, spans and metrics?
**Liudmila Molkova** 15:23 I would like to have everything, but since we are…
Switching to the new version, it's opt-in for users anyway, right?
I'd like to leverage the genial tools, and if…
we… once we add events to OpenAI, we add them to the OTLs rather than individual libraries.
So it's also a forcing factor.
**Keith Decker** 15:58 Okay, sounds good to me.
**Liudmila Molkova** 16:01 Cool.
Thanks a lot.
then let's get this in, and let's, I'll continue working on the OpenAI. Thank you.
I'm going to… Stop sharing.
And… and the tower.
To Lucas.
**Lukas Hering** 16:24 Let me share it here quick. My question is more of a high-level question.
But I will try to be quick.
artist.
Okay, can people see… this… PR page.
Yeah, so,
just for some background, so in the contribute repo, we have instrumentation for BotoCore, which is the…
AWS SDK, or the lower level SDK for Python.
I was looking into adding support for the async I.O. implementation.
And I know I was digging around through some older issues, and it actually looks like there were attempts to do this and just make it its own library at some point.
But I think it was just not approved due to, like, scope limitations.
But the… this library is actually almost identical to Bodacore, so I was actually able to just add support directly into the BodoCore
Library to just… Basically, it's, like, 95% code reuse.
You just would need to patch the additional async functions.
So the question I have is, like, what…
And I know, Ricardo, you've made some comments here. I just want a little more clarification here, for how… if we are going to decide to go through with this
what should the entry points look like for this in the PI project TOML, and…
do we want to give people the ability to, like, just instrument AIO Boto Core, just instrument BodoCore, or do we just make the assumption that
If they have this…
package installed, then we'll just check if the AIOpoto Core dependency is installed, and then instrument it in the instrumenter.
**Riccardo Magliocchetti** 19:02 Yeah, like, I think, your code is fine, like, the entry point is… the separate entry point is fine, but, as my comment says, like.
We already have… Way of…
Providing, like, the same instrumentation or package for different, instrumented libraries.
And what is the syntax?
you should use, but apart from that, I think the rest is mostly fine.
So, like, the behavior will not be different when what you try to express, but the syntax is just a bit different.
**Lukas Hering** 19:42 Oh, okay.
**Riccardo Magliocchetti** 19:44 So, because, like, the syntax I'm showing there.
Is, understood by the tool we use to generate, the mapping between the variable instrumentation and the instrumental libraries.
And so it will create proper…
stuff that will be used by, a tool we have that is OpenTeometry Bootstrap.
**Lukas Hering** 20:09 Right, I guess my condition here is that…
**Riccardo Magliocchetti** 20:11 The one you expect.
**Lukas Hering** 20:14 Yeah, like, this instrument's any, from, like, from digging into the code, it seems like… It, will…
I think it will just check to make sure that only one of these is installed, right?
Or is… or am I… I guess I can take another look, but…
I think that's all I have, then.
**Riccardo Magliocchetti** 20:50 Okay, thank you.
Yeah, like, we can… I haven't took a look after you updated it, or responded to my comments, so I'll take another look, and maybe we can discuss.
on the APR.
**Lukas Hering** 21:05 Thank you.
**Riccardo Magliocchetti** 21:06 But…
Yeah, like, from my side, I don't have a problem in adding support for both libraries in the same instrumentation.
**Lukas Hering** 21:17 Got it, yeah, I think it's probably the better approach to follow anyways.
I have one other, just, like, small comment. I know you mentioned there's a lot of, like, contribute PRs that need reviewing. I haven't… I've only been contributing for, like, maybe 2 months here, but…
I don't have a prover role, so I'd be, like, more than willing to review PRs, but, like, for now, I don't have a prover, so it doesn't really make a difference,
what is, I know, like… I guess,
Yeah, I guess, what's the general… I know I've read the contributor docs, but… What's the expectation around…
Having a proverbird.
**Liudmila Molkova** 22:15 I think this is the best contribution to make to the open source project, is to review PRs. Please do, even if you don't have approver status. If you consistently contribute by reviewing pull requests, this is a great way to become an approver. Sorry, Python maintainers, I didn't want to speak in front of you, but…
**Aaron Abbott** 22:35 It's emotional.
**Lukas Hering** 22:36 Okay, got it, yeah. I've kind of done that a little bit. Yeah, I just didn't know if, like, there was any point in me even reviewing if I don't have a prover, but yeah, I'll just keep doing that then. Thanks.
**Aaron Abbott** 22:49 Yeah, I was… I was gonna say the same thing as Ludmilla, that's… that's awesome, and
It definitely helps, especially… we also have, like, this code owners thing, and if you have any packages that you're…
you have a lot of knowledge and stuff like that, we can add you to the code owners and stuff like that, so… even if the checkmark's not green, it's… it's helpful, and…
Yeah, we always need more approvers, so…
It's a good way to get in that, in that route.
**Keith Decker** 23:19 So to piggyback off of that, if I'm listed as a code owner for, like, GenAI utils, but don't have approver status.
Just keep reviewing ones that's come in, and just… Go from there.
**Aaron Abbott** 23:33 Yeah, pretty much, like, I think…
I think there's some formal requirements, but we're usually honestly pretty loose about it.
**Keith Decker** 23:40 Okay.
**Aaron Abbott** 23:41 some SIGs have, like, a triager role. I think, Ricardo, actually, we were having some issues with the auto-assign bot with the code… with the code owners. Or not code owners, it's called component owners, it's like an hotel workflow, but…
Yeah, unfortunately, GitHub makes it kind of difficult to give people green check.
For… without giving them access to the whole repo.
**Keith Decker** 24:06 I see, gotcha. But yeah. Okay.
**Aaron Abbott** 24:10 Thanks, Lamilith.
**Lukas Hering** 24:22 I didn't have anything else, so…
**Riccardo Magliocchetti** 24:37 Okay, so this was the last topic for today.
Any last-minute topic?
Okay, so… Thank you, everyone.
And see you.
in the next SQL.
Thank you. Have a nice day.
**Liudmila Molkova** 25:01 Thank you.
Thank you.
**Lukas Hering** 25:04 Thanks, everyone.
