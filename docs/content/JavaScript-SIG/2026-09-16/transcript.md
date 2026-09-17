SIG: JavaScript SIG
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trent Mick 00:03:01 Never know.
Marc Pichler 00:03:04 Nope.
Marylia Gutierrez 00:03:44 While we're waiting, Mark, do you want me to merge the admin PR?
Let me know when you…
Marc Pichler 00:03:51 Thank you. I actually wanted to talk about that, just for a second before we do that. But thank you for approving it. I can… I think I also have permission to merge there, so… Okay. I will do it once we're ready.
Marylia Gutierrez 00:04:07 Okay, no problem.
Marc Pichler 00:04:14 Alright, I have to close my 15 million.
Browser tips before sharing.
Oops.
Welcome, everybody. I guess we can get started.
The first topic here on the agenda today is from Trent…
Trent Mick 00:04:46 Sorry.
Marc Pichler 00:04:47 saves, like, about the…
Trent Mick 00:04:53 Yeah, I can… I can repeat it.
Nope.
Or, presumably, hopefully, people can follow through on that one. So, again, on the widening… the attributes type, and adding in any value export. This is… all part of… Stabilizing logs, so API logs eventually moves into the API.
So, if we were to do this, is it okay to… bump the peer depth on the API package in other packages that need to do so.
And that doesn't… So basically saying that a new version of OpenTelemetry Core would have a peer depth on the new latest minor version of API.
Marc Pichler 00:05:41 Aye.
Trent Mick 00:05:41 package, instead of supporting back all those older versions. Is that… is that okay, or does that break some contract that we have with users, or…
Marc Pichler 00:05:49 What we usually do is we do that within the context of a major bump?
So an SDK major bump would also raise the minimum supported API version.
So that…
Trent Mick 00:06:02 Or would we do that re… Regardless, even if we didn't have a need to do that, would we move the bump up, or only when we need to here?
Marc Pichler 00:06:10 only when you need to. That's why some of the packages are at 1.4.0, some of them are at 1.1. It's really just a thing that we do when we have to, because it means that people have to bump the API version, and they might not want to So we keep as much compatibility as we can.
But for new packages, for example, when we introduced SDK metrics, we… had to go to 1.3.0, because, metrics wasn't there yet before that, so…
Trent Mick 00:06:47 Right, that's what I said in my comments. Some of them got bumped to 1.3 when API Metrics was merged in. Okay, Okay, just because I'm me and my wife hates me when I do this, I don't actually need to dive into this detail, but would we need to have a major version of Core to do that? Like, is it a requirement, other than, like, we're trying to be nice and not force you to bump your API version to a new miner?
Marc Pichler 00:07:17 Oh, that's a good question. I don't know the answer to that, actually. There might be some spec requirement that we are trying to adhere to by doing that, but I'm… Not entirely sure.
Trent Mick 00:07:33 Yeah, okay, fair. Because, like, by rules of… Senver, at least, we shouldn't need to, right? Just requiring that you have the latest. Or a newer, minor version of something shouldn't… break the user, they just… when they're updating one package, they have to update some other dependency, period.
Marc Pichler 00:07:48 Mmm.
Trent Mick 00:07:49 This case, but… okay.
Given that in the past we've done this with a major version bump.
if I can get this stuff approved and in.
in September here, then… It all seems fine.
Does that sound… Is that correct? Okay.
Marc Pichler 00:08:07 We would just merge it in, and if we start using it.
anywhere, we would just bump the peer dependency version to… Whatever version is gonna be next.
And… should be finding… I'm not sure if we have enough automation around that, because it's kind of finicky dealing with API peer dependencies.
So delights.
Trent Mick 00:08:29 I suspect not. We need to manually.
that in the PR that creates the new version, I'm guessing?
Of the API?
Marc Pichler 00:08:37 So, yeah.
Trent Mick 00:08:38 Yeah, yeah, okay, that's what I expected as well.
Okay, thanks, I think that answers that question for me.
Jared Freeze (Palo Alto Networks) 00:08:48 Quick question. Are you guys talking about the comment I made about 1.4.0, or is that related?
Trent Mick 00:08:55 I'm not aware of that. I don't know which comments you mean, so… Okay. No answer, but what's the comment?
Jared Freeze (Palo Alto Networks) 00:09:01 I'll dig up the link. It might have been on David's PR, but we had something where I think I said, this doesn't match the rest.
Marc Pichler 00:09:13 I hate it.
Jared Freeze (Palo Alto Networks) 00:09:14 You can work on this right away.
Marc Pichler 00:09:16 That's okay.
Jared Freeze (Palo Alto Networks) 00:09:17 I'll pull up the link.
Marc Pichler 00:09:19 It might be, anyway… in the PR that we're gonna talk about in the next topic, right?
the one that removes SDK trace web.
David Luna Bistuer 00:09:44 There is no… no PR yet for moving that.
The utilities and the components, yeah.
or not yet, but I've seen that The, examples that there are some talks that are still referring to SDKreeze Web.
So first, I'm going to change that.
And just the SDK trace first, and then… when that's done, I'll proceed, so I'm happy to do it, so… I agree that we have to remember that.
Marc Pichler 00:10:19 Right, thank you. If you have any… yeah, if you, if you, have any PRs that need approval, please feel free to send them to me, and I will also have a look, as quickly as I can.
David Luna Bistuer 00:10:31 Cheers.
Trent Mick 00:10:35 Likewise, if you need.
In my time zone.
Marc Pichler 00:10:41 This was the comment, right?
Oh… Yeah, it was kind of related. We were talking about bumping the… Version on the core package.
So the minimum required API version on the core package. And it has similar implications as what you described here.
Where people will run into this.
Which is one of the reasons why we would consider only doing that via a major version bump, because, It's… It can be very difficult to know, like, which version you need to install now, and it's kind of frustrating to deal with, so…
Trent Mick 00:11:37 But it's only unresolvable if the user is pinned to… In this example, 1.3.x. Is that right?
Jared Freeze (Palo Alto Networks) 00:11:46 That's right.
Trent Mick 00:11:47 And theoretically, as long as… we're following SEMVR properly, they should be able to go to 1.x.
And then it's resolvable.
I mean, I understand, you know, Stuff's hard, so… You don't want to force the user to have to do that, but okay.
Marc Pichler 00:12:07 Yeah, there might be third-party packages that pin the API version,
Trent Mick 00:12:13 yet.
Marc Pichler 00:12:17 It's always a bit… a bit tricky.
Jared Freeze (Palo Alto Networks) 00:12:21 So, in our vendor SDK, I have an integration test that does that latest for absolutely everything, just to see what falls over.
Obviously, that's an easy thing to do. If you… want me to do that, I will, in the JS repo.
I've had this ticket for a long time to pull web stuff into JS, and to pull JS into browser, just so we all are on the same page. We could also do a matrix where we run through a couple of these versions, you know, just with an, you know, a VEET build, you know, just to see.
If you'd like, I can prioritize the JS version pulling in browser.
That seems much more important than browser at this point, because… no one's using our instrumentations. Not a lot of people, basically. But everyone's using JS, so that might be better.
Trent Mick 00:13:19 Okay. I'm not exactly sure what you're saying, because the Slack thread that I'd posted for the first agenda item here, I'd had a second comment in the thread on that Slack thing, asking if we're doing… and this is… slightly different than what you're saying, but I'm not sure I understand exactly what you're suggesting testing, but do we have any tests where we test, for example, whether the latest version of OpenTelemetry Core works with an early version of OpenTelemetry API that is in its peer depth range.
Marc Pichler 00:13:50 We don't, but we should have. I think that would be one of these tests that we should definitely do, because, it has Rakuten people in the past. One of the examples that comes to mind was introducing Advice on metrics?
Instrument creation.
So what you can do is, you can specify, like, an advice of, like, which buckets to use, or histograms.
And we introduced that, and we introduced a new type.
we used the type in the metrics SDK, and then that type didn't exist on older versions of the packages, and then a compiler failed.
Trent Mick 00:14:36 A test passed, because it's always testing the latest version.
Marc Pichler 00:14:39 Yeah, exactly. So, having that would be very helpful.
Trent Mick 00:14:44 Okay, so that was me hijacking what Jared was saying. Jared, what was it you were suggesting testing?
Jared Freeze (Palo Alto Networks) 00:14:49 Same family of idea, which is, like, pinning certain versions of things, and just… trying to make a mess out of it, like this, like, where you, like, pin to 1.3 and, like, pull in the newest, and then the opposite, you know, whatever, just, I mean, for us, it would be the cross-repo is what I would focus on, but same idea, where we'd have a folder of just sort of chaotic, version, you know, cross version stuff.
Is what I was kind of thinking, because you can just run through VEET quickly to build and see what happens.
Trent Mick 00:15:23 Okay, cool.
Marc Pichler 00:15:30 Yeah, I think that would be helpful.
There is one category of, pain that's kind of introduced when a new API version is released.
Which we haven't done in a while, like, a new API minor version where, people who are running older SDKs.
have to update their SDK to be compatible.
Because we defined, like, an upper limit of which API is compatible.
So any tests would have to leave that category out, which might be a bit difficult.
to do.
But I think it makes sense to, have that sort of test.
I'm actually kind of worried that when we release 1.10, we'll get a flood of issues from folks that have never experienced that, sort of… Thing, because we haven't released in 2 years. New API.
Trent Mick 00:16:50 But when we do… We should… the migration doc that we're gonna have for 3DX, we should probably have a section for that.
Can we specifically point that out in the release announcement.
Marc Pichler 00:17:05 Yep.
I agree.
Right.
I guess that's it for that topic, David, I think we, did discuss yours briefly, or, you were just saying that you were going to open a bunch of PRs in Core and Contrip to remove, yeah.
David Luna Bistuer 00:17:42 Listen.
Marc Pichler 00:17:42 tracer provider.
David Luna Bistuer 00:17:44 At least one. I'll check, Two in the core repository, first to update the examples, and then finally to move the package.
And then I'll check if the contribository needs some details as well.
Marc Pichler 00:17:57 Okay. Thanks, Jason.
David Luna Bistuer 00:17:58 So, at this tool.
Marc Pichler 00:18:03 Right.
Moving on… Yes.
Trent Mick 00:18:09 This is the same me asking every week, yeah, it's been… Number of weeks, yeah.
Marc Pichler 00:18:14 Yeah, I'm sorry for not getting to this one.
Trent Mick 00:18:17 You don't ever have to feel sorry, it's fine.
David Luna Bistuer 00:18:21 Me too.
Marc Pichler 00:18:22 hoping that I will have some time this week. If anybody else wants to have a look at it, please do.
Any… Anybody had a look and has some… Ideas that we should discuss now?
I cannot, I guess let's move on to the next topic, Trent $3 milestone, yeah, that's also something that I would have, brought up, if we run out of topics. If anything else comes up where we're talking about 3.0, please feel free to interrupt us, and we can talk about… another topic.
One thing that I just, maybe I mentioned that briefly, I just opened the PR for 3.0 to pump the minimum Node.js version to 22.15, this is the version that, trent you suggested in the Issue where we were talking about, the minimum supported Node.js version for
Trent Mick 00:19:57 Register hooks.
Marc Pichler 00:19:59 Yeah, exactly. I did leave out this, 23.
Version here, because that's out of our supported range anyway.
I'm not sure if we should explicitly… Note that in the… in the packages, or if we can just leave it out.
Trent Mick 00:20:18 What we can do is do, a caret on that 22.15, and then… 24 and greater, but I, like, explicitly say or 24 and greater, but I'm not sure we need to do that. I think people understand.
That the… the odd versions are excluded there.
We could just state that in the docs when we do this, or in the commit message.
Marc Pichler 00:20:44 Yeah, I think we have, somewhere in the README.
information about… which Node.js versions we support is, this one here.
Node.js Active or Maintenance RTS.
Yeah, so this is just me saying that the PR would be open for review. I also have an admin PR. This was the one that Marlia, mentioned earlier.
To remove the required checks for 18 and 20.
To get the SDR to merge.
I left it open for… Discussion until tomorrow.
And if there's no objections, then I merged it in.
Trent Mick 00:21:44 Has… has anyone gone through the changelog for… 22.x minor versions after that, to see if there's something interesting that we'd want to pick. Like, this is the best time to… pick. I haven't, you know.
Marc Pichler 00:22:00 haven't checked. The main thing that I… Was looking forward to is, bitch.
Which is not behind the… Blackmail can be disabled.
So, 22 already includes that.
So we can use fetch for exporters in the future if we… 1, 2… Other than that, I haven't really checked the changelog.
To see…
Trent Mick 00:22:36 Good.
Marc Pichler 00:22:41 In any case, I think if we merge that PR and decide later to bump that, we can still do it until the end of September, so if anybody runs into it, and sees a feature that they would like to have.
We can still change the version, before the month is over.
And then we would be stuck with it for a bit.
Trent Mick 00:23:06 Yep.
Cool.
Jared Freeze (Palo Alto Networks) 00:23:10 I have a question about 3.0. So the core… the… Like, at root, package JSON does not specify type module.
When, in fact, a majority of… the environmental files are ESM.
So, like, I'm seeing, like, Karma Base is not, but it could be easily converted. But there's some other things that are.
That's a lot of work. I think now would be the time to do it if we're gonna do it.
to just say it's ESM, because in fact, most of the config files, most of the setup, most of the… The other things at root are… Actually, ESM. We're just saying.
mjs when we could invert it, if you wanted to keep CommonJS files. If you don't, you know, we could convert them.
to ESM, because almost all the utilities will accept that.
Marc Pichler 00:24:19 What you're saying is, for example, here in this package, Ed, type module, and then…
Jared Freeze (Palo Alto Networks) 00:24:34 Yeah, now, I… so what I wound up doing is including explicit extensions?
So there's no ambiguity about what is what.
So, in this, type module is not here, so .js would be interpreted as common.
But I went ahead and included TGS, so just, like, again, no ambiguity about what you're getting.
It… Still matters.
It still matters for, you know, files where someone would forget the extension on… Or for files that are .js that are config files at root.
Because that's how the interpretation would work. So, adding type module to everything is something that Publint will complain about.
It'll say pick one.
You know, when in fact Node's default is CommonJS, so if you don't put anything, you get CommonJS as the interpreter.
Do you guys want to do that? Because every… I mean, most of… most of the… this entire repository is using import.
You know, for a lot of the… again, for the configs.
Marc Pichler 00:25:49 Oh, with the configs you're talking about, this right here, for example, are…
Jared Freeze (Palo Alto Networks) 00:25:56 Right.
Marc Pichler 00:25:56 I'm… I am.
Yeah,
Trent Mick 00:26:00 That one's .ts, so, like, the karma.confident.js files are still using… require, for example, but I don't.
Marc Pichler 00:26:06 Right.
Jared Freeze (Palo Alto Networks) 00:26:09 I mean.
Marc Pichler 00:26:09 I think it's.
Jared Freeze (Palo Alto Networks) 00:26:10 A little churny, but, you know, it'd be… the consistency would be nice.
This is more for us than consumers, but it would change. It would change what consumers see.
But now that, you know, we only support node versions in most of these packages that are, you know, ESM, Should be… should be fun.
Trent Mick 00:26:32 There are 110 JS files, and… the repo.
Jared Freeze (Palo Alto Networks) 00:26:39 Yeah, and again, if we didn't want to change the content, we would just add .cjs to those files, and then add type module to the package JSON.
Trent Mick 00:26:47 Yeah, I gotcha. Yeah.
Jared Freeze (Palo Alto Networks) 00:26:48 Yeah.
Trent Mick 00:27:00 And I guess the ancient, not updated examples, you could just, say, type CommonJS in them if you wanna… Avoid some work, but, yeah.
Jared Freeze (Palo Alto Networks) 00:27:08 Yeah, just to quiet down the warnings, because I do think the… You know, a lot of the environmental tooling is getting a little stricter, so… It'd be nice to… Go full on and just specify.
There's also other things, too, I mean… like, module.
at the top level, inside the package JSONs is not valid.
at all. I kept it to be conservative, because, like, I don't know exactly what people are using. I think it's very possible that they're using a webpack that we say we don't support, but it would You know, deleting that line and just posing them, you know, without really affecting anybody else seems unnecessary.
Trent Mick 00:27:55 Do you know that's where that came from? Like, almost certainly it came from an earlier Webpack version, but do you know that?
Errh.
Jared Freeze (Palo Alto Networks) 00:28:01 I… I would bet on Webpack for pulling that in to use ESM, because exports… it definitely doesn't support exports.
And so, I think if you were in, like, an ESM mode, it would actually pull that key.
I'm pretty sure.
You know, in the olden times, it was the only way to pull an ESM in a package JSON that specified nothing.
So… But, like, you know, what version of parcel are we willing to support?
That's the sort of thing that I, you know… I haven't investigated, but, you know, in browser, we say.
We don't support any of this. Like, we explicitly say, do not use Webpack 4, it will not work.
You're welcome to try and do all the aliasing and all that good stuff and dig into the folders, but it's not recommended, because… it will keep breaking. I mean, it's just constant maintenance for somebody, so…
Trent Mick 00:29:00 Yep, yep.
Jared Freeze (Palo Alto Networks) 00:29:05 I mean, talking…
Trent Mick 00:29:06 Winpack 5 is to… Webpack 5 is the lowest version we have in the bundler test directory, so I would say.
Jared Freeze (Palo Alto Networks) 00:29:13 It's because of this.
Trent Mick 00:29:14 Yeah, yeah, no, I understand.
Jared Freeze (Palo Alto Networks) 00:29:16 So the browser key at the top level is also invalid. That is… that is a convenience.
That should probably go away as well. But again, I was trying to… I don't know how much… how nuclear we want to make this, release.
Marc Pichler 00:29:32 One of the things… that I would throw out there is… We could do it for $30, and if we get… Lots of issues opened, we can add it back.
Nothing prevents us from doing that, right?
That's true.
Jared Freeze (Palo Alto Networks) 00:29:54 Yeah.
Marc Pichler 00:29:55 We could release 3.0.0, and then if we get a bunch of issues, we release 3.1 and add these back.
Oh, okay.
Trent Mick 00:30:09 Do so silently, or specifically mention in…
Marc Pichler 00:30:13 I would mention…
Trent Mick 00:30:14 migration dog.
Marc Pichler 00:30:15 Right? Yeah.
Trent Mick 00:30:17 We've dropped these, we expect Webpack 4 usage to break.
Marc Pichler 00:30:21 Yeah, and I think…
Trent Mick 00:30:22 Leave it hanging, like, you need to show some initiative to go open some issues, if you care.
Marc Pichler 00:30:30 Yeah, I think we could just say, like, you know.
you need to migrate to Webpack 5, and… Then there's probably gonna be people still that still want it, and those are gonna open issues.
Jared Freeze (Palo Alto Networks) 00:30:51 Yeah, I mean…
Marc Pichler 00:30:55 It's unfortunate that we don't have a lot of telemetry ourselves to actually make that car, Based on data?
But that needs to be…
Trent Mick 00:31:07 You're never gonna have.
Marc Pichler 00:31:08 That's a bill.
Trent Mick 00:31:09 tilling. It's fine.
Marc Pichler 00:31:10 Yeah.
Trent Mick 00:31:11 I don't mind that idea, yeah, if it's a… clearly written in the PR that here we're explicitly cleaning up and dropping We expect this to break Webpack 4 support and do it, and go, and then… I don't know what… lots of issues, like, I don't know what the threshold is for us putting it back, if one person complains.
What do we say, but… I don't know.
Like, is Webpack core maintained by Webpack anywhere?
Jared Freeze (Palo Alto Networks) 00:31:42 -
Marc Pichler 00:31:43 I think.
Jared Freeze (Palo Alto Networks) 00:31:44 Gone, gone. It's been years.
Nope.
Trent Mick 00:31:48 Okay, okay. So, like, I wouldn't feel bad.
Jared Freeze (Palo Alto Networks) 00:31:52 There's another issue I'd like to bring up, which is that, you know, CGS is not valid on the web. It doesn't run in any context. Not that I expect anyone to not be using a bundler.
Trent Mick 00:32:02 Interesting.
Jared Freeze (Palo Alto Networks) 00:32:03 But technically, a web build using CJS? Are you not using a web builder?
Trent Mick 00:32:11 Well, I'm just… I'm a Node.js dude, man.
Anyway…
Jared Freeze (Palo Alto Networks) 00:32:16 So, yeah, but if you were to pull in, files, you know, again, so, like, here at the browser key, that .cjs file.
Is a weird setup with an even weirder build process.
No one should actually be hitting .cjs with a web build itself, so… And again, it's… it's… You know, if we were to say, hey, we strictly support, you know, the web as it is, again, no bundle, that file doesn't run for anybody.
It is there strictly for, again, being conservative on my side, to just say, like, hey, we had that file before, we still have that file, but truly, this is… I'm not sure there's a consumer of this that's… you know, real, so… If we're gonna…
Trent Mick 00:33:03 Okay, so…
Jared Freeze (Palo Alto Networks) 00:33:04 the browser key, we should remove the browser mappings that do NodeCJS to browser CJS.
Trent Mick 00:33:15 Sorry, is there a mapping somewhere else other than this browser key in the package.json file?
Jared Freeze (Palo Alto Networks) 00:33:22 Not in this file. I think… I believe there's others where we had to do that, like, in the, some of the utilities, like the SDK utils.
one of those, or, like, where the OT Performance used to live?
Like, there… it was, like, there's a fork where it says, like, if you pull in this file, but you… Are in a browser build, you get the browser file instead.
I forget where that was.
Marc Pichler 00:33:54 The core package as well.
Trent Mick 00:33:57 That's where OTP.
Marc Pichler 00:33:58 performance with.
Trent Mick 00:33:59 Yeah.
Marc Pichler 00:34:00 Yeah.
I think the package JSON for the exporters might also be very weird, micrime, probably.
But yeah,
Trent Mick 00:34:19 I've never heard someone phrase it that way. My crime. I like it.
Marc Pichler 00:34:24 That's me not being a native speaker, probably. Anyway,
Trent Mick 00:34:32 I thought those things relied on this browser keyinpatcher.json file. I might be wrong, but, like.
Jared Freeze (Palo Alto Networks) 00:34:38 No, you are right. That is what I am remembering. So, you can look at, exporter logs, OTLP Proto.
But when the browser key goes away, you're right, they get dropped.
They don't exist outside the browser key.
we will get Webpack complaints.
And… we should just have a plan.
Yeah.
Trent Mick 00:35:05 I'm guessing your ideal is we hold a stronger line on, even if we do get complaints, saying, sorry, we can't support WebPad 4 anymore.
Jared Freeze (Palo Alto Networks) 00:35:12 we just say, hey, the npm package JSON spec, Never provided this key.
it just didn't. This was absolutely, an optimistic, proposal.
From… somewhere else that NPM never picked up. So this does work for people, and it is keeping their projects alive, but it was never… fully supported.
Same with…
Trent Mick 00:35:38 Well, but I mean…
Jared Freeze (Palo Alto Networks) 00:35:39 Yeah.
Trent Mick 00:35:41 I'm just being devil's advocate here, like, NPM doesn't own the package.json spec. Sure, they started package.json, but, like, any number of tools out there add their own keys for… using the package.json file as a place to store config and things like that. And, like, so it wasn't totally… I mean, it's messy. Package.json's a nightmare to know what Tool uses what keys in there.
It was… But it wasn't… I guess it's debatable. Wasn't totally out of reason for, early versions of Webpack to tell people to use this key to do the mappings, but… yeah.
That said, if, like, Webpack doesn't support Webpack 4 anymore, and we're way past… I don't know what the timeline was when Webpack 5 was released.
like, moving on for a new… in a new major version, I don't have a problem with that.
Jared Freeze (Palo Alto Networks) 00:36:33 Okay.
Marc Pichler 00:36:34 Yeah.
Jared Freeze (Palo Alto Networks) 00:36:34 Cool, and you are, you are correct.
I mean, I'm remembering now, like, yes, it's sort of flexible, but I keep going back to the package JSON, like.
page on, you know, npm.com to go look and see, and it's not there, so…
Trent Mick 00:36:50 Yep.
Jared Freeze (Palo Alto Networks) 00:36:51 Okay.
Marc Pichler 00:36:53 -Oh.
Let's just remove it and see what breaks.
Jared Freeze (Palo Alto Networks) 00:36:59 I think that's the move.
Yeah, because like I said, I mean, officially we dropped Webpack 4 support.
Already. That's why the integration test is wrong.
Sorry, that's why the integration test is gone.
So…
Marc Pichler 00:37:13 Yeah, I think we also had some discussion around Webpack 4 at some point. I don't recall anymore, I can't find it, but I think we made the conscious decision of not supporting it anymore.
Jared Freeze (Palo Alto Networks) 00:37:29 Yeah, it's because… because there are sub-modules.
that are required for browser to run. That was the idea. You can't use submodules, because you need the exports key.
Marc Pichler 00:37:42 Right. So… Yeah, that… that was then the reason why we dropped support for… for WebEx4.
I'm not sure if it happened within SDK 2.0 work, or if that happened somewhere… sometime after that.
but I think it would make sense to just… Call it out explicitly in the migration doc for 3.0, and then… See if… there's maybe some other tooling that, breaks from that, or if it's really just Webpack 4, and if it's Webpack 4, we just say.
There's no support for it anymore.
And 2.X will still be supported with priority bug fixes and, security fixes for a year after we go out with 3.0. So, They don't have to scramble immediately to get updated, but… They should consider it in the backlog for the next year.
Jared Freeze (Palo Alto Networks) 00:38:57 I like using emojis.
Marc Pichler 00:39:02 Was there an emoji somewhere? I didn't…
Jared Freeze (Palo Alto Networks) 00:39:04 Oh, I put a waving goodbye emoji on this PR.
Marc Pichler 00:39:14 Alright, so I guess we have a plan for… What we're gonna do with these, exports. I think we haven't settled on what to do with, if we want to put the… type module.
build.
on the package, JSON.
Is the implication of that, that Node will do require ESM?
on these packages, and Common.js is that code.
Even if we have the entry point.
Jared Freeze (Palo Alto Networks) 00:39:57 So my understanding is that modern tooling ignores all top-level keys if exports is present.
It doesn't use main, doesn't use module, doesn't use anything. If it sees exports, it uses exports.
I don't know in the Node world, like, in the backend world, exactly what people are using to put things together, you know, if they don't use any bundle or something like that. In Webpack specifically, and, well, Vite, everybody followed the lead, for that matter.
There is a main fields config option where you can specify keys.
Which is where there was advice to use a browser key. Or if you had something like browser true, it would hunt for the browser key at the top level.
Somebody may be doing that as well, where they started a project a long time ago, and they said.
the main field I want to use is not main. I want to go into ESM mode, and I don't have a way to do that in my config, so my main field is module. Like, go, like, find that. If you don't find that, it starts to do fall… it starts to fall back into other things.
I… I am not certain what people are using.
I don't have a lot of experience with that environment, but… There are odd things that you can do in configs to pull out specific keys, so… Like I said, if you were… it would be for someone that had Node running, and then wanted to use ESM early.
they would have pulled in the module key. And so, they would have had to have been eager to use ESM, and then also not have updated since then.
Which is probably, again, not a real person.
Marc Pichler 00:41:39 Yeah.
That makes sense. Yeah.
Alright, I'll try a few things out.
Trent Mick 00:41:54 I'm trying to refresh my memory on what Node'll do, like, I think it's… But I'm just, yeah, I'm hesitant because I don't know what the impact is, but I think, given we have exports defined everywhere, I think we're probably… Fine.
Marc Pichler 00:42:10 I've…
Jared Freeze (Palo Alto Networks) 00:42:10 what I would propose is I'll make a PR to remove all browsers, so that sits in one commit, so if we have to revert, it'll come back out easily, and not include anything else with it, just to be safe. I know that's the rule anyways, but I don't mind doing that.
Marc Pichler 00:42:29 Sounds good. Yeah. Cool. Then let's do that. Our… See and check if… what Node does, because I also don't… No, immediately, Right now, what it would do if we were to add type module and still serve both.
And…
Jared Freeze (Palo Alto Networks) 00:42:51 It is… yeah, it's version.
Marc Pichler 00:42:53 10 boosts.
Jared Freeze (Palo Alto Networks) 00:42:53 So, getting rid of main as well, I know that feels super dangerous, but again, the newer nodes, I believe that's what you just posted.
Is that if it sees exports, it uses exports and ignores.
everything else.
Marc Pichler 00:43:07 Yeah, perfect. Yeah, I'll check, and then we can decide on that, if… you're also looking to open a PR for the other changes in package JSON, then we can just discuss during the PR review.
Alright.
then I guess we can move on to… the rest of the milestone here, I haven't checked if there was any new topic here. Doesn't seem like it.
I haven't gotten around to publishing the re-release yet.
I was meaning to… release.
these development versions, ran into some trouble with the bundle tests, because, funnily enough, one of the dependencies that we have here Pest is… your optional API dependency, and if we have a pre-release version that doesn't match They're like… carrot, thing, so… I need to find a workaround for that.
Other than that, everything seems to be working fine. I… I'm hoping to get to it this week to get the pre-release out so that we can test some of these changes.
That's just an update on what's going on there.
If anybody else also wants to have a look, please feel free to do so.
We'll probably only have time.
Tomorrow evening, or Friday, so… Might take some time there.
I think, I've also added this issue here.
We've already kind of agreed.
on that, I think, to, drop the SDK trace node package.
I put the… Up for grabs later on this one.
Any objections still to removing that package?
David Luna Bistuer 00:45:51 Nope.
Marc Pichler 00:45:52 And our support, triage accepted label on it.
And let's see if, anyone's interested in picking that one up?
I haven't done a lot of the PRs myself, because there were a lot of people who were eager to open PRs for it, and it just tends to be a bit quicker.
So the up-for-grabs label is very helpful here.
export a Jager package we had already talked about, it looks like, or so there was a PR open for… It's already closed. I think that was opened.
Before we started work on 3DGO.
So… I will also put… Up for grabs later on to this one.
Trent Mick 00:47:03 You did… you had closed that PR and just said, I'm closing it now to not have the clutter, feel free to reopen when it's no longer blocked, so… could just… ping on that issue and reopen that guy's PR. I didn't look to see if the PR was… A good implementation, but…
Marc Pichler 00:47:20 I'll have a look at it again, and we'll reopen the PR if… If we can easily do that… It should be just a removal of the package and then binding them to the OTRP exporters. Yeah.
Let's see, We also have another package remover, this is the Shim Open Sensus one.
Also ran into some, conflicts now.
Trent, would you be looking to continue work on this, or should I also just put the… Labor on the issue. I feel.
Trent Mick 00:48:12 You can put up for grabs on it.
Pick me off.
I mean, I might get to it, but happy if someone else does.
Marc Pichler 00:48:21 Actually checking now, do we have an issue for Shim open census Remover?
Trent Mick 00:48:26 Not sure, not associated with the issue.
Marc Pichler 00:48:30 I think we might just have to… DR here, so I keep that open and, recreate an issue.
Let's see if somebody will pick it up there.
Trent Mick 00:48:44 Oh, sorry, was this a poll for me?
Oh, okay. Sorry, I thought it was just an issue that I'd… stamp my name on Is there another PR?
Marc Pichler 00:48:53 I am.
No, there's no other PR. I think it's just this one.
Trent Mick 00:48:58 I just need to update.
Marc Pichler 00:48:59 issue for it, so…
Trent Mick 00:49:01 I just need to update this one to main. Okay.
Okay, I'll get back on the hound.
Marc Pichler 00:49:09 No worries if you don't find the time, I guess we could just always open an issue and let somebody else,
Trent Mick 00:49:16 Definitely.
Marc Pichler 00:49:17 Handle it, and we do the review on it.
Alright, this one we already talked about, I think,
David Luna Bistuer 00:49:33 Does it make sense to navigate that?
Are you already removing the package?
Marc Pichler 00:49:38 Yeah, I think.
David Luna Bistuer 00:49:39 you know.
Marc Pichler 00:49:40 close this one, yeah.
David Luna Bistuer 00:49:42 Oh, yeah.
Yeah, I haven't closed this one yet.
Because it says in the checklist that this should be published.
But I guess, If you want to wait to… if you want to wait to… to have the published package, with the… Thank you. With the YouTube.
Marc Pichler 00:50:04 I look for you.
I think it should be fine if we just close this,
David Luna Bistuer 00:50:09 Hmm.
Marc Pichler 00:50:10 One option that we could… do is we could backport it to… to the decks, and then publish… Webb with the deprecations on it, but, I guess I'm fine without doing that. The whole package will go away, so we will have, like, one.
David Luna Bistuer 00:50:32 Yeah.
Marc Pichler 00:50:33 node.
David Luna Bistuer 00:50:34 After that, the next release of the fetch and XHR instrumentations already will use the SDK trace.
And we'll use, you know, we'll use the utils from the other set, so… Just the difference is that you're getting the other packets and not the SDK3 as well.
Marc Pichler 00:50:54 That would close this.
David Luna Bistuer 00:50:55 Santa Claus, yeah.
Marc Pichler 00:50:56 Yeah.
Closing as we were drop SDK trace web… Filters are moving to the web.
Just so that we know what happened here.
So dudes.
Is… There's this… issue here, where we have the Prometheus specification alignment.
Trent Mick 00:51:50 Yeah, I'm not sure if there's a lot here.
Like, I think there might be.
A chunk of work that… If we don't pick up, we might not get done in the next couple of weeks.
That said, the Prometheus order is still experimental, so I guess we could do a breaking change.
In it after, to align with spec.
Marc Pichler 00:52:11 I think the needs refinement is still accurate here. We might want to do, like, the larger breaking changes first.
And get those into 3.0.
One of them is already merged. This is this, setting the exporter host to local host by default, that we're probably… Affect most people.
Because, right now, if you set up the Prometheus Exporter, it will bind to our interfaces, and, with this, it will just bind to localhost.
Right. Which was a huge problem with… The… or, like, a huge challenge to get people to migrate, with the collector.
And I assume that it will be similar here, so… I'll go through the list here, assign myself.
And see what else we should do.
2… Make sure that the, larger braking changes are… Exodin 3 little.
This one here…
Trent Mick 00:53:40 Oh, modulo, the 699 that I have, that's related to MVAR stuff, but that's not about… living in this key trace. My understanding is nothing looks at environment variables anymore where it shouldn't, except the exporter packages.
And we talked about that last week, there was someone who had a PR for that, but it's scary and probably not the way we want to do it.
I don't know if we're fine releasing with a known issue that… When using our declarative config path, you're not supposed to look at environment variables, but we have a known limitation in looking at the exporter. Sorry, for now we'll fix it later. I don't think it has to happen in 3.0.
That's what I'm saying.
Because I don't think we're gonna get, like, a major change to the exporters in the next two weeks, is what I'm guessing.
Marc Pichler 00:54:28 Yeah, I agree. I think… This one also needs refinement here, because, that's really just now dropping SDK trace node and SDK trace base.
Which… Those are the two that still did, environment variable parsing, if I recall correctly.
And once that's done, then this issue here will also be done.
So…
Trent Mick 00:54:58 Sorry, say that again. I think I blanked out for a second there.
Marc Pichler 00:55:02 SDK trace.
node and SDK trace base.
Did… parse environment wherewares, but the new SDK trace package doesn't. So, if we get rid of these two packages, then this will automatically be done.
Trent Mick 00:55:20 Yeah.
Marc Pichler 00:55:24 Just link the SDK node one.
And I create a second issue for SDK trace base, which will probably depend on the SDK trace web remover.
Which probably also needs an issue.
And Edward and are so close.
This here, I really need to get my issues, sorted out here. There's… there's so many.
Essentially, just referring to the same thing.
Then we have… the export in SDK node, I think we discussed this already a few times.
Trent Mick 00:56:43 Yeah, I guess we agreed on that one. I'm still a little bit hesitant. I don't know if… if, like, if… just to say it again, but I'm… this is not a hill I'll die on. If a user is using the SDK node package to encode, bootstrap the SDK, or set up the SDK, That re-export is… makes it easy for them to have a dependency just on SDK node and get the same versions of things.
Or get the appropriate versions of those packages, which makes their mechanics in updating dependency versions in package.json easier.
As time goes on, especially for the… The ones that are still experimental, because keeping those up today is a pain.
So I don't know.
Marc Pichler 00:57:31 I guess with these, we can go the same route as we… planning to do with package JSON, and also remove it and add it back later if there's actually people that need it.
Trent Mick 00:57:45 Like, I mean, no one needs it, so I guess, like, the argument is just, like, add the depth if you need… on resources, if you need to set up a resource, then…
Marc Pichler 00:57:54 Mmm.
Trent Mick 00:57:54 Added dependency on that one, yeah.
Yeah, okay.
Marc Pichler 00:58:03 I have a, I feel like I… want this, so I'll assign myself.
Trent Mick 00:58:10 Excellent.
Marc Pichler 00:58:10 We'll work on that.
if, I've been looking at these re-exports for a long time now, and every time I… come across them, I want to get rid of them, so… Now's my chance. I will take it.
Here we have an old draft PR from Dan, to not use.
HR time in browser instrumentations.
I guess since most of these were moved, just… Yars or so.
Not applicable anymore.
David Luna Bistuer 00:59:03 Yeah, I heard that at comments, but Trent didn't respond, so yeah.
Marc Pichler 00:59:14 Or reach out to Jen.
David Luna Bistuer 00:59:16 Huh.
Okay.
Marc Pichler 00:59:18 Let's see if he has any… -Oh.
Additional need for this, or if we can close this.
Then we can just cross it off the 3.0 list and move on with other stuff.
to minimal support in Node.js version, we already talked about, this year… It hasn't really caused any problems in the past.
We just have this huge list of, pure dependencies for zone.js, and I was looking at these, thinking that it might be good to remove these.
Are there any objections to me just closing this as one-do? Because there's no real need for it.
I'm not hearing any, so… Close this is not planned, and… Shrink the milestone a bit.
The ad network span events… Thing, that one actually moved.
But it's still here. I think this still needs some refinement, we can still deprecate it, when it's exported from Webcommon, right? So… We could move it and then immediately deprecate it.
David Luna Bistuer 01:01:26 Yeah.
Marc Pichler 01:01:38 I'll just put a comment here, since… We're also instrumentations.
Pretty funny.
We might also want to consider… cleaning up the public API for it a bit, because I think we ended up with a bug where there's, like, add network span events, and then, like, ignore events, or something.
Silly back then. Or what's the…
Trent Mick 01:02:56 Yeah, really gross.
Marc Pichler 01:02:57 Yeah, or the performance timing thing.
Trent Mick 01:03:00 This is…
Marc Pichler 01:03:00 Hmm.
Trent Mick 01:03:02 The thing's not actually called that name, like, grep turns up nothing for that. What is this?
Function actually called?
Marc Pichler 01:03:09 I don't know what that's.
Trent Mick 01:03:10 And network events, maybe it is, actually.
Oh, there you go.
Marc Pichler 01:03:14 Yeah.
Trent Mick 01:03:15 The title's just wrong.
Dad.
So this is already in Webcommon, we're just gonna deprecate it?
David Luna Bistuer 01:03:26 It's already in Weber Command.
Marc Pichler 01:03:33 Just to let people know that this is there, but only for backwards compatibility, if they need.
That same functionality, but they really shouldn't use it that way anymore.
Trent Mick 01:03:44 So, are we… sorry, side question, are we deprecating the instrumentation fetch and instrumentation… XHR in the core repo now, or are we not yet doing that?
Jared Freeze (Palo Alto Networks) 01:03:59 I liked Mark's suggestion of doing it now.
A bit like removing the browser key. Do it now, wait for… wait for comments.
The… the biggest… the biggest change is this is not a port. I mean, David can speak to this. It's not a port. Like, it does not produce the same telemetry. I understand this point.
Trent Mick 01:04:18 So yeah, removing it.
Jared Freeze (Palo Alto Networks) 01:04:20 I think everybody knows that.
Trent Mick 01:04:21 Yeah, okay.
Jared Freeze (Palo Alto Networks) 01:04:22 But yeah, this… this shape is gone, so… Yeah.
Marc Pichler 01:04:30 Let's, create some issues, to remove it, and then, we can add it to the milestone.
Alright, I'm, just realized that we are over time already, so I don't want to keep you any longer.
Thank you, R, for joining.
Have a nice week, and see you next week.
Trent Mick 01:04:54 Extra.
David Luna Bistuer 01:04:54 Right.
Jackson Weber 01:04:56 Have it going on?
