SIG: JavaScript SIG
Date: 2025-07-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

MG Marylia Gutierrez 00:00:35 Hello!
Trent Mick 00:00:40 Hello!
Marc Pichler (Dynatrace) 00:00:43 Blue.
MG Marylia Gutierrez 00:00:45 Happy Canada day, Trent.
Trent Mick 00:00:48 Thanks.
We can't.
Marc Pichler (Dynatrace) 00:00:51 Okay.
Trent Mick 00:00:51 It was yesterday, you know.
Marc Pichler (Dynatrace) 00:01:07 Is it usually every 1st of July? Or how does.
MG Marylia Gutierrez 00:01:12 Central life.
Marc Pichler (Dynatrace) 00:01:13 Yeah. Okay, yes, it's good to remember. Then.
Daniel Dyla (Dynatrace) 00:01:20 Canada day 1st of July.
MG Marylia Gutierrez 00:01:22 Yeah.
Trent Mick 00:01:26 That's right. There's something less important 3 days later, but I don't remember what it is.
MG Marylia Gutierrez 00:01:31 Who's awesome.
I celebrated doing like a Brazilian barbecue. So it's like.
Daniel Dyla (Dynatrace) 00:01:41 All the Canadians have been around this week.
Marc Pichler (Dynatrace) 00:02:20 I guess we can get started. I'm not sure who put the 1st topic here.
Daniel Dyla (Dynatrace) 00:02:25 I put this here during the triage last week.
We copied it to this week because we didn't have time to talk about it.
This is yeah. So Aaron mentioned.
you know. We asked him to look at A. Pr. He said, sorry I haven't had time, whatever. I'm looking to get rid of this and just expose the one that Google hosts
that Google maintains the one that they host theoretically
and ours is less maintained because of it. I guess
he doesn't want to maintain both. He only wants to maintain one that makes sense. The question is, how do we feel about hosting
modules in our repository that are just
re-exporting modules. We don't have control over.
There are a couple of big advantages from
Google standpoint. I'm just using Google here because they're
it's Aaron. And he's at Google. But this could apply to anyone.
One is discoverability. We do technically have the registry. That's like the party line answer. But
when was the last time you actually looked at the registry.
2 is inclusion in auto installation. Meta packages.
That's probably the bigger of the 2.
Because we could always just
add a readme or whatever that says, Hey, we don't have this anymore. Go look over here in our repository and help them with discoverability.
the auto installation stuff. I don't know that we want to include stuff we don't control in the auto installation, including if we're just like
proxying, we're just proxying their module. That's not really any better or maybe we don't care.
I think the true answer for this would be to say
like, if if we had a better mechanism for auto detecting installed plugins like, if we could just tell users, if you install the Gu, the Google version of this, it will be discovered by our SDK,
then a lot of that problem goes away.
You still have some discoverability, but it is what it is.
I'm leaning towards saying, bye, no to this
like not not saying no, because he's not asking for that.
I'm I'm leaning towards towards saying, we're not going to proxy, some external module
that we don't have control over.
and we're not going to include external modules in our auto installation scripts. If you want to host externally and have an auto installation script, you should, you know, have your own auto installation script that includes the things that you're comfortable, including.
Marc Pichler (Dynatrace) 00:05:52 Yeah, it's
ideally. We would have some way also to make
make it known somehow that there is a resource detector somehow, so that we could
like auto, load it as you said.
I'm just not sure exactly how we would go about that
Daniel Dyla (Dynatrace) 00:06:22 Yeah, I don't know either. I mean, I know that like
there is precedent for this type of thing.
If you look at like eslint plugins.
They work somehow.
Obviously they have a config file
which tells them where to look for stuff.
Marc Pichler (Dynatrace) 00:06:51 Hey!
Trent Mick 00:06:52 I mean, we could eventually grow an extensions mechanism that, like the Hotel Java.
I just have a extension thing. But that's gonna be explicit config required by users.
Daniel Dyla (Dynatrace) 00:07:04 Explicit config is okay in node. I think everybody's moving to. We're gonna have to implement file config. Anyways.
Trent Mick 00:07:11 Yeah, yeah.
Daniel Dyla (Dynatrace) 00:07:12 And explicit config is fine.
It's a little bit
like. It's difficult to work in an Esm context when you're loading. Are you trying to dynamically load
plugins from a config?
But
if we say, you know, if you again taking es linked as an example, the config can be a Json file. It can also just be a script.
And maybe we say, if you're an Esm, you have to. You know your config file has to be a script that does the loading.
I don't know.
I think we're gonna have to solve that, anyway. And then in Browser
I think it's almost not a concern, because in the browser you have to do everything manually, anyways.
Marc Pichler (Dynatrace) 00:08:14 Yes, and it would probably also be fine if it was different to what we do on, not js.
Daniel Dyla (Dynatrace) 00:08:20 Dynamic loading doesn't work like webpack bundle. It has to know where to find Plugins. Anyways, it needs to be referenced from the code.
Marc Pichler (Dynatrace) 00:08:29 And
it's unfortunately not a quick answer for this. Pr that we need to come up with something like that. But I have, I think, talked about this in the past before. And there's a thing on the focus topics issue where it says, some form of dynamic loading for
instrumentations and resource detectors would be a part of that as well.
Daniel Dyla (Dynatrace) 00:09:01 Yeah, I think the file config includes.
like a, you know, external module loading
the concept like it already has, load these instrumentations, or whatever and pass them these configs. We're gonna have to figure it out for that, anyways.
So I think that's the long term answer
for the short term. This is a module. The Gcp detector is in our contrib. It needs to be reviewed and merged, and we should set. You know
it's already implemented there. Maybe we can ask him like, Hey, can we mark this, as you know?
If if you don't want to maintain it in both places, then don't. Should we mark this as deprecated, and remove it from our repo.
Marc Pichler (Dynatrace) 00:10:02 Yes, I think that's also what we suggested with most packages before. That went this route. There are, I think one of them was. It wasn't exactly that. It was
the browser, plugin think
where somebody else has taken over the work and extended it quite a bit, and the one that we had was unmaintained. So we also suggested that we would link to the repository of the the new one, and just deprecate ours.
Daniel Dyla (Dynatrace) 00:10:36 Yeah, the auto installation stuff is frustrating, I I guess you know, probably for for someone like Aaron to say, like, we're kicking this out, and we don't have a way to auto. Load it, for now
it
Marc Pichler (Dynatrace) 00:10:54 Wondering if oh, sorry! Go ahead.
Daniel Dyla (Dynatrace) 00:10:58 I was just gonna continue the thought of like we we can't continue to maintain, or, you know, try to host and maintain a million different packages with. We have limited people and limited people working on it. And just, it's proven not to be
very scalable. We're trying to distribute as much as possible, and I think pushing people to host in their own repos.
You know, if if you create an angular plugin.
you don't go to the angular repo, and try to add it to their.
Trent Mick 00:11:30 Repo.
Daniel Dyla (Dynatrace) 00:11:31 Let's not the way that any open source projects really work.
We did because we depended on those plugins to like survive in the beginning.
But now we kind of you know it sounds harsh, but don't need them as much anymore like
the ecosystem will continue to exist, and we should try to push things out of our repos like we don't want to maintain every plugin. We probably do want to maintain a set of like really core important ones like Http. And stuff like that.
But we don't need to be maintaining a plugin for every database under the sun.
Marc Pichler (Dynatrace) 00:12:18 I agree.
Oh, next step for this would be to just see if
not doing what suggested. Here is an option for them.
And think about some way of dynamically loading things.
Daniel Dyla (Dynatrace) 00:12:44 Yeah, I mean, this is an old Pr, I think we it came up in the triage. It's not that old, but letting this Pr die and potentially saying, You know, maybe maybe comment. And on on it and say, Hey, we didn't realize you're hosting a separate one. Should we just remove this one from the repo.
and then he will probably come back and say.
Trent Mick 00:13:06 I don't like that for these reasons, and we'll have to have the same conversation we just had.
Daniel Dyla (Dynatrace) 00:13:13 But yeah, he's not here.
I guess I could reach out to him in slack as well. He used to be pretty responsive on slack, he might still be.
Marc Pichler (Dynatrace) 00:13:23 Yeah, I think that would be a good
good way forward, for now.
we can load some ideas about how we would go about the auto loading stuff.
I guess issues are always welcome with that prototypes. If anybody has any
also, as a basis of discussion, it can help to have some sort of prototype that we can
play around with and test things out.
Trent Mick 00:13:58 For the I don't know if this is a fair data point. I haven't really followed this Pr closely. But
the Google one that where they say the 3rd party, one where they say they've implemented this already is still using
version one of the SDK, so it's currently not an option for someone using the latest stuff.
And I mean, yeah.
Daniel Dyla (Dynatrace) 00:14:25 Yeah, we're we're in a little bit of a bind. Because while we depend on this stuff less than we used to, we do still need like. I don't think we've grown to the point where we can just be like, like.
update your stuff. We're not, gonna you know. We have to maintain some balance.
Trent Mick 00:14:43 I mean, yeah, I don't know.
Marc Pichler (Dynatrace) 00:14:49 And we.
Trent Mick 00:14:49 I was. Gonna say, cloud resource detectors, for the Big 3 providers are kind of arguably
in the core set of ones, but then they have a zillion services. And this is not about the core stuff. It's about
the long tail of services on each of those ones which we don't need to sign up for maintaining.
Daniel Dyla (Dynatrace) 00:15:10 They? They may be core important. Yes, but they're such big targets.
Trent Mick 00:15:22 I don't know. I guess. Yeah, on balance, I'd be inclined to just let this one through if it looks like it compares favorably to the upstream Google maintain one because Google maintain one's not an option right now for people, but.
Daniel Dyla (Dynatrace) 00:15:33 Yeah, it's just.
Trent Mick 00:15:34 Kick to Kendall.
Daniel Dyla (Dynatrace) 00:15:34 Arguing that it was a bad feature, or that we shouldn't allow it, or anything like that. We were just asking Aaron to review it. And he said, You know.
basically, I don't have time, because I'm maintaining my other plugin.
If we have time to review it and think it's valuable, then great. We can merge this through.
but I think long term we don't want to host both.
I'll I'll reach out to him on slack it's possible. He's not
aware of the fact that his plugin doesn't work with the latest stuff.
Marc Pichler (Dynatrace) 00:16:25 Yeah, I think in general, what I take away from that discussion and from the question that we that that was stated here in the beginning was
we would like to not have the actual resource detectors for everything in the contract repo, and we wanna move on to something that's more scalable for
more maintainable as well for us.
And we still have to figure out how to do that.
Daniel Dyla (Dynatrace) 00:16:58 Yeah.
Marc Pichler (Dynatrace) 00:16:59 I mean it's not hurting anything to have it there for now.
Daniel Dyla (Dynatrace) 00:17:02 As long as people are aware that reviews might be slow.
Marc Pichler (Dynatrace) 00:17:07 Yeah, agree.
Daniel Dyla (Dynatrace) 00:17:11 Okay.
Marc Pichler (Dynatrace) 00:17:14 Alright, thank you.
Does anybody have anything to add to this topic?
If not, then we can move on to the next one. Trent.
Trent Mick 00:17:33 Like a link to the old Pr machine to find a new one
status?
Or is this my new Pr?
I've lost it.
Marc Pichler (Dynatrace) 00:17:55 This is the older one. The new one is here.
Trent Mick 00:18:02 One.
Marc Pichler (Dynatrace) 00:18:03 Put the link.
Trent Mick 00:18:04 Oh, I'm on page one that's starting.
Some people.
Marc Pichler (Dynatrace) 00:18:07 It's okay.
Trent Mick 00:18:08 Thanks.
Oh, yes, there's a heads up. And then I guess also a question about timing.
There was an old Pr which most people will know what I'm talking about to rename
most of the packages in the contribut repo to a regular scheme, instead of having them all divided into separate little namespaces. Generally, I've got the sense that there's agreement from everyone to go ahead and do this.
but there will be an impact on the currently open Prs, because, I don't have a good sense of how difficult the
dealing with the merge conflict will be. So if this goes in. Well, I'm hoping it'll be easy, because it's gonna be. Get Renames for everything, or for a lot of stuff with some like small changes inside files to deal with the the move directories.
So yeah, it's a heads up for people.
There are a few prs, I'm hoping to get in 1.st One is the instrumentation redis
consolidation, so that we don't have a rename, and then just immediately get rid of one of the old ones. So
that's 2915 yeah. The 3rd one down there. Second, 3, rd one down. Yeah.
But yeah, also heads up. And so then the question about timing for people here. Does it seem reasonable to do this early next week?
I don't wanna do it this week, because it's getting towards the end of the week already.
Daniel Dyla (Dynatrace) 00:19:42 Seems fine to me.
Trent Mick 00:19:43 Cool. Okay.
Marc Pichler (Dynatrace) 00:19:45 Yes.
Trent Mick 00:19:48 I'll go for that. Then.
Marc Pichler (Dynatrace) 00:19:51 Alright. Sounds good.
Does anybody have any questions about this rename plan?
Not then. Yeah.
I guess we can move on from Rhode Island.
Raphaël Thériault 00:20:18 Yeah, this is the one I brought up like 2 weeks ago, with, mentions of reworking the tests. I still need to open an issue describing, like what I ended up doing. But
long story short, it's really not easy to change the test to use another typescript runner.
and I managed to just fix the one broken test from that one so.
Marc Pichler (Dynatrace) 00:20:41 Nice.
Raphaël Thériault 00:20:41 Yeah, if Mark, you have some time to give it in a second shot at reviewing, I would appreciate that.
Marc Pichler (Dynatrace) 00:20:47 I will take that onto my to do list, and then I will have a look.
Yeah, you could make it work without having to change a lot of stuff. Because
migrating the tests.
Yeah, I had started a little bit with that before, and then
I I didn't spend a lot of time on it, but it seemed like a large task.
Oh.
alright. I will have a look at that. Pr, if anybody else wants to have a look, I would also appreciate
reviews from other people as well.
Yeah.
does anybody have any questions for Rafael immediately?
But I guess we can move on to back triage. If anybody else has any topics they would like to discuss. Please feel free to
add the topics to the list here, and let me know that you've added the topic, and then I can get back to the agenda, and we will discuss your topic there.
Alright. 1st one here different minimum language feature targets
mentioned and read me for Process port. Oh, yes, I had looked at that Pr before, which
wasn't this one but this one here?
Things like, there's a problem
of the Cla not being signed yet. So we'll head on over to this Pr after.
Oh, after this meeting, and write a comment that they need to sign it.
Yeah. So this is a documentation pack, which let's see, p. 4,
and it seems that they are working on it, so I will assign them
alright. Moving on
so maybe 6 dns. Failure
tries to includes the
the brackets, the square bracket stairs. It tries to do a dns lookup.
This is p. 2, because it
fails the request, and that means that the data does not arrive where it should go
and it is in the export of pace calling.
Yes, it should be fairly simple. Fix, I think.
Just need to make sure that we drop the square brackets there.
Think this square bracket is not a loud character, anyway, so
so it'd be fine to just check if it if it's there on both sides, and then
drop it alright. That's it for
repo, and then we can move on to contribute
where the 1st one is about Mysq. 2 instrumentation
that seems oddly familiar. I think we've
had that a few times already, but should be already fixed.
Daniel Dyla (Dynatrace) 00:25:16 It's possible that this is a duplicate.
Cause you're right. It does sound really familiar.
Marc Pichler (Dynatrace) 00:25:36 What is the current version of that? Actually,
okay, let's go to 0 dot 48.
This recent pr,
Trent Mick 00:26:23 I only linked that because it suggests that there is promises. Api.
Marc Pichler (Dynatrace) 00:26:27 Okay?
And then there are also tests for it. I assume so.
Yes.
I guess I can ask on the issue if
if they are certain that this is the version that they are using.
Daniel Dyla (Dynatrace) 00:27:24 Yeah, I mean, maybe ask for a like a runnable reproduction.
Marc Pichler (Dynatrace) 00:27:31 Yeah.
Daniel Dyla (Dynatrace) 00:27:35 They do show like the.
Marc Pichler (Dynatrace) 00:27:37 It's yeah. It says the version here. Actually.
I will mark this as is it cool
doesn't seem to work there.
I don't think there's anything that we can figure out on this call right now. But it's prioritized. So
let's move on to the next one.
If we don't hear. Back week this issue will be closed
all right.
That was it for country pack triage, and then we can move on to old Prs.
this one, I guess we haven't had any
activity on. Jamie is out for traveling, so only
we'll wait until Jamie is back for this one.
David Luna Bistuer 00:29:54 Mine's as one.
It's it is mine, but I prefer to, if Trend is able to merge next week the name of the packages.
so then I can rebase on December with the new organization.
Marc Pichler (Dynatrace) 00:30:11 You can skip.
David Luna Bistuer 00:30:13 Already.
Marc Pichler (Dynatrace) 00:30:14 All right. I will skip this one, and I will also skip that one because we already talked about this
Then the next one is this Pr into component owners.
seems seem seems to have updated the Pr
2 days ago and pinged them again.
So yeah, let's see if they
find some time to review this.
Call me.
Trent Mick 00:30:56 Let's see.
Marc Pichler (Dynatrace) 00:30:57 This one here.
Sorry about pending for
We're also seek picking off.
figuring out what the requirements are, and then
this will become a lot more actionable.
I'm also not sure if there's anything we can do with this right now.
That's kind of
difficult to figure out what we want to do with all of these things that are more or less pending specification.
which definitely would be the case for all the oh, wrong things.
or most of them, at least where it's kind of.
There's a lot of stuff that's trying to be added. That's tracing, based. And a lot of existing packages that we have that's tracing based. But it's supposed to
end up being events.
So I'm kind of lost on what I'm
what our what our plan is to deal with these.
We're just gonna keep them open and
wait for progress to happen, or if we should just march the Prs.
Or try to get them merged and then deal with updating them too different state later.
I'm not sure. Does anybody have any opinion on that. Maybe.
David Luna Bistuer 00:33:12 Yeah. Well, my, my opinion is everything that's related to Browser, or will run.
It's seems to be on. Hold
this Thursday. So tomorrow we want to start the 1st
person meeting. So we did that, some some because they can
had some discussions asynchronously. But tomorrow we're gonna start with the browser. At least, we're going to start the 1st part of the of this phase, one which is 1st review of the Apis, and and so on. So I guess
we suspect that this Prs would be on on standby it.
And yeah, after a thorough review, and we will re- restart the working, or maybe rework them.
So I guess it's fine just to return.
Marc Pichler (Dynatrace) 00:34:05 Okay.
I'm wondering if we should add some sort of a labor to these Prs to like signal that the they are kind of on hold
because they're neither draft nor
they're they're not markets draft. So it it's.
David Luna Bistuer 00:34:24 Kind of.
Marc Pichler (Dynatrace) 00:34:26 Difficult to figure out what to do with these.
Yeah, I will also try to join the meeting
tomorrow. You said, it's it's gonna happen right? So
yeah, I will try to join that. And
see if there's anything that we can do to move things forward.
David Luna Bistuer 00:34:51 My my guess is that I'm I'm going to paste some links in the chat
we're working on the semantic convention. So trust was, yeah, it was present in the last couple meetings.
And
we revital believe so. There are some. There are some semantic conventions that in there for a for a while. We're trying to
move them again and and have it merge up this semantic convention part. So at least we have the semantic conventions, even though they are
experimental development status. But I'll be at least we have it, because right now is
we don't have it at all.
So yeah, I guess the the line of work would be. But what I expect is like, 1st
start with the semantic relations and and review with the Apis, and then once we are.
you have an agreement on that. Then Morgan did some additions.
Marc Pichler (Dynatrace) 00:35:46 Yeah, that sounds good.
Alright, thank you for the insights on that, yeah, I, guess, then, we
skip this pr, for now and skip this Pr for now. And yeah, if anything comes up we pick those back up again.
David Luna Bistuer 00:36:11 Sure.
Marc Pichler (Dynatrace) 00:36:12 Right this is sqlized instrumentation.
David, you actually reviewed this one so that seems to be in progress. Now,
see if there's up to date, and added 2 additional component owners. It's our put thing here
right? And once we have these onboarded, I think
so be fine to move forward with reviews here as well.
Nothing immediately to do
with adding a new instrumentation for sqlice.
Then there's this exception. Hook for
the aws SDK reviewed by the component owner, and I also put the comment in slack last week
or week before that, letting the
person that opened the Pr. Here know that it's ready for.
Oh, so me changes now, and ready to be updated, and that the owner will approve it.
Haven't heard back from them yet. Yeah, I guess
3 weeks is what we said we are going to do. Going forward from the last comment on so
since I sent a message last week. We'll wait for 2 more weeks and then
come back to that one
marriage. It.
Trent Mick 00:38:59 I was talking muted. I ping them last week so wouldn't mind giving them a little bit more time. There's also some discussion on this side. It's possible some Microsoft folks that do Gen. AI stuff internally will wanna contribute and offer to be maintainers for
some instrumentations. But those will be Sep separate Prs from this one. But yeah.
Marc Pichler (Dynatrace) 00:39:21 Alright! Then we'll also keep this one open and sucker back to it
over the next few weeks, and see if there's there has been any activity.
This is also web this in draft.
Don't think there's been any activity since then.
One reach. So ours is fine on that the next one
is a draft Pr for propagator. Aws, X-ray
also commented, but no activity here.
Next one is
by default.
Daniel Dyla (Dynatrace) 00:40:31 Yeah, about this last week she said.
that she'd wait for the original author to reply for a week or 2, and if not. She would handle this.
MG Marylia Gutierrez 00:40:45 Yeah, and I know not.
Daniel Dyla (Dynatrace) 00:40:47 You're scape.
MG Marylia Gutierrez 00:40:48 Yeah, I'm here. Yeah, I'll say like, and I'm learning
to not skip any meeting. The one meeting that I did not attend. I just get assigned to things. So
yeah, just waiting for them to give a chance just in case they wanna do it. But then, probably next week, you can take over.
Daniel Dyla (Dynatrace) 00:41:07 Purely
usually afraid to join meetings because they're gonna be given tasks. But if you skip a meeting that's when you get assigned stuff here.
MG Marylia Gutierrez 00:41:14 Yeah.
Marc Pichler (Dynatrace) 00:41:19 Alright! Thank you for looking into that then the next one is also.
We have exceptions, probably also to skip.
David Luna Bistuer 00:41:37 Yeah.
Marc Pichler (Dynatrace) 00:41:38 I guess.
Yes,
The next one is a workflow for yes, I remember that.
I feel to follow up on that one.
Hector Hernandez 00:42:12 Yeah, I may need a refresh, but I think there's some permissions.
Yeah, we can discuss it.
Marc Pichler (Dynatrace) 00:42:19 I think this.
Hector Hernandez 00:42:20 Approach that collector is doing.
Yeah, we can talk to them about permissions as well. Maybe get some feedback on that side.
Marc Pichler (Dynatrace) 00:42:29 If if the collector is doing something similar, then I think it should be fine. We have the
book from here so that should always work. I guess.
Worst case we can just check
if it works by merging it and then disabling it if it causes a lot of failures.
yeah, I will have to have another look at this 6
outside of the court before approving this one, because it's also
like security. Wise something that I need to have a look at.
I'll put this in my notes and I will. I will give this another go.
But yeah, this would be helpful to add the actual labels to
the Prs if the owner approves it so that we can easily filter by whatever has owner approval and get these merged quicker.
yeah.
but definitely, not something to close.
Sure.
this one is a fix for instrumentation data loader.
Trent Mick 00:44:17 We're just waiting to see if they'll provide a test event.
Marc Pichler (Dynatrace) 00:44:28 And next one
cloud run support with.
This is the one that we talked about earlier. But we already have discussed this one, so we can also skip it.
Trent Mick 00:44:59 That one's released.
Marc Pichler (Dynatrace) 00:45:00 This one depends. Yeah.
Some depends on that one.
verified duplicate logging workaround
to stop duplicate. What's from happening?
It seems that they registered to transport and to the instrumentation itself.
And they're getting to.
But they're getting twice the logs
because, Winston instrumentation registers. It.
Daniel Dyla (Dynatrace) 00:46:10 Yeah, honestly, though, if you're using oh, Winston, transport.
Marc Pichler (Dynatrace) 00:46:15 And.
Daniel Dyla (Dynatrace) 00:46:16 Instant transport exports open telemetry logs to Winston right.
Marc Pichler (Dynatrace) 00:46:22 Oh, Winston, transport is basically the bridge that you can register yourself.
so it's just the bridging code, and none of the
booking or or anything like that, so you could.
If you were to bundle something up, you could also, use this Winston transport in your setup for Winston, and then
have logs exported.
Daniel Dyla (Dynatrace) 00:46:47 Yeah. So I mean, I guess the question I have is, why would you set up both? Why wouldn't you just disable the Winston instrumentation.
Marc Pichler (Dynatrace) 00:46:56 That's that's exactly what they are trying to do. Here, I think, is we have this call out here. That says logs would be duplicated if both
of the are added.
So yeah.
Daniel Dyla (Dynatrace) 00:47:17 Yeah, okay.
Marc Pichler (Dynatrace) 00:47:22 I mean, not sure what they are trying to accomplish with this thing is like disable log sending far.
I guess what.
Daniel Dyla (Dynatrace) 00:47:38 Like you should be able to disable the entire instrumentation right.
Marc Pichler (Dynatrace) 00:47:43 Yeah, I should be able to disable the instrumentation. But I think it does also something with span events. If I recall correctly.
Trent Mick 00:47:50 No, it's not span events. There's 2 features. It's log sending. You can get it to send log events
or the adding trace, id and span id.
Marc Pichler (Dynatrace) 00:48:04 To right.
Trent Mick 00:48:05 To Winston logs itself. If you're using a normal Winston transport sorry.
Marc Pichler (Dynatrace) 00:48:11 Good morning!
Trent Mick 00:48:11 So that's an overloaded term. There are 3 things that you could be talking about when you say the words, Winston transport. But
Daniel Dyla (Dynatrace) 00:48:18 Got it so in this configuration, where you disable log sending, but the instrumentations enabled it will add the trace. Ids.
But use the Winston Transport, v. 3 to send it manual.
Trent Mick 00:48:34 Quite sure what his bug was, so.
Daniel Dyla (Dynatrace) 00:48:38 Well, he was getting logs twice. The instrumentation was automatically sending or was sending
Winston was slurping up Winston and sending it to the open telemetry Api. And then he was also using the transport, which does the same thing.
Trent Mick 00:48:57 Yeah, I get that. The why did, says, added Doc. Help clarify.
Daniel Dyla (Dynatrace) 00:49:05 I think it's just an example of. So it says they'll be duplicated if you have Winston transport, and you use the instrumentation without disabling log sending. This is just an example of how to disable log sending so that you don't get duplicates.
Hector Hernandez 00:49:25 Yeah, it feels that it's more confusing. Looking at this.
Daniel Dyla (Dynatrace) 00:49:28 Yeah.
Hector Hernandez 00:49:29 And before, but.
Marc Pichler (Dynatrace) 00:49:32 That was the kind of feeling the same way here.
Oh.
Daniel Dyla (Dynatrace) 00:49:38 Yeah, I would probably.
Trent Mick 00:49:49 And it assign it to me. I'll suggest different wording.
Daniel Dyla (Dynatrace) 00:49:54 Maybe the.
Marc Pichler (Dynatrace) 00:49:55 Thank you.
Daniel Dyla (Dynatrace) 00:49:55 Can detect whether the transport is registered.
Trent Mick 00:50:03 Oh, I'm not sure I wanted to get to be magical, but
Marc Pichler (Dynatrace) 00:50:09 And then you can also register it later. Right? So you would be able to
registered with Winston after you've set it up, and then you would have to deny the transport being added
Trent Mick 00:50:26 Or someone could add a subclass of the open telemetry transport.
That doesn't like what? What attribute do you sniff on the array of transports
or a wrapper around the cause. You can have a transport that is, a wrapper around a transport that adds some attributes, but otherwise uses the functionality of the transport.
Anyway, I'll I'll take a look.
Marc Pichler (Dynatrace) 00:50:52 Perfect.
Thank you.
Alright. Renovate pot.
I guess we can just merge this one in while we're here. It's already approved. So.
Daniel Dyla (Dynatrace) 00:51:12 Boom.
Marc Pichler (Dynatrace) 00:51:13 Oh, still small wins in life.
Daniel Dyla (Dynatrace) 00:51:17 We closed the 2 prs. This week we merged one.
Marc Pichler (Dynatrace) 00:51:23 I guess. Renovate, but won't be mad, though, if we don't review their pr boom
alright, moving on.
Trent Mick 00:51:34 That's me. I'll take that one. Yulia poked me
in a DM. To take a second look at this one.
Marc Pichler (Dynatrace) 00:51:43 Got it. Thank you.
Mind if I assign you to this.
Trent Mick 00:51:49 Yeah, that's cool. Yeah.
Marc Pichler (Dynatrace) 00:51:55 No, that's not what I wanted to do.
And there was some other person today removed.
So slow.
Yeah.
right?
I guess this is for. Yeah, it already has been wrong.
Update alright.
a size or innovate bot, but doesn't seem to that. We can merge this.
These Eslint plugins are always
Eastland updates the rules, and when there's an update then.
Trent Mick 00:53:10 Aren't we also like 6 major versions behind.
Marc Pichler (Dynatrace) 00:53:14 Probably very likely that this is the case.
Someone, I think, recently updated Eslint in the core repo.
So we would have to do something similar here.
and the contrary people as well
just tends to be more work because there's more packages to go go through.
Only
alright.
Then the next one stretch for container, Id. From Ecs. For Gate, who is is a draft.
Daniel Dyla (Dynatrace) 00:54:01 It's a draft. Yeah.
Marc Pichler (Dynatrace) 00:54:02 Why?
Daniel Dyla (Dynatrace) 00:54:03 Last time we were just saying like, Hey, this is really old draft. Can we close it.
Marc Pichler (Dynatrace) 00:54:23 Okay, trying to find wording here on zoom.
yeah.
Daniel Dyla (Dynatrace) 00:55:05 I think we might want to think about
making like a markdown file somewhere that has like.
here's some, you know, pre-made responses for common issue triage things.
Marc Pichler (Dynatrace) 00:55:24 Yeah, sorry you have to look at me struggling, coming up with wording.
Daniel Dyla (Dynatrace) 00:55:29 Not about that as much as just like we do it every time. And it's like we say the same 5 things over and over and over.
having some consistent wording, and then it could also link to a file. That's like, here's a longer explanation of what we mean when we say this, and what you can do about it.
Marc Pichler (Dynatrace) 00:55:47 Okay, yeah, I think that would be very helpful along with
possibly some rules as what to expect when something is in draft.
like the explanation that you were mentioning would be one of the things
that we could say, and when it's in draft we usually think spect is not ready yet, and we won't review it.
Oh.
Daniel Dyla (Dynatrace) 00:56:12 Yeah, I mean, I think that's
kind of explicitly what draft is for, even when it's something in draft, the button says, ready for review to tomorrow.
Marc Pichler (Dynatrace) 00:56:22 Oops.
Yeah, but it's
sometimes one just has to bring it up again. It's similar to the Cla bot right where people open the thing, and it has, like the large red
id missing thing, or like signature missing thing. And
people need to be poked sometimes, too.
Take care of it.
MG Marylia Gutierrez 00:56:52 Maybe something that can get added to the contributing guidelines because we already have a session ball.
Prs, and I don't know merge requirements.
Marc Pichler (Dynatrace) 00:57:08 Yes, we could just probably add one thing here that, like general merge requirement, or something like that.
till it's supposed to be not in draft.
because we literally can't merge
anything that's in draft as well. Right? It's like the buttons grayed out. If I recall correctly.
Yeah.
alright. The next one will be outdated. Now that I merged the other one.
David Luna Bistuer 00:57:51 This one.
This one is a draft, this for me. You can vote so you can see it better.
Marc Pichler (Dynatrace) 00:57:59 We skip this one, and next one is also renovate.
if you
see your renovate Pr, and you have permissions to approve and merge. Please feel free to do so. If the tests are passing.
I'll be usually the quicker we merge the renovate Prs the better, because if they get outdated.
It's very difficult to figure out from the package. Look
what package cost built to fail. Ask me how I know.
alright, this is instrumentation. Pops. Chris, pretty recent.
Trent Mick 00:58:53 Yeah, Marillia, I've done a review on this. I just had a question for you in the main. There, I'm not sure the tests are covering the different opt in.
MG Marylia Gutierrez 00:59:00 Yeah, so I did tests of like, the default is the as the default it is for now. And I made some tests with the functions accepting the new value. But I guess I need to do one with like the environment that are being bolt or something like that.
Trent Mick 00:59:15 But I I don't know that maybe it doesn't have to be the environment variable. But I'm not sure were there any tests of like.
If someone selects the new, we don't actually get the old one. So I'm not sure there was any kind of negative test to make sure that.
MG Marylia Gutierrez 00:59:31 No, that one I didn't. So yeah, pretty much. The ones that I did is
the default it is to send just the old one. So I tested all the tests, making sure that we have the old stuff some of the new functions that I created, I tested using them the new one, just to see if it is getting that. But yeah, I still need to add some extra stuff.
Trent Mick 00:59:55 It's possible I just missed those tests.
MG Marylia Gutierrez 00:59:59 Yeah, but I still need to add more.
Trent Mick 01:00:00 And ping me. Yeah, let me know. And ping me, and I can review again.
MG Marylia Gutierrez 01:00:04 Cool.
Trent Mick 01:00:05 But otherwise it's fine. That's all good.
Marc Pichler (Dynatrace) 01:00:10 Right?
yes, that's it. For today. We've run out of time.
thank you, everybody. And see you next week.
Daniel Dyla (Dynatrace) 01:00:25 Next week, thanks, mark.
Trent Mick 01:00:27 Thanks, Brent.
Jackson Weber 01:00:27 Okay, see you bye us. But.
