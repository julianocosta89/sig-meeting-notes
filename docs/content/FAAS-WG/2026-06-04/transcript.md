SIG: FAAS WG
Date: 2026-06-04
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Raphael Manke** 04:44 Hello.
**Warre Pessers** 04:46 Hello. Yeah, the AI note-taker thing joined again, but, I don't have permissions to, change stuff in this meeting, and I think Tyler was busy at the moment, so… Guess it's joining again for this meeting, but… I'll see, I need access to some sort of document to… request permissions to this… to be admin in this Zoom call, but… Yeah.
As long as I can't access the document, I can't request the access, so… Stuck with it for now.
And now I see that the bots posted something themselves, so maybe I can…
**Raphael Manke** 05:42 know now who is responsible for it, this person.
**Warre Pessers** 05:46 Yeah.
**Raphael Manke** 05:46 Namely.
**Warre Pessers** 05:48 Yeah, indeed.
Okay, but the command triggered it to leave, so that's good, I guess.
Let's maybe wait one more minute to see if anyone else joins, and otherwise, Can kick over the meeting.
I guess we can get started. So, I see someone new joined as well.
Maybe you could introduce yourself? I can…
**Sidartha Gracias** 06:58 Can you hear me? Yeah. Yeah, I'm Sudhartha. Yeah, I was just joining to listen in. I work on the Splunk team, and I've managed the Splunk serverless races, so I was mostly just joining to listen in this time.
**Warre Pessers** 07:12 Okay, cool. Just interrupt me if you have any questions about anything we discussed, but I don't think it will be that much on the agenda today.
**Sidartha Gracias** 07:21 Got it, yeah, sure.
**Warre Pessers** 07:24 Okay, so there was this one action item that Max added. I recall him… talking about it a couple of weeks ago, about some, stabilization of some semantic conventions.
Yeah, I guess, I can take a look at this, see what would be the actual process, because I don't think we would be… able to resolve this in the current meeting. I'll have to contact some people, On the semantic conventions seek for that, so… I will check that.
Just a sec.
**Raphael Manke** 08:07 Yeah, I think maybe he wanted to join, but somehow didn't make it.
**Warre Pessers** 08:12 Yeah, I'll, shoot him a message after, but, it's fine.
Other than that, I can take a quick look at the current open PRs and some issues, maybe, unless you had anything you wanted to discuss before.
Okay.
**Raphael Manke** 08:32 Not really. The only thing we might discuss today is your integration test progress. Is there something that you need help with, or anything that's blocking you?
**Warre Pessers** 08:42 Yep, we'll definitely get to that in a second.
So maybe just also a quick note, don't know if you've seen it in our, so, for Siddharta's information, Raphael is an approver on the project, and I'm a maintainer, so there's some private chats with, Stuff that's relevant only for maintainers, But, basically, I notified people there that there were some issues being opened, and some comments being placed by some, Chinese bot accounts about… some sort of bot activity on the repo. They were claiming that we had 16,000 stars and 50 forks or something, so it doesn't even match the actual numbers that the repo has, but I asked GitHub support to look into this, and they… basically, they just came back to me, they didn't say anything about, stars or forks, but they just said, yeah, we blocked all those, Chinese spam accounts, so… Not sure what that was about, but, was quite… Weird to see all the issues and comments being placed, but that should be resolved for now.
Then, so I think most importantly, I'll quickly note for these two issues, these are people tracking CVs. I'm not necessarily a fan of people opening issues on the repo for that, but it's not that big of a deal.
Both of these should be resolved next time we release the collector layer, because I believe that we have upgraded all those dependencies that were causing those. But before I do the release, I'll check anyway. We should be good there.
And then, next, maybe… most important that I would like to discuss is indeed, as Rafael said, we have some initial work to get some integration tests going, so the idea is basically to have some sort of smoke check that the instrument… the other instrumentation from the language layers is working, and also the collector layer is used in all of these, so we can verify that the collector layer is Properly exporting the telemetry data.
So I set up something very, basic with, just exporting spans to the console, to standard out, and then we query CloudWatch to verify that those were actually, generated.
And that initial work, I think, is done, and indeed, I noticed yesterday or two days ago, Rafael approved, so thank you for taking a look, but I was also… looking into the original issue, and I kind of forgot about your earlier comments, because the, CloudWatch has, since a couple of months ago, released that OTLP endpoint, and I think that's a very good point that that will be, that would actually be the right, thing to use here, so our collector should really be exporting to that endpoint. So I'm basically just… I don't know what your preference is, maybe, Raphael, but I would be down to just, include that in this PR as well, or we can merge the PR and, track some improvements in the follow-up issue. I don't really have any preference, Regarding…
**Raphael Manke** 12:30 I would, merge it now, so you are also unplugged to release new layers already with this approach, and have those tests easy, runnable, and then we will expand it to a better state later on.
**Warre Pessers** 12:44 Yeah, I think that's… that's a good point. If we merge integration tests now, I'll do a release also, this weekend, probably, and then we can indeed do the work later, that's a good idea, yeah. Okay, so I'll, I'll take care of creating a… follow-up issue, I guess I'll… I had put some to-dos here based on your comments, but I will be converting those to One or multiple issues, and you can look into, Yeah, I'll happily do the work, but if you or anyone else wants to jump in, that's fine by me as well.
So, I will take care of that.
**Raphael Manke** 13:29 But I think, technically, all signal types should be supported, so you should be able to emit logs via the OTLM point. There are some specifics, you need to send some headers to route to write, lock group.
Then for spans, they will land in the transaction, so it's AWS spans log group, so that's the same as, other exporters. And then for, metrics.
They will also expose to… export it to CloudWatch Metrics. There I see, might be there's an issue with latency. We need to check, Or how do we identify the metrics data points to be one.
**Warre Pessers** 14:12 Yeah.
**Raphael Manke** 14:12 our execution.
**Warre Pessers** 14:14 Yeah.
**Raphael Manke** 14:15 because high cardinality data will be more expensive for AWS, so we need to see how we can.
**Warre Pessers** 14:21 Yeah, exactly, I haven't thought that through, but yeah, maybe, like, definitely splitting up metrics as a signal to… Take care of on its own would be a good idea, just for all those nuances to be properly, looked into.
**Raphael Manke** 14:40 Also, I'm aware that AWS is working in that direction to re-factor some of the stuff, so maybe we will add that later on. Maybe Max can enlighten us, because he's in the team building these new capabilities for Lambda and OTEL.
**Warre Pessers** 14:53 Yeah.
Yeah, okay, good, good input, thank you.
Let's take a quick look at the other issues… Yeah, this is mainly for tracking on my end, because we added the transform processor in the last release, so I will do a… actually, after this meeting, a quick PR to remove these processors, so we can, in the next release, already have only the transform processor. I put it as a warning on the latest collector release that these would be removed, so we're good to go ahead with that, I guess.
This one… I think…
**Raphael Manke** 15:37 That was, state-of-the-art analysis with what I think is right now not optimal. The locks parsing of the telemetry API receiver is, not respecting structured locks, really, or not very well.
Yeah, that's just a tracking issue. I can draft something, but there were also some questions if we really should do it, and… Yeah.
**Warre Pessers** 16:05 Mmm, yeah, I have a hard time remembering, I'll… I have to, after the meeting, I'll look at this one again, because I have read this before, but, Yeah, I see that I put the labels on it as well.
Yeah, I'll, I'll take a look. My bad for, for, my memory loss, but .
**Raphael Manke** 16:30 I'm also not sure if I find time in the next few weeks to really work on that, so…
**Warre Pessers** 16:36 Yeah, fair. And all the others are some bit older issues. From time to time, I come through this, answer some people if required, or close some issues if people forget to close their own issues.
But for now, I'm not going to go too in-depth. I did do… I'm on my corporate account… I did clear up some of the, security advisories here, Most of these were in-dev dependencies that are not really relevant for production use of the layers, and here we have some generic advisory to pinned versions everywhere. I have taken care of that in the past for… in some places, so… It's just whenever I would find time, I will create an issue, or, do it myself, but for now, it's not that… not that critical to look into, I guess.
**Raphael Manke** 17:35 But are we tracking those, reported CVEs? So do we have our own CVE scanners or layout scanners somewhere set up?
**Warre Pessers** 17:43 The only thing that's set up right now is, that dependable, report CVEs for known, dependencies that we use. And it's also possible for people to, like, privately report the CVE for the layer. So… I'm not entirely sure why, but the CVEs that we see reported here.
They should, in fact, also show up thanks to Dependables.
in here, but, they don't. So, maybe that's because I've already merged those PRs to upgrade those versions, because these are basically CVEs that only exist now in the current layer version, but not in the current code. So, Yep.
Not sure if it covers everything, but the only scanning we do have is just dependability reporting, what it knows about our current dependency versions.
**Raphael Manke** 18:48 Enter.
**Warre Pessers** 18:49 Right, let's… let me take a quick look.
There's some here, yeah, I saw you approved some stuff, so I'll have to, merge as well, but I won't go into it now. And this dependable PR is something I… Need to check, not sure why it failed. Yeah, also not for now, and… I see this is also still with the old 3.9 version, so that will be dropped anyways. Yeah, so a bit of checking for me to do. I do know that you have some of these draft PRs open, but, again, little bit of memory loss, but I seem to recall that A part of the effort you were doing would be solved by the transform processor anyway, right?
**Raphael Manke** 19:43 So I was working on injecting the account ID.
stuff, and I think I solved it by adding it to the wrapper scripts. That was…
**Warre Pessers** 19:58 Yeah, yeah.
**Raphael Manke** 19:59 Oh yeah, it's still open, the… with your cursor.
**Warre Pessers** 20:05 This may be something I still need to, prove, and actually, I did, apparently.
It's been a while.
**Raphael Manke** 20:12 Was there something open at the end?
**Warre Pessers** 20:20 There was some… change that deviated from how it was before. Yeah, basically just alignment, but, For me, that's not really blocking. I'm not sure what's here as well.
**Raphael Manke** 20:37 Oh yeah, he wanted to make that file name more variable.
**Warre Pessers** 20:41 Yeah.
**Raphael Manke** 20:42 to address that.
But I don't think someone will fiddle around with it, because no one will know it anyway.
**Warre Pessers** 20:49 Yeah, I think so too, but, I just put my, my like on here, because Max obviously has, some of the main… slash internal knowledge that I don't have, so, basically up to you. If you, feel like it's fine as is, I'm fine with merging as well.
**Raphael Manke** 21:09 I will get back to it, and I think it should be an easy change, yeah.
**Warre Pessers** 21:14 Alright, I'll see that when it rolls in then. Good, then I think there's nothing else from my side for today, so if there's no further questions or remarks, I think you can end the meeting here. I've got some action items that I'll take care of.
And then, we'll see each other again in two weeks.
**Raphael Manke** 21:35 Huh.
**Sidartha Gracias** 21:37 Thank you.
**Warre Pessers** 21:38 Thanks for, attending and for.
**Sidartha Gracias** 21:41 And then…
**Warre Pessers** 21:41 Also, nice to meet you, Siddhartha.
**Sidartha Gracias** 21:43 Yeah, nice to meet you.
**Warre Pessers** 21:44 We see you here, more often.
**Sidartha Gracias** 21:46 Meh.
Right, techniques, right?
**Warre Pessers** 21:49 Nice day.
Might.
