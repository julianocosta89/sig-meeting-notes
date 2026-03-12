SIG: Ruby SIG
Date: 2026-01-27
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/T3_Za8GDBoqEMeXsrZKXIW-iFbi0VPMlz6EcIUs-Th2ihYB83w_EM2p03bj0lQ1I.a1nkxdyJIK42yI_I
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 02:46 Hello, everyone.
**Hannah Ramadan** 02:50 Hey, Kayla. Hi, Daniel.
**Daniel Azuma** 02:53 Hello, everyone.
**Kayla Reopelle** 03:00 Let's see, I know we don't have an Ariel today, Can wait a little bit, see if anyone else joins us.
Okay, well, we can go ahead and get started, I think.
There we go.
Sean?
Alright, so for the spec sig today, I, wasn't able to attend.
So, we can take a peek at some of these. Doesn't look like there's too many points.
So, suggested string representation of complex attributes for non-OTLP protocols.
Specifically, the Prometheus Exporter, or maybe Zipkin?
We don't have a Prometheus exporter, so we wouldn't have to worry about that.
Mmm… Yeah, and I don't know if we're updating Zipkin. I remember… Jaeger we deprecated recently, but I don't know where we're at with that, so this one might not apply to us.
Hotel resource attributes… Getting refined… Just basically adding some error handling.
Principles… Don't remember if we support OTEL resource attributes, I think we do.
In the SDK.
And then this is about allowing multiple resources.
Oh, this must be some of the work, I wonder, that they've been doing on the entity team, trying to develop the concept of entities as something separate from resources.
In hotel.
But it's just at an OTEP phase, so if this is something… anyone would find useful, now's probably a pretty good time to get involved.
Max batch size for push metrics exporters.
This is still just at the issue phase, so there's… suggestions. Is this something that you've run into, Schwan, with, Wanting a max batch size at all.
**Xuan Cao** 06:52 Oh.
I can take a look. Sure.
**Kayla Reopelle** 06:59 Thanks, yeah, I'm curious if it's something that we might want.
And then… Something about time series, start time tracking, so another metrics-related one, it seems.
This one is a pull request.
But it's at the development phase, so… Yeah, I guess another metrics one, if you have time to take a look at, that would be helpful.
Yeah, anything else that people want to look at for the specsig today, before we go into our own agenda?
I have, sadly, had very, very little time to work on hotel, lately, and so I know I'm very far behind on reviews and things.
I don't realistically know if that's going to change before February 10th.
I continue to hope and try to, make time, but I know that it's limited, and I also know that we're pretty backed up, so… I'm going to do my best, but I don't think I can necessarily promise anything big in terms of progress right now.
Is there anything in Core or Contrib that people want to discuss today, in particular?
**Hannah Ramadan** 08:52 Nothing in particular. We could just look at, like, new things, if… Anything from the community came up?
**Daniel Azuma** 09:00 I can bring up a question, then. So this is a, conversation. Actually, I think I, Hannah and I talked about this, last, last week, but, Maybe you have some opinions, Kayla. We, we, so I've, I've had this, discussion with James, about, Some work that, they're doing to, Ugh… If we tighten, the way that our… GitHub Action workflows are being, tested. So… Let me see if I can find a good example of the pull requests.
Well, okay, the one that's, they were looking at was… There's my, true.
Oh.
Paste it in here.
I'm gonna taste what's going on, like… I can't paste into this Google Doc, why can't I paste into…
**Kayla Reopelle** 10:19 Oh, that's strange.
Open.
**Daniel Azuma** 10:22 Put it in the Zoom chat?
**Kayla Reopelle** 10:24 And I can add it there.
**Daniel Azuma** 10:26 I just edited the Google Doc, I don't know why I couldn't, It's in there, but, it's, it's this… pull request, So the idea is that… We have, 6 different workflows that are related to the release process. we had an issue, a few weeks ago where, renovates.
edited, these, these pull requests to… or at least, these, these workflows to update the Ruby version, that's installed.
**Kayla Reopelle** 11:08 without updating Setup Ruby. And so it's, it's… so those started failing.
**Daniel Azuma** 11:15 And that got, you know, that got rolled back, but, James said, hey, we need to, have some way to test these things, or have some kind of CI on these things so that, you know, we can detect when these things will fail when, because of a change like that. So, So… It opens a… this pull request, which goes through and, adds a trigger to each of the release workflows that runs it during the CI process.
Now, of course, you cannot run a release during CI, so… so for each of the workflows, there's… there's two parts. There's, adding a trigger, specific to CI, and that could be… that was easy in a few cases and kind of complicated in other cases, like this first one.
And then there is logic, In the workflow to disable part of the workflow that actually executes a bunch of release-related stuff.
So, basically, what it does… the upshot is it's, whenever one of these, workflows gets modified, it runs the workflow, but only does the installs. Not actually do the final run, run the release script thing.
So, so, you know, we went through a bunch of, things, and I think this will work as is.
I'm un… I'm uncomfortable with, this change because it makes these, workflows, more complicated. I, I, you know, I have to maintain these, and, you know, now I have to reason about, okay, what's… is this workflow being run in CI versus the real thing, and, you know, how do I… if I need to change any of the triggers, now I have to think about that, and…
**Kayla Reopelle** 13:17 I kind of don't want to do that.
**Daniel Azuma** 13:19 So… I put together an alternative.
**Kayla Reopelle** 13:26 Which is number 1959.
**Daniel Azuma** 13:31 And this… what this is, is basically it creates a new workflow that replicates all the installs, it runs only in CI, replicates the installs, and basically, that's it.
And then it does kind of a token, kind of dry run, thing at the end, just to make sure that, you know, the CLI can start up, but doesn't actually try to do any release stuff.
So it doesn't touch any of the existing workflows, it just does this. The idea is that if Renovate runs, and wants to update the Ruby version, it'll update all the workflows, including this one. And this one can be used as kind of a canary to say, hey, if something is gonna fail, this one will fail.
so I put that, that out there as an alternative. James and I, disagree on which, which, which approach we should use. and so there's some discussion in these, these, these pull requests. I, James isn't here, obviously. I can try to, I can try to express what, what their argument is. So, my argument is, obviously, I, I would rather not touch the existing workflows, not make them more complicated, and just do this. And this will catch all of the, the, the, you know, it'll catch those renovate cases.
james' argument, as I understand it, is that Yes, this will cache and renovate cases, but it still does not test the actual workflows.
And so there are… so there are potentially other cases, like, you know, oh, I go through and I need to make a manual change to one of the workflows. It's not going to catch that, because, you know, I haven't touched this canary.
So… I think those are kind of the trade-off, the basic trade-offs.
One could think… one could even think of a third approach, which is, well, if we're concerned about actually running the work… the testing the real workflows.
why don't we actually do a CI that actually does a full dry run release? So, you know, set up some workflow that actually, It, it, it's, you know, it, it, it's programmatic, programmatically runs, the release request, workflow, creates a real, pull request, release pull request, merges it and puts it in some kind of a dry run state, so it doesn't actually try to do anything, but it actually goes through the entire thing and makes sure that the whole process works. So, one could even consider doing that. That would be more work.
But I think it's feasible to do. So there are these different, approaches that we could… Beautiful.
Use for this, for this problem.
I'm curious as to what's, if people have opinions, about this.
**Kayla Reopelle** 17:07 No.
Thanks, yeah, thanks for being involved in this discussion and bringing it here and kind of catching us up on where it's at.
I think I'll probably need more time to, like, read the PRs and kind of digest them before I have a stronger opinion, but I mean, as far as, like, where my just general values for the project lie in terms of a solution, like, something that makes you know, maintaining the project easier. I guess right now, the question is, like, what's easier for different people?
And then I think… Yeah, trying to protect our release process so that we don't need to… Like, if we need to do some sort of emergency release, hopefully the CI isn't the thing that stops us.
I know in the past, too, we've also had issues, Or I think, you know, this is an ongoing problem of trying to allow the CI to run quickly and, you know, maybe only run things that are relevant to whatever is in the PR.
I'm not sure if maybe that could, in some ways, be used here, too.
But I do worry about, like, running all of the release hooks every time we open any PR, even if they have been disabled in some way.
**Daniel Azuma** 18:35 Yeah, I think the idea would be that, any, any CI here would only run, if, some of these, if one of these workflow files, YAML files, were modified in the PR. And I think, James's, James' changes are tailored to do that.
So, that's… worried about that.
**Kayla Reopelle** 19:02 I guess maybe this isn't ideal either. As you were describing the options, too, I was also wondering about workflow dispatch, and if that becomes something that people run when they're evaluating the Renovate PRs?
For any time that, like, an issue or a certain file is changed, but that's a manual step, and so we probably want to avoid too many manual steps.
I'm reviewing things.
Yeah, those are just my hot takes right now, but I'll, you know, think more about it. What do other people think?
**Hannah Ramadan** 19:49 I guess the point about, like, maintainability is probably, like, a big one for me. I feel like we're all kind of struggling for time, so if something seems, like, too complex or, like.
overwhelming to… to go maintain. I think that would be… Something, like, probably a larger consideration.
I feel like I had one other thought, but it's escaping me.
**Kayla Reopelle** 20:18 It comes back, let us know.
**Hannah Ramadan** 20:19 Yeah.
**Kayla Reopelle** 20:22 I'll add this to the agenda as well.
**Daniel Azuma** 20:31 Anyway, so that's… That's an open discussion here.
I've been doing a bunch of work on the release, process. There were, a few weeks ago, there were some feature requests, such as being able to have the release process update existing release requests, When, you know, new commits come in, and, I've actually now, are, I've… I've basically implemented that, and I've been testing it over the past few days, so I have a… I have one more pull request in to actually enable that in our configs, so if we want that, so we can actually… start having it now. And there were a few more, feature requests that I'm still working on, so…
**Kayla Reopelle** 21:24 Nice. Thanks for working on those. It's exciting to hear about progress there.
Right, let's hop into Core… So, we've got some Renovate PRs to… review. I saw this PR, I just started reading it this morning.
It looks like Arielle has some feedback on it.
Is there anything about it that you'd want to share live?
**Xuan Cao** 22:08 No. This, It's actually tied to another PR, so this will be a breaking change.
Boom.
Yeah, well, just change the, from the SEGI to the standard libraries. Like, other languages, they… they use their standard libraries.
**Kayla Reopelle** 22:30 To the encoded decode.
Okay, nice.
Thanks Anything else?
On here, it looks like we have a lot of… Tech debt, and kind of… System upgrade-related things.
Is this one of the PRs you were talking about, Daniel?
support.
**Daniel Azuma** 22:58 This is… oh, yeah, this, this was, one that I opened a few weeks ago. They're, This we probably need to get in, because we did this already for Contrib, but haven't done it for Core, I think, because of CI issues. But this was switching the release system from the old legacy system that, that I had put together years ago to the new one that I'm actually maintaining now.
**Kayla Reopelle** 23:26 Okay.
**Daniel Azuma** 23:26 So…
**Kayla Reopelle** 23:27 Nice. Sounds good.
**Daniel Azuma** 23:32 But, you know, I think there was… there… there were just a bunch of… there were some CI issues that I think people were, Blocked on, and some of these were blocked on, so maybe since… is… Those were resolved… maybe… maybe that flaky test, 2026, that you had.
**Kayla Reopelle** 23:56 Yeah, this one, I think I was waiting for things to… Oh yeah, I can put a link to the issue in the comment for the test.
**Daniel Azuma** 24:09 But it seemed like that was one of the, one of the CI issues, so if we can get that skipped, then maybe… Yeah.
maybe that'll solve a bunch of these other failing, failing CI issues. Nice. Okay, I'll try to.
**Kayla Reopelle** 24:24 Take care of that one.
I guess we can put some of these in here.
I'm missing your toys PR. There it is.
Okay, any issues?
Oh, we had one open today.
Support for the enabled setting.
That would be… Good to work on.
There's a slightly different way to do this in… an hotel spec'd way that we haven't.
supported yet, and so I can… Try to add that as a comment.
Anything else on here?
The environment variable propagation spec.
Hmm, interesting. Okay.
Has anyone looked at this before, or used it for other… Languages.
**Daniel Azuma** 26:19 Status is alpha.
That's…
**Kayla Reopelle** 26:24 Yeah, we can… we can take a look at, let's see, maybe it will be in the alpha. There's usually a PR somewhere in the spec.
That's not what we want. Somewhere in the specification repository, there should be a PR that has, like, a list of other languages that have implemented it so far, and kind of more about the status. So that might be the next step on this one, is to figure out, like.
Where it's at with the other languages, and if it seems like it'll be moved forward.
Oh, and here is said issue.
Interesting. Okay. So it seems like they opened… This for a lot of languages.
Maybe only Go has picked it up so far?
Okay.
Well, it's nice to see a feature request added related to a feature that was changed in the spec, or is changing in the spec, that makes it a lot easier to track.
Right, and contrib… what do we have here?
Is this what you were referring to with, Some of the changes in toys with the new.
**Daniel Azuma** 28:02 Yes, this, is… Which one was this? This isn't trip, yes. This was, just modifying the configs to enable some of the… the, changes. This actually had one question in it.
So, currently, the release process requires that all GitHub checks have succeeded before it will allow you to request a pull request, or request a release. Also, when the release starts actually running, it will wait for the GitHub checks on the release pull request merge commit, the checks will run, and it will wait for any checks… that are running to succeed before it actually proceeds with the release.
I… have gotten lukewarm about that, that functionality over time, and I'm inclined to disable that, now, and just allow a release to… to run, regardless of, you know, whether checks are still running or not.
So this… Pull requests, does… modify the, it currently modifies the configs to disable that… that GitHub check, requirement, but I also wanted to put that up for discussion. Do people… would people rather to… rather retain that, or.
**Kayla Reopelle** 29:44 Hmm.
**Daniel Azuma** 29:45 you know, this lab releases. I'm… I'm… I guess I'm… I'm concerned about… number one, it's a little bit annoying sometimes. When I've used… I've been using the system on my… on… on other, other repos in this… if… especially if the CI runs, or takes a while to run, it gets annoying to have to wait.
And I'm also concerned about if CI was ever flaky and we need to do an emergency release, then, you know.
what's… we might get stuck. So, those are…
**Kayla Reopelle** 30:18 Yeah, I'm trying to think of… I feel like there's been a case where the CI failing has helped on the release, but it's been a while. I think it was kind of… In a situation where we had… Maybe, like, multiple dependencies, Oh, it's instrumentation all. So instrumentation all in the past has generally failed if it, you know, maybe needs a release, or we're missing, some other gem that needs to be released, and I think that's a required… workflow, so I guess if we label a workflow as required, is that one ignored as well? Or…
**Daniel Azuma** 30:58 Should I have to… I… I think…
**Kayla Reopelle** 31:05 Yeah.
**Daniel Azuma** 31:06 It's… Yeah, I don't remember. I don't think, required versus not required, factors into what it's waiting for. Okay. But I'd have to double check that.
**Kayla Reopelle** 31:19 Okay.
Yeah, I think that's the only one I would be… curious about, or, like, want to potentially save, and that's one quick, brief… CI run that only checks, like, the… that things can be installed in a valid way.
But if that's too complicated to have that type of an exception, I understand.
**Daniel Azuma** 31:48 Okay, yeah, I can possibly… so… So, to be clear, if there was… if there was a way to have only the… only the required checks, be gating, for, for release, versus all checks being gating.
**Kayla Reopelle** 32:06 Though I also feel like I've… been in a situation where I've been able to merge a release PR without all the checks completing.
With only the required checks completing.
**Daniel Azuma** 32:18 You can definitely merge a PR, yeah, especially if you're an admin and you can force merge with, you know, without the checks succeeding or completing or whatever, then that's separate. It's, it's, the, the release scripts themselves, so the, the, the script that, that opens a PR, will currently look at the branch that you're, you know, you're opening the PR against, and see is the… have the checks finished and passed on the latest commit on that branch. If not, it'll refuse to open the PR, for example. So, you know, things like that.
**Kayla Reopelle** 33:01 Got it.
Interesting.
Okay. Well, yeah, I'll think about this a little more. Thanks, thanks for opening it.
Okay, what do we have one here?
Depend upon… Okay, that seems… Like, it could be helpful, hopefully.
**Daniel Azuma** 33:55 I was mentioning something about… Looking for someone on AWS to help with this.
**Kayla Reopelle** 34:01 Yeah, yep, that's what I would… I've thought to. Okay, I know some of these folks are on Slack, so maybe the next step is to… Ping them in the CNCF Slack to see if we can get help.
Okay… Oh, there's a logger issue.
Take a look at that one, too. Is there anything else on here that That people see right now that they want to jump into?
I know there's a lot that's open.
Can peek at the issues, too.
Yeah.
I feel like it's a lot, a lot to take in, so, if no one has anything in particular that they want to take a look at… Then maybe… Maybe we wrap things up here?
I have to leave in about 5 minutes anyway.
So…
**Daniel Azuma** 35:57 Yeah, maybe we should wrap up. I feel like, Yeah, there's a lot going on, and I think it's probably best to try to do some… Reviewing offline first, and then… Bring actual questions, specific questions here, so…
**Kayla Reopelle** 36:16 Yeah, yeah, I agree.
Well, I appreciate everyone's, like, patience with my kind of changing availability right now.
I'm gonna do my best to try to catch up on these things, and we'll hopefully have feedback and discussion points next week instead of just, An overwhelmed, overstimulated look at the lists.
So…
**Daniel Azuma** 36:40 Yeah, no worries. Thanks. Thanks for, thanks for leading us, Keira.
**Kayla Reopelle** 36:43 Yeah, no problem.
See you guys next week. Take care.
**Daniel Azuma** 36:48 Thank you.
