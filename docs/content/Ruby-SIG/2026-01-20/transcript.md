SIG: Ruby SIG
Date: 2026-01-20
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/WNb9g0-Iomte4B23bgVb1FT4QrtmJ1wbtfuZ5Kd4y0koLxb9JvRqhqlxp--iVPY.uDNDl_eXGMQmmFw-
============================================================

## Zoom Recording Transcript

**Hannah Ramadan** 12:12 Hi, Daniel. Hi, Schwan.
So, I don't think we have Kayla or Arielle today, so… I'm not really sure if we're waiting for anybody else, we might go ahead and get started.
**Daniel Azuma** 12:28 Oh, okay.
Sure.
**Hannah Ramadan** 12:33 Yeah, I can go ahead and share my screen, although I don't… I didn't attend SPEC… SIG, so I'm not really sure.
What took over there? But we can take a quick look at it.
Looks like not too much was discussed today.
And Ruby's not even on this chart.
Bye.
I wonder if this is something we need to be aware of.
Okay, well, hotel resource attributes does look like something… We need to do, but we weren't included here, so… Might look into that.
**Daniel Azuma** 14:20 Yeah, not every language is there, so I probably just… Didn't include Ruby in that initial investigation.
**Hannah Ramadan** 14:29 Yeah.
I wonder if, I might take a look at this and see if I can add to the chart. Anything y'all want to talk about for this?
I think I'm good.
Let's look at the issues. Any new ones for core?
So we've got 3 new ones, Oh, Shawn, did you… it looks like this was already… Taken care of, perhaps?
Nice.
**Daniel Azuma** 15:23 No, they should be closed, Xuang.
**Xuan Cao** 15:28 No, no, actually, I was, having this to… To remind myself to improve the test case, because the test case, was not, deterministic, so… So now it was just skipped.
**Daniel Azuma** 15:45 That's… I need to…
**Xuan Cao** 15:46 Find a way to, To make sure you produce the same results for every time. Otherwise, you just keep some other, like, PR fails, which is not really good.
**Daniel Azuma** 15:59 Oh, yeah.
**Hannah Ramadan** 16:01 Nice, thank you.
Similar, looks like Kayla had this one, but… skipping for now. Not merged.
And then a new feature request.
**Daniel Azuma** 16:38 Hmm.
**Hannah Ramadan** 16:55 I think maybe… I think Ariel had these open last week, I don't know what they're failing on, probably the same thing, given…
**Daniel Azuma** 17:02 Yeah, I've got this… That's… Seems… That might be something different. There… I know a bunch of things were failing on… oh, no, this was the Ruby 4, so this is probably the… what was it, the O structure, or something was failing across…
**Hannah Ramadan** 17:23 Yeah, I was struck.
**Daniel Azuma** 17:24 Or… So I think… Some… wasn't someone else working on…
**Xuan Cao** 17:35 Yeah, this, this removes CGI and the Astra dependency from V4, the one I have, So, basically, just, bump to the rig to from 12 to 13, and then… because rig, rig fell using the open straps, but 13 doesn't even use anymore.
And this, this one is, different, it's about the, encoding, because the CGI is removed, And, I'm thinking to using the URL coding, which has a similar, spec.
yep.
**Daniel Azuma** 18:16 I saw you were, you were working with Ariel, kind of back and forth on the, on, on these. How are things right now? Do you…
**Xuan Cao** 18:26 Maybe you just needed him, need his another, review, and then if… if he's okay with this, and then we can, like… well, basically just update the other rig dependency, and then… Remove some of the test cases that use the OpenStar as well.
Yeah, I can pee him, too.
Ask for an outlook.
**Daniel Azuma** 18:55 Okay, Do you need anyone else's eyes on this, or are you and Arielle… do you and Arielle have it already?
**Xuan Cao** 19:07 I mean, I, I don't, welcome to, approve numbers, but I, I, I, I will… Top swimming, for sure.
**Daniel Azuma** 19:16 Okay.
**Xuan Cao** 19:24 Oh, oh, and one thing, for the… for the… to replace the CGI with the URL to encoding, this is, as… since Ariel, as mentioned, is kind of a, Big change on it.
Yeah, maybe more eyes on this would be helpful, but, basically, I look at a different language, how they're encoding their, their headers, I think… the URL encoding one is safe, but I'm not an expert on this encoding… decoding stuff, so…
**Daniel Azuma** 20:00 Okay, I see. There's a… there's a small, just a small functionality change there, because they… they, they…
**Xuan Cao** 20:07 Yeah. Behaved differently for asterisk, okay, yeah.
**Hannah Ramadan** 20:10 Look at that.
**Daniel Azuma** 20:18 Okay.
**Hannah Ramadan** 20:36 Oh, I don't think anything else is new, these are on graph.
I'm looking at Contriv… Looks like we got a logger bug.
Everyone's…
**Daniel Azuma** 20:56 Yeah, here's… Kristen did have a… PR for this.
**Hannah Ramadan** 21:09 I like when folks open issues and just make PRs to fix them.
**Daniel Azuma** 21:14 Yeah.
Yeah, I'm thinking it was look… I sh… I should look at this.
Yeah, at first glance, I was a little bit… concerned about this one, so I need to… I need to look at this one more closely.
Berret.
They're doing… they're… yeah, they're doing something different here with the… with… with the threading, so… I think To require some… Careful.
betting.
**Hannah Ramadan** 22:04 Yeah, they even say it may not be entirely clear, but it helps prevent deadlocks.
Interesting.
Okay.
Nice.
**Daniel Azuma** 22:33 So some… something that's, been, going on here, So… who's this? James Thompson, has been doing a bunch of… Updates for renovate, and, Word.
Kind of making sure that we're… renovates working, and those changes are tested, and so forth. There's a particular, so if you can open 1952, That's, I think, kind of… this is… this is a… this is one that we've been… he and I have been having a discussion on.
So, what… What's going on is, There are cases where Renovate, will make a change, and that change will break.
So one of the, one of the, the example that, that just happened this past week, Renovate went through, all of our GitHub Actions repo, workflows and updated Ruby from 4.0 to 4.01.
**Hannah Ramadan** 23:50 The problem is that the setup Ruby.
**Daniel Azuma** 23:54 action was still pinned on a version that did not support Ruby 401, and so all of the workflows that were affected, stopped working. And that wasn't caught in CI, because we don't have any CI that actually ex… that exercises these workflows when we modify the YAML for those workflows.
So what James was trying to do here is, pss.
modify these workflows so that they run not just when they would normally run. These in particular are part of the release process, so they're run as part of the release process, and some of them are run manually, some of them are run when pull requests close, or, you know, there are different kinds of triggers that trigger these at different parts of the release process.
What he's doing, if you go to Files Changed, He's… in addition to when they would normally run, he's modified these to run also, during, kind of, during a normal CI process, so when the pull request is open and when the files are changed.
So there's a bunch of new, logic in here to, number one.
run these, these workflows, during CI, in addition to when they would normally run. And two, because these are part of the release process, you, you don't want releases to happen during CI. So… or normally, really, if they, if they would… if you run them during CI, they would… they would generally fail, because you don't have a release that's configured at, during that time, and whatever, so… So he… so he's also hacked each one to… To try to detect whether this is being run as part of CI or as part of a normal release process, and disable parts of the workflow, if it's just CI.
So… So he's kind of done these two things to these workflows in order so that we can run at least part of them during CI to check whether or not those installations of Ruby and other installations that each one of them is doing is going to succeed or not.
So, he's doing this with this one, and there is also another pull request, 1955, where he does that with the same kind of thing with another of these GitHub Actions workflows.
Now, I've had a… I've kind of been working with them to… on these… on this pull request. I've… I think we have it to the point where it's working.
But you saw the… you saw the changes there. They're kind of… I think they're kind of… I don't like them. They're… they're necessarily ugly, and seem somewhat precarious. So, I'm… I'm… I think they'll work, but I'm really hesitant about them, and so I was hoping that other people might have opinions about these. I did come up with an alternative, which is that one that you're clicking on there.
This… this alternative, the way this works is it just creates a new workflow, that does the same installations as all the other workflows, but just runs as at CI. So you don't modify any of the existing workflows, you create a new workflow that, that just runs during CI, that does the same does the same… attempts to do the same installations and so forth, and so the hope is that if Renovate goes through and updates something, it'll update all these workflows, including this one, at the same time.
this one will run during CI, and if it fails, that'll be kind of a canary to indicate that, although the other ones probably would fail as well.
So, this is another… and there are some pros and cons to this approach versus what James has said, which I kind of, I wrote out here.
So… Yeah, I'm looking for any other opinions, from, from people about, about these two approaches to this problem.
**Hannah Ramadan** 29:02 Yeah, I'll… I'll read about this more. This… this Canary one seems more simple. I like the idea of just not having to change all the other files and having one kind of, like, test go.
Did… the user… what's his name, Thomas, like, have any commer… like, did you guys talk about this, or…
**Daniel Azuma** 29:21 No, I just… I just opened this, an hour.
**Hannah Ramadan** 29:25 There we go, who docks.
**Daniel Azuma** 29:26 I don't… I think, yeah, I think James is… I think they're in Australia, so they're probably… it's nighttime right now.
But, yeah, hopefully… I'm hopeful that's, Yeah, we can have a discussion about this as well. I did mention this… this technique to James, in, in the discussion on the other, on the other… on his PR. I think he still prefers his approach, and again, there are pros and cons.
But I don't know, now that I've actually opened the one, we can actually have a… direct conversation about, so, what they actually look like. So, yeah, we'll… maybe we'll see what he says.
But yeah, if anyone else has opinions, Please let us know.
1959 is the other one.
**Hannah Ramadan** 30:48 Yeah.
Amazing.
Is Thomas a, like, SIG member, or he's, just a community member?
**Daniel Azuma** 31:13 I… I don't know. He's been pretty active the past… couple weeks, but I only rejoined the group,
**Hannah Ramadan** 31:21 Yeah, right.
**Daniel Azuma** 31:22 two weeks, and so, yeah, I don't…
**Hannah Ramadan** 31:24 I don't know. Nice, I wasn't sure if he was, like, a past contributor, but yeah, okay, cool.
Don't know much about this, but… Seems reasonable-ish. I'll have to look at it.
Did either of you have anything you wanted to discuss with the PRs for Contrib?
**Daniel Azuma** 33:10 I don't think I have anything else… .
**Xuan Cao** 33:21 That's it from me.
**Daniel Azuma** 33:23 Yeah, there's… yeah, there's a bunch more, going on that probably should be looked at, at least, so, that… that's, I think… on me and on maybe all of us to kind of get… I… I feel like I need to get more reacquainted with the codebase here, so I can contribute more meaningfully with reviews.
**Hannah Ramadan** 33:53 Amy, I feel like I'm always struggling for… just to find time.
Yeah. I do have one PR that I… that I'd love to… to talk about.
**Daniel Azuma** 34:03 Perhaps we can talk more about it next week with Caitlin Arielle.
**Hannah Ramadan** 34:07 This is a feature to add a query summary attribute to database spans. Under the new semantic conventions, the query summary is meant to be the new span name.
And so this is a… an attempt to tokenize, parse, and, create the query summary attribute slash name. I'm a little bit hesitant about… introducing this as a on by default, because of the potential overhead. I think, it could be quite heavy to… To do parsing for… Every database query, a cache would make it faster, but I… I'm not sure if this is something we want to introduce overall. And it is a kind of a heavy PR, has a lot of logic, especially in the parser.
Section?
I can go over this a little bit more detailed, but I think this might just be one that we can maybe take a look at and review, maybe, like, slowly. I… the… The cache and the tokenizer files are much more straightforward and less complex than the parser.
So that would probably be an ideal place to start, This is also an AI project, so the… the tokenizer and cache are simple, that was, like, easy to do for me, and then the parser was generated with AI, so that's another, like.
Different things about this.
Yeah, we're being definitely encouraged at work to use AI more, and so, this was a project I figured I could, do.
get the AI piece under my belt for work work, and then do something here with this. So, personally, like, this… this is… I'm still, like… trying to follow the logic for every single case. And it's heavy stuff, like… There are a lot of chess cases and a lot of, like, different conditionals and branches that… Like, this could take, yeah, I only saw the .NET team do an implementation of this, that was similar, and they are using it in production and generating database summaries, but I'm not confident this is something we really want to introduce by default, but I think it is a good option to provide people and kind of see how it plays out.
There are other, for getting a… the span name, because it's… the intent of this originally was to follow semantic conventions and get this span name.
But there are other fallback options that might not be as intensive as the query summary, so I might try to… Create a default fallback, and this could be something on or off that people can decide what they want to do with.
**Daniel Azuma** 37:16 Yeah, I think… I think just, you know, without having looked at this at all in any detail, at, you know, at the very least, having some, you know, way to opt in or opt out, seems, seems like a kind of a minimum, approach to Reducing risk for having a lot of heavyweight parsing and things going on.
Okay.
Just as a… Just as a note, the feet, should be… should all be lowercase, for conventional commits.
So in, particularly in the,
**Xuan Cao** 38:18 Shit, oh my god.
**Daniel Azuma** 38:19 As… in the commit message itself. So I… I guess when we do this, we'll, we'll, we'll squash, probably, so it won't…
**Hannah Ramadan** 38:28 Oh, that's probably why I passed. I was wondering why the conventional… I know we have a… A test for that, so I guess I was right there.
But yes, way too many commits, I wouldn't want to commit all of these.
Cool, yeah. Okay.
**Xuan Cao** 38:49 Beautiful.
**Daniel Azuma** 38:51 I… yeah, I think… Maybe, yeah, maybe we can start looking at this offline.
**Hannah Ramadan** 38:58 Yeah, it's… I think this is a… because it's so big, probably, and offline, but I tried to… make it easier to review. The parser has a README That I added to kind of, like, explain everything in English, because it is so… there's so much crossover with things, but… And I think I happened to read me…
**Xuan Cao** 39:27 She's not…
**Hannah Ramadan** 39:28 For a query summary as well, that goes through everything.
Cool, other than that… Do you guys have anything else you want to go over, or any PRs people are looking for reviews on? I know Kayla put in the Slack channel that if you have anything you wanted her eyes on, we could go ahead and share, I believe, just directly in her… in the Slack channel.
I don't have anything else.
**Daniel Azuma** 40:25 So…
**Hannah Ramadan** 40:29 Nice, I think then we can go ahead and call. I hope everyone had a nice weekend, and good rest of your week.
**Daniel Azuma** 40:38 Thanks for leading us, Hannah.
**Hannah Ramadan** 40:39 Yeah, see you guys later. Bye.
**Daniel Azuma** 40:42 Right?
