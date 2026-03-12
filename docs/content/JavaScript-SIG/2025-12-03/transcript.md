SIG: JavaScript SIG
Date: 2025-12-03
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/gAKtTQC9yRRfRfgbDbLOAjz_TWAczpo7IxhU7YkWIi-yucgu3Lk82P8S6CG56AmC.dk1St7W-jhQpUx5u
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:38 Nope.
**Caelin Bryant (Capital One/Discover)** 00:49 I'm just a fly on the wall today, so…
**Marc Pichler (Dynatrace)** 00:53 It's fine. Everybody's welcome.
I'm just waiting a bit for more people to join, but the agenda seems very empty today.
Let's wait a few more seconds, and then we can get started.
**Trent Mick** 02:46 I totally am late because I was… mucking around with markdown table formatting, so there you go.
**Marc Pichler (Dynatrace)** 02:56 It, it, seems to be the, the hot topic, for all of OpenTelemetry I've seen, in a few other repos also, Mark don't think this… Everybody'.
**Trent Mick** 03:12 It's new.
**Marc Pichler (Dynatrace)** 03:13 Interested in it, now that the table change has been released.
**Trent Mick** 03:17 the new VIE Max.
**Jamie Danielson** 03:21 Controversial.
**Trent Mick** 03:21 They're two sides, yeah, it's just… yeah.
chaos.
**Marc Pichler (Dynatrace)** 03:30 Right, welcome, everyone. Looks like we don't have any topics on the agenda for today, If you would like to discuss something, please feel free to just add your topic here, or… Just start talking, and then we can… Disgusted.
If not, then we might jump immediately into park triage, which is everybody's favorite part of the SEC meeting anyway.
Yeah, I guess, let's do that. Oh, hey.
**Jackson Weber** 04:18 Oh, I was just gonna bring up a quick note for review again. Sorry for sounding like a broken record, but I made the changes that you had discussed.
On the logger configurator, PR.
**Marc Pichler (Dynatrace)** 04:33 Yes, or have another look at this one.
Yeah, these are probably all sorted out, so I will, do another pass at this.
**Jackson Weber** 04:49 Awesome.
Thank you.
**Marc Pichler (Dynatrace)** 04:53 Thanks for, bringing it to my attention again.
Yes.
As always, if anybody else has time, please also feel free to have a look at the, PRs that are, open.
There, and no.
The more reviews we have, usually, we get, peers merged a bit quicker.
Alright.
This one here, is the first bug that we have on the list, I wanted to look into this one, but This seems to me that it's not really, Not really just related to what we are doing here, and it just happens during debugging, so… What I would put here is P4 and… I will look into this, Once I have some time. Or if anybody else wants to take a shot at this, it just seems to… Be something that, produces… panic in V8, and it might be… Worth bringing that up for, I don't know.
whatever… Project is appropriate to file this bug to. And there's already, like, a small… Reproducer here, that probably needs to be broken down into a few smaller chunks, so that it digestible for the folks that work on the upstream projects.
Error.
This one here, also… Did not have time to look into it. The person here is… Kind enough to take this over.
I'll just type up a quick comment here.
The issue here is that, they are using a custom… I think it's called, like, a metric producer.
And the data that they generate here, there's… Some type that was not correctly applied, or maybe something was missing that we expected there, and the task here is to double-check first If it's actually missing on our type, and if it is, then we need to add proper checks in the OTLP transformer package.
Or, if… it is there, then this is a warm fix, I would say, because we need to rely on the types being correct.
And we don't put extra checks everywhere.
Especially in, the packages that are considered as internal here.
So I will, just typed it up.
Type up, if the tabs are correct… Alright.
Where do I send a person here?
Alright.
I guess we can keep triage on, as a labor here.
Until the person, had a look at that, and then applied… applied the proper label as… Needed.
Alright, this one here is for instrumentation Postgres.
Burying the B operation names with spaces before or after the name.
Oh, looks like… Something might be wrong in the way that things are being generated. Let's just check real quick which version they're using. That's… 0.62… Does anybody know… Which version you're on right now?
**Jamie Danielson** 11:38 Six… This is 61.1 in the package JSON.
**Marc Pichler (Dynatrace)** 11:49 Thanks.
**Jamie Danielson** 11:52 Oh, auto instrumentation is known.
**Marc Pichler (Dynatrace)** 11:53 Yeah.
67… But it might be that this is already fixed. I seem to remember that there was something… That was very similar to that.
Let's just check if there's something in the changelog.
Looks like search does not work here.
Oops.
Instrumentation, Postgres… Change the… let's see here… And there's the updates… Looks like… Nothing really happened here that would fix that, so… Mmm, might be… Remembering the wrong thing here.
Anyway, this is P2, because, These shouldn't be there, and it's messing with, the telemetry that's being exported, and it's for instrumentation Postgres.
And I would assume that this would also be easy for people to pick up, because we just need to… Trim, whatever.
string we put in there, so I put it up for grabs on it.
In case anybody has time to look into it.
Right.
What's the door for contribute to?
Yes.
Gee.
Does anybody have any topics you would like to discuss in the meantime?
Not then. Let's move on to looking at pull requests.
I guess we can go either way, either go for our comp trip.
It seems like Contrip has more PRs open at this point in time, so let's go with Contrip first, and then… - Let's, look at the core, if there's more time.
I'm actually working on getting this one, sorted out now, started… authoring the PR for the SEMConf.
Repo to add this experimental, flag there.
Planning to open the PR today, still.
To make sure that's our, on the road there.
And then… The next one is, AWS Lambda.
Seems like this is… Waiting for a component owner review.
if I understand correctly, there was some confusion about, how… the messaging, semantic conventions, and the lambda… Semantic conventions diverge in the handling of, SQS… Was some alignment that needed to be made to make sure that this is all updated.
**Jamie Danielson** 16:42 Yeah, it seems like the open question is… On the spec side, not… This side, right?
**Marc Pichler (Dynatrace)** 16:50 Yeah, it seems that there's some confusion about what to do now.
There's, so… It says in here, instrumentation should provide utilities for creating Message processing spans.
But processing spans basically went away, in favor of, span links, so… This is quite outdated.
It would be interesting to see what other, Instrumentations are doing from other languages.
Because this likely affects everybody, to some extent. I would assume that they just updated to… The latest, But… Difficult to say.
I wonder if there's something on semantic conventions?
That would… Already tracked it.
There's, plunder spending inconsistency… I will actually comment here and just let… - Let me see… Or just, comment here that it looks like this PR has starred due to, Bonuses… I'll just link to the SamConf.
**Trent Mick** 19:22 Alright, I'm slowly catching up. This thing is proposing using the stuff in propagation utils.
I think there'd been a long discussion a while ago. I was pushing it to drop all of that stuff.
I can't remember the degree to which it's currently used. It does surprising things, like patching for each and map on Object and array.
were the object and arrays that you get back from these things to try to blom in processing spans, which had been in the spec for a while, but anyway, I don't think it's going to change your answer here, because I don't have the bandwidth to fully engage on this, but… I think, if I understand correctly, I… It would not support this kind of thing.
Yeah, anyway, sorry to distract.
**Marc Pichler (Dynatrace)** 20:08 Would you say it's, accurate to, state that… semantic conventions seem outdated for… Lambda?
Side of things.
**Trent Mick** 20:21 I'd have to look again, but yeah, that's my memory, like, the messaging spec had moved on, but Lambda didn't… I guess.
to say it one way, I'm not sure if this is accurate, but Lambda spec didn't keep up.
to those changes, or wasn't also updated for the same thoughts on messaging? It's kind of hard. I don't know what… Engagement there is on the messaging semantic conventions right now, so…
**Marc Pichler (Dynatrace)** 20:46 Yeah, I think it's, there's… there's not a lot of engagement right now.
But… I think it would be worth at least to, open, an issue on the CENCOMF rep repo to let, to have something to track any sort of update, and to get some clarification on what to do now.
Yum.
**Trent Mick** 21:10 Yeah, that's true. Yeah, that's fair.
**Marc Pichler (Dynatrace)** 21:13 So… I will put a comment here that it looks like it's a star due to inconsistencies.
Consistencies here… issue there to seek, right?
Oh, don't worry, so… Internet.
Then that's this one, and let's see, All that continues. There's instrumentation, dang chain.
I'm not sure if, Yeah, this is, probably… This probably should be a draft.
Because there's this PR here.
That adds the initial skeleton.
**Jamie Danielson** 22:35 Oh yeah, like, this one is, I think, to replace the other one.
**Marc Pichler (Dynatrace)** 22:41 Looks like this is already… Approved, but we're missing some… There's something wrong with the tests.
That's always a bit difficult to figure out what's actually wrong here.
It looks like there's some problem with NPM installing stuff.
And it seems to have been failing for a while now. I never got to test our versions because other tests failed.
This probably needs some in-depth, NPM troubleshooting, I guess it's kind of obvious that these are, This is what it needs, but I'll just pack it out anyway. Looks like… Some things… We're all over.
I wonder if this is the same thing that we were running into with, the NPM versions 11, Dot 6.1.
And 11.6.2.
Where… depending on which version you used, it might generate a package log JSON, or, like, in-store stuff.
Forget to install stuff that should be there.
**Jamie Danielson** 24:41 Yeah, like, when it skips the optional dependencies, if it…
**Marc Pichler (Dynatrace)** 24:45 Yeah.
**Jamie Danielson** 24:46 Can't find it, or whatever.
**Marc Pichler (Dynatrace)** 24:48 It might be that, This needs to be served in our, in our workflows that we pin everything to the latest NPM version there.
And possibly regenerate package log.
I'm not entirely sure if that's the solution, though.
I will assign this to me, Since I did look into these things before, I might have some context on… what might… be going wrong here?
But overall, this is approved, so it shouldn't take a lot to get this merged.
And then I guess this one will become more actionable.
This is Redis Cluster Instrumentation support. I did ping, Amia and the Seymour component on this.
But didn't get a response yet.
I guess we can keep this open for now, and then circle back to it.
At a later date. But, it's been sitting for… About, pretty much exactly 2 months now, so… I will try to reach out to… the component owners on Slack, and… see if Don't have time to look into that.
Alright… This is the one that we had looked at earlier.
There's browser navigation instrumentations.
There's a bunch of… Changes requested reviews, and the person asks for… pre-review.
So, I think this one is on track.
**Trent Mick** 27:30 And we have…
**Marc Pichler (Dynatrace)** 27:33 MCP SDK… Thank you, Hector, for reviewing.
these, both this one and the Langchain one, appreciated.
So, it looks like this one is also on track, and then… There's another AI-related one, which is the… Instrumentation, OpenAI… responses, API, PR… I remember this being quite large.
Looks like there was a bunch of discussion, and the last comments from today ago.
I guess we can leave that be for now, it doesn't seem to… Have any pending questions here?
Then we have, renovate bot, which we will skip.
This one is in draft, so we'll also skip that one.
Renovate bought again.
This is, baseline ESLint is also in draft.
I guess it would, like, tends to… Possibly ask what's going on here, what's, missing?
It looks like this one is… Was just opened to… be a demo for Otta Browser, but I wouldn't see anything wrong with adding this here as well, to make sure we don't… Introduce things that aren't supposed to be used. What do you think?
**Jamie Danielson** 30:25 Can you say that one more time?
**Marc Pichler (Dynatrace)** 30:28 It looks like this PR was only opened, as a demo for OTR browser, but, I'm wondering if we should try to get this added anyway, because it prevents us from using features that we shouldn't use in the browser packages, catches things before they… can merge to main in the lead step.
So I'm wondering if you… what do you think, should we… ask Jared to go ahead with this change.
On this repo as well.
**Jamie Danielson** 31:07 Yeah, I think we can probably at least ask the question, like, this seems like it would be a beneficial change Was it something you plan to move forward with?
**Marc Pichler (Dynatrace)** 31:19 Yeah, I guess there's just one thing failing here, which is, instrumentation for a feature that's not baseline available. So, we're just asking to, if he wants to go ahead to also, exclude that package from the checking.
And then, once that feature becomes baseline available, we can… Edit back.
Alright.
And I guess, and we can also leave that be. The, draft PRs are… Usually, it's usually good to figure out what the next steps for these are, because they keep lingering around sometimes. I have been guilty of that in the past, to just open a draft PR to show something, and then it's… It's sitting there for a while.
Alright.
Then let's move on to the next PR, which is… Propagating context using… this thing here… It looks like, component owners… I actually did not see this one, so I will… kingdom here.
It's been sitting for 2 weeks.
So… Yes, it's, fine to ping.
April after this time.
This one is, renovate configuration updates.
I guess we can, talk about this. I have some opinions about… how we should configure Renovate, on this repo, because it's, can be kind of painful to have, all the PRs always open for all the packages, and also can be painful to have everything summed up together.
what this PR here is proposing is that, to enable… the Docker pin digests, and… pinning GitHub Action Digests, which we actually do already over in the core repo, so I'm for that change.
And there's, config migration thing, I'm not sure if that is already enabled or not, I seem to think that this is already there.
pin-def dependencies, I don't know, not completely sold on this one.
It would automatically pin all the dev dependencies, which would also mean that we would pin, OpenTelemetry core repo dependencies, which would probably mess with our update script.
And… And there's this abandonment thing, which I don't really know what it… what it does.
I guess the question here would be, do we want to apply this, Best practices set up here, or do we just want to go ahead with, adding our own.
Updates to the rules that's here, so that, It's more tailored towards what we need.
Rather than just… Going all in on whatever the recommended setup is.
**Jamie Danielson** 36:28 I guess we would be more explicit if we put in the things that we want or don't want, especially if the upstream thing changes.
And maybe it's fine, maybe we want to get updated when it changes, but…
**Marc Pichler (Dynatrace)** 36:49 Yeah, I personally, I think, most of these changes, I find, I would be more, I would be more comfortable if we were to just go ahead and, apply these on a step-by-step basis, and I would also be more comfortable if it was, done by somebody who has to interact with RenovateBot more, Because an outside person coming in and changing the settings for something that Essentially, everybody in the approver groups, uses.
It's probably not the best way of going about this here.
in the end, we have to live with it, the way that it's set up, and it has also big impact on, like, how many PRs are open at any given time, which can take visibility away from, actual code changes.
Yep.
I will, assign this to myself, and… Will state here that it would probably be better if we just Go step by step and add one after the other.
I guess we have a pretty good idea of what we would like to see, in the config, and then we can change the config as we… As we see fit.
That's wonderful.
**Trent Mick** 38:31 cunning.
kind of agreeing with you, the Pindev dependencies, I agree, is the… when I'd have the biggest question.
**Marc Pichler (Dynatrace)** 38:43 Alright.
**Trent Mick** 38:44 That sounds good.
**Marc Pichler (Dynatrace)** 38:46 Things didn't ever, I'll do that, and write the summary here.
And this is also renovate JSON update.
What this essentially does is, it allows for more updates that… Don't need dependency dashboard approver.
For stuff like, images that we use in the… Testing the unit test.
workflow, and then also, probably for GitHub Actions.
they're probably configured right now that they don't get updated, but I suppose we can also do the same thing with more explicit config. I know that in the core repo, the GitHub Actions and images get updated without needing dashboard approval.
So I would likely… have a similar… opinion here.
that we want to specify that explicitly. Also, I think JS is not a manager.
It's, NPM needs to be written here.
**Trent Mick** 40:32 Or is it Node?
No.
**Marc Pichler (Dynatrace)** 40:35 Could also be… It's difficult. I'm not sure if that's, like, a valid string, but it might be, damn.
I guess I will also assign this one to myself.
And, I just moved some of the changes that I did to renovate JSON in the core repo to the contrary repo as well.
So that it, So that we have a similar setup in both places, and that should probably also reserve what the person is trying to do here with this.
With this ruler.
It does seem a bit odd to… Change to renovate config tool in… repos.
As, like, the first contribution.
**Trent Mick** 42:03 Cato.
What are they going for here?
**Marc Pichler (Dynatrace)** 42:06 I'm not exactly sure. And in the first one, they said that they just saw that Markdown lint was outdated.
And I was, saying here that I'm kind of fine with MarkdownLint being outdated, since it's not really security critical, or Mission critical with what we're trying to achieve here.
and… Previously, we used a more, a less restrictive renovate JSON that just kept creating a bunch of PRs.
I think this might have been even before Most of the regular contributors from today, we're here.
we just had, like, constant streams of renovate PRs that were failing and needed attention and stuff like that.
And I had… Approve us, reach out to me, thing that they were, getting kind of burned out by, having to look at renovate PRs all the time, because there's so many dependencies in this repo that I, turned on the dashboard approver for most updates.
To give people a chance to, like, if they feel up for it, go to the dependency dashboard and start approving things, and then merge in, renovate PRs.
As they have time. But having it… set up in a way that it just creates PRs over and over again, takes a lot of visibility away as well from actual bug fixes and stuff like that.
And since we don't ship most of our dependencies, anyway.
And they are def dependencies, it's, less critical to have these be up-to-date, I think.
I'm not sure where I was going with Link.
with this, but I'm also not sure exactly what…
**Trent Mick** 44:26 Do you ever go… Back and look at the dashboard?
With any kind of… to, like, click… basically… so, I may be misunderstanding, because I don't use Renovate, it works, I don't use it a whole lot, but basically, the current setting is that we're not going to get Renovate PRs to update A lot of things.
Is it most things?
Actually, I should read the renovate config. I haven't gone through it to get an understanding of what's actually being restricted then. But then, I guess, like, if we want to kind of stay with the latest, I understand we don't want to have the torrents of renovate PRs all the time, but… Should there be… kind of a regular cadence to go look at the dashboard and tackle some of them, or not? Or is that…
**Marc Pichler (Dynatrace)** 45:13 I think there should be some regular cadence of going over to it. I've been doing it, in between meetings and stuff like that, you know, when, when there's time, I usually… go in if I have, like, 10 or 15 minutes where I know I won't get a lot of stuff done anyway. I… Trigger these, and then come back later and try to merge these in.
**Trent Mick** 45:40 Yeah, because you're gonna have to get… leave the hour for CI to run on those PRs once they Right, so, yeah, okay.
**Marc Pichler (Dynatrace)** 45:47 But, yeah, I guess we could make some changes here to have them be updated more often. The issue is that, With the way instrumentations are written, they sometimes patch internals that might change in, in, Minor versions of the package.
So, it might not be… Might break stuff.
**Trent Mick** 46:15 Which is something that we kind of want to fix, but isn't a P1.
**Marc Pichler (Dynatrace)** 46:18 Yes.
**Trent Mick** 46:19 Right? So, like, the test-all version should be capturing Those kind of things.
**Marc Pichler (Dynatrace)** 46:23 Exactly, yeah. The tester version is, is, capturing this, but, if we have situations like, something doesn't compile, but passes tests.
Then we don't want to, divert resources away from trying to update whatever thing is failing for the compile step when it actually works in production.
And… Also, all of these changes, if we have them be bundled up into one big PR, there might be one package that's causing trouble.
And, then you need to go figure out which package that is. So you're essentially back to, like, going step by step through all of these dependencies anyway.
And that happens more often than not, at least.
Back in the day, when… This was set up to, bundle all of these together.
It would just update everything, and then you would have to go in step-by-step, install, Newer package versions until you came to that one package that was actually causing the trouble.
So, you were essentially doing renovates work anyway, which wasn't very efficient.
**Trent Mick** 47:53 Okay.
**Marc Pichler (Dynatrace)** 47:57 Yeah, I'm, open, though, to, better.
Ideas of how to do this.
There's just some, cavats that one runs into when having a repo with so many dev dependencies.
Oof.
like, things that… Oftentimes also do the same thing.
And then, packages get deduped and stuff like that, which, yeah.
Leaves everything in a bit of a wild state, usually.
But yeah, I think what I was trying to say here when I started talking was, there's easier ways to get MarkdownLint updated.
We can just, updated and, merged it in.
**Trent Mick** 49:04 I think we're totally fine to just say, no thank you. Close this one, yeah.
**Marc Pichler (Dynatrace)** 49:10 That would be my preference for this, yeah.
And then if anybody of the, approvers is interested in making a change.
to the way we do things, I would be probably more open to, To merging that change and seeing how it goes.
Alright.
And we can move on to the next one.
I guess, choose not this one, renovate.
But… This one here… Looks like Marlieu already did review this one.
Since addressed, I guess here, get back to it once.
She has time to do so.
And then we have… This one, which I thought I had approved already, but I didn't.
This is in response to, us having a P1 bug in the, OpenAI instrumentation, I think it was, which caused… Essentially, we had methods here that we thought were internal, but just had the underscore there, but not the private modifier, so the types ended up on the types that we published and caused people that didn't have OpenAI, installed to run into compile errors. So what this does is basically force us to… it.
access modifiers.
Two other things here.
I'll give this another look.
After this meeting, but, it should be fairly straightforward, and it's just applying the… things from the SLint drawer.
Yeah. So… Making things private that, were unintentionally public is, breaking change, so… .
**Jamie Danielson** 52:08 I think in this particular one, though, he specifically didn't add private to anything yet, and just focused on putting public on the ones that were public, is that right, or no?
**Marc Pichler (Dynatrace)** 52:19 Yeah, I think so.
**Jamie Danielson** 52:24 There is a couple, yeah.
**Marc Pichler (Dynatrace)** 52:27 Though I'm not sure if that is actually… Exported from the module here, so… There might be a few that we need to check here, but… Should be fairly mechanical, tool.
Check and see.
I'll give this a look, Hopefully tomorrow, so that we can get this merged.
And the rest are renovate PRs.
Looks like we're done for a con trip.
Should we go ahead, and do Core 2, or should we call it, call it a meeting, is that how you say it? No, I'm not sure.
**Jamie Danielson** 53:20 It's like, call it, call the end.
I think you say call it.
**Trent Mick** 53:25 I'll let a day.
**Marc Pichler (Dynatrace)** 53:27 Yeah. For me, at least.
**Jamie Danielson** 53:31 I think that's alright, we went through quite a bit there.
**Marc Pichler (Dynatrace)** 53:35 Morant?
There's no objections.
Then… Thank you, everybody, for joining.
See you next week.
**Jamie Danielson** 53:48 See you next weekend.
**Trent Mick** 53:48 Thanks.
**Hector Hernandez** 53:50 Thank you.
**Marc Pichler (Dynatrace)** 53:52 Bye.
