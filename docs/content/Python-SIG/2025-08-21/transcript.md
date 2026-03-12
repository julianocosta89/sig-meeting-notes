SIG: Python SIG
Date: 2025-08-21
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:55 Hello.
**John Scancella** 05:00 Hello!
**Shuwen Pan** 05:01 Hello!
**Riccardo Magliocchetti** 06:44 So, welcome, everyone, to this week's Python Sq course.
We'll wait just a couple more minutes for more people to join. In the meantime, please add yourself.
As an attendee.
To this… to the notes document.
And also add any last minute or topic you want to discuss. Thank you.
Okay, so… we're 5 minutes in, I think we can start. Welcome, everyone, again.
To which we call patency code.
So, the first topic for today is from me.
… Yeah. I created the PR… Adding, sorry, it's a bit noisy there. Okay, I create a PR, for, teaching the outer instrumentation code.
about… GEvent application.
Because, usually, like, salespeople like big demos in Kubernetes, and some of these demos use locust as a load generator.
And at the moment, We're not able to instrument GM device application without instrumentation.
So… Yeah.
Which is more or less an act.
But, yeah, if you have time or interest in the topic, please take a look.
And then… Second topping is also from me.
But it is, but… we're doing some cleanups on the… Admin repo.
And… We have, like, a strange configuration on our… code owner, file in, contrib.
So, like… Like, as far as I understand, at least from his comments, … Component owners, … Will be the… with the changes proposed to the admin, … Repo, what is the… usually the Terraform scripts that configure the various repositories.
We'll need, like, Component owners, approval to merge stuff for instrumentation.
But the problem we have… Is that… … We don't have many eye.
Active, code owners, and so we're just asking for, you know, clean up our list.
And… yeah.
**lechen** 11:28 Yeah, I think for historical reasons.
**Riccardo Magliocchetti** 11:31 So… repo is private.
That's my computer.
And so, if any of you wants to be a competent owner, a competent owner for our instrumentation, just give a shout-out.
And we'll probably find a way, like, I'll probably find a way to… To see if the current component awards are active, since a few, or… Try to ping them.
… yeah.
Maybe next week, I'll open a PR with… I revised, … Compared to one's list.
**lechen** 12:14 Hey, Ken, is my mic working?
Agreement?
**John Scancella** 12:19 Yeah, we can hear you.
**Riccardo Magliocchetti** 12:19 and your opinion?
**lechen** 12:22 Oh, nice.
… So… Ricardo, do you know if, the new changes an admin.
… Component owners is probably not part of this, right?
**Riccardo Magliocchetti** 12:41 Sorry, like, I had my… my audio muted, so I wasn't listening to it, sorry.
**lechen** 12:50 Just specifically me muted. Just talking too much.
… Can you hear me now, Ricardo?
**Riccardo Magliocchetti** 12:59 Yeah, yeah, right now, yes. Sorry. Oh, mate.
**lechen** 13:03 No problem.
… Yeah, so for historical reasons, the reason why we're using component owners instead of code owners was because, there are various contributors that were not part of the OpenTelemetry org that still wanted to kind of have a degree of ownership over certain instrumentations.
This is why we set up our code owners like this. So code owners are specifically for Assigning… reviewers, but more importantly, your reviews will be green.
For the certain namespace that you're under.
Component Owners doesn't do that. Component owners only assigns, … Your alias if a instrumentation is touched that you own.
So… with the new changes in admin, I believe it's, you require… someone to being code owners. I don't think this will change anything in the way we, … in the way we currently are doing things. But the only other administrative task, like you said, which is separate from this effort from admin. We do have a bunch of… Component owners that are… … I guess.
they don't… they aren't actively contributing anymore. This still kind of presents the problem in which, like, … the… maintainers or the approvers of the contrib repo will now be the catch-all for everything.
I think that's okay, like, the way that we've been, … Dealing with, like, issues for instrumentations that we don't have that much experience in, is if… if, like, the community cares about it, like, someone will pick it up.
So, I think a cleanup of the component owners is fine, but it's not, like.
We have to do it because of this.
This new, new thing, so….
**Riccardo Magliocchetti** 15:18 Okay, so… So, you said that… We don't need to change the code owner's file.
**lechen** 15:28 … Oh, no, no, I'm saying the com… we still need to change the code owners to remove the instrumentation.
But I'm saying, like, the cleanup of component owners is, like.
**Riccardo Magliocchetti** 15:42 Okay.
**lechen** 15:42 Separate. Separate from this task, yeah.
**Riccardo Magliocchetti** 15:47 Kind of, sure.
Yeah.
Awesome. So thank you for bringing some history on.
**lechen** 15:54 Yeah, yeah, I was.
**Riccardo Magliocchetti** 15:55 Let's all.
**lechen** 15:56 Yeah, we had to deal with this, like.
Finding a good way to, like, manage the… contributors was difficult. There was no good, clear solution.
**Riccardo Magliocchetti** 16:23 Okay.
I think we can move to the next topic, unless you have any questions, or… Comments?
Okay, next topic from John.
**John Scancella** 16:50 Yeah, I don't know if you want me to speak to it, but basically, just was trying to help out with some of the documentation stuff that I mentioned a few weeks ago. Did a pull request, I know some people, commented on it, just wanted to see if there's anything else you needed from me.
you know, I understand it takes a while to merge stuff, whatever. I just wanted to make sure you weren't waiting on me, is all.
**tammy.baylis** 17:22 Hi, John, I can speak to this a bit, because I was the reviewer. Yeah, first off, welcome, and thank you for putting the PR in. I just left a comment right now.
On one of the… one of the existing comment threads on this PR, and there are still some CICD failures after, you added my suggestion, so my suggestion didn't fully fix things.
It's… it's okay if the various instrumentation tests fail on this PR, because this… this is a doc's PR. Oh.
Yeah, sorry. So, if the instrumentation tests fail, that fails, that's probably okay, because we know there's some flakiness issues, but there's still some… Sphinx issues, and, I think the quickest way to get around this, would be if you could run talks-edocs on your local, then you should be able to see Hopefully the same errors, and you can, more quickly address any remaining formatting issues.
**John Scancella** 18:29 Oh, okay, perfect, yeah, I'll give that a try.
**tammy.baylis** 18:32 Yeah, thank you.
**John Scancella** 18:34 Yeah, thanks for the talks. I… I didn't know I could do that. That's perfect.
**tammy.baylis** 18:40 Sweet. Cool.
**Riccardo Magliocchetti** 18:46 Thank you both. Let me add it to the notes.
Okay… And then, next topic from Sergeye.
I'll say pinkularity.
But I don't see Sergeye connected.
So yeah, maybe we shouldn't… Just keep it for now, and the next one is… from Dylan.
**Dylan Russell** 19:28 Hello?
Yeah.
This one is kind of a small PR.
That was just filtering out some logs that otherwise might… Cause problems if, like, the logger itself is down?
… And I'm just wondering if someone else can take a look and… review it, and… so I think it's pretty much good to go.
But yeah, basically just… If we see the same log… Like, within 60 seconds or something?
And it's coming from, like.
it's one of our logs that we log through the logger, then we'll, like, filter it out. We won't… we won't try and log it.
So, yeah, that's pretty much it.
**Emídio** 20:31 This is a case of the… Infinite loop of login when the collector is shut down.
**Dylan Russell** 20:40 Yeah, exactly.
The logger is down.
**Emídio** 20:45 Nope.
**Dylan Russell** 20:45 When we log something.
And then….
**Emídio** 20:48 Yeah, we'd end up in, like, an infinite.
I've tested your PR, and I remember it fixed the issue.
But I don't remember why you didn't adopt a warning stat.
**Dylan Russell** 21:02 So, say that again? Why it didn't….
**Emídio** 21:04 Why didn't it adopted, instead of tutoring, we just, used warnings module.
from Python build teams.
**Dylan Russell** 21:17 … Not sure what the… yeah.
**Emídio** 21:23 Because with the warnings, we… It, the log message won't go through their login handle.
**Dylan Russell** 21:31 Oh… I think some people are saying we still want like… The log to go.
… like, we still want to see… potentially want these logs to be written through, like, the OTLP handler.
… It's just… We want to prevent this issue of, like, the endless slogging.
When, like, the logger is down.
**Riccardo Magliocchetti** 22:03 Yeah, like, I think the issue with the warnings module is that I think Aaron pointed out.
But there is a way that you can convert warnings into plain logs, and so you….
**Emídio** 22:15 you get the loop again. Yeah, yeah.
Yeah. Okay, then.
**Riccardo Magliocchetti** 22:27 So yeah, I'll try to take a look at it, but… I say the same for every PR, but I don't hear me in the background.
But yeah, I remember I've already seen it, so I'll just… Thank you. Thank you, Lee.
**Dylan Russell** 22:48 Alright, cool. Sounds good.
**Riccardo Magliocchetti** 22:56 So… Sergey is still not here? Maybe, maybe… So, I see there are colleagues from Cisco.
Maybe… Man web….
**Pablo Collins** 23:17 Yeah, I don't know where Sergey is. We have a… larger meeting at Cisco right now, so he might be in that.
**Riccardo Magliocchetti** 23:24 No, like, maybe you're aware of the topic, so, like….
**Pablo Collins** 23:29 Yeah, I don't know.
**Riccardo Magliocchetti** 23:29 Okay, okay.
Okay, so… any last-minute topic?
Otherwise, like, I think we can move this next week, or Slack.
**Dylan Russell** 23:59 Sounds good.
**Riccardo Magliocchetti** 24:01 Okay, so… Thank you, everyone.
**Pablo Collins** 24:06 Thanks. We are 40 minutes back.
**Dylan Russell** 24:09 Gotcha.
**Riccardo Magliocchetti** 24:09 Thank you.
**Shuwen Pan** 24:12 Thank you, bye.
