SIG: Collector SIG
Date: 2025-08-20
Duration: 10 minutes
Zoom Recording URL: https://zoom.us/rec/share/wiTqdHwoErcLA3nXSihTnQYBmMsmRTKw2rrcqHSXcNRiMSZkNrV7Q2SMClVT7EOP.SgOJUh0zdnATu1HX
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 02:29 Hi, everyone. If you have any topics, please add them to the agenda in the document that I'll link in the chat.
And the first one is Stephani. Stefani, do you want to start?
**TH Tiffany Hrabusa** 02:41 Sure.
So, I'm here on a bit of a fact-finding mission from the communications SIG.
We have a bit of automation that updates versions across the website and the registry.
And one of those workflows updates, collector versions.
And there's been a slight increase in the number of patch releases over the last month or so, and every bot update for a patch release has failed, building, because we have a link checker, and …
I guess some parts of the collector are not included in all patch releases, or I should say, not all
parts of the collector are included in all patch releases, and so it's breaking things on the website, basically, and so we haven't been able to actually update collector versions to the patch release number.
… Or… I guess the last two… … minor versions. Anyway.
what I'm here to figure out is, whether we on the doc side need to change our automation and make it a little bit more nuanced, or if there… if it would be…
a lighter lift to just include all parts of the collector in every patch release. And I really don't know the answer to that, so I just wanted to…
Find out.
**Andrzej Stencel** 04:11 Yeah, so first, if you could definitely add a link to… is there an issue about this already? I think I saw something before. If you could add it to the agenda doc, it could make it easier for other folks.
**TH Tiffany Hrabusa** 04:24 Sure, I can add a sample of the, ….
**Andrzej Stencel** 04:28 Is there an issue you created in the collector repository, or in the Docs repository, or somewhere else?
**TH Tiffany Hrabusa** 04:33 Yeah, there is.
**Andrzej Stencel** 04:35 Okay, and the other thing… thought I had was, I think we should be…
releasing every artifact with every patch release, and if we don't, that's probably a mishap in the release pipeline. And we've seen that in the recent patch releases, that not all assets were published, and then we tried to fix that.
I hope that the latest release has all the assets here, Pablo?
**Pablo Baeyens** 05:07 Yeah, I mean, I think what Andre is saying is…
Right? There are some nuances, and I'm wondering what links are the ones that are failing.
This second….
**TH Tiffany Hrabusa** 05:25 So, the first time, I think it was because the builder and supervisor were not included. There's been 4 patch releases for the last minor release.
And, on the first…
patch release, it was the builder and the supervisor, and then, I think it was the reverse, only the builder was included in one. I'm not really sure, maybe Jade has more information, because.
**Jade Guiton** 05:54 Yeah, so… what I want to clarify is that
a lot of these patch releases were not actually patches at all, they were just reruns of the release process, because we've had issues with the release process, with Docker integration and all that, and we currently don't have
A better way of rerunning the release process, … besides setting a new patch release number.
And…
So yeah, that's why some of the artifacts aren't included. And the second thing, the second nuance, is that…
… The version numbers… On the Collector Releases repo.
which correspond, usually, to the, version numbers on Docker and all that.
They don't necessarily match the releases on the Core Collector repo, And the collector contribu.
We can have a patch release in one repo, but not in another one.
And so, I think it's likely that the current documentation automation
Makes this assumption that, they're all in sync, all the time.
Which is not really the case. We can have… what we've had in the past releases is essentially, new versions on the collector releases repo, because the release process was failing.
But without a corresponding code change,
in, the core and contrib repos.
And vice versa, there's also have been cases in the past, I think, where we've had patch releases in the core repo.
That, you know, usually leads also to a patch release in the releases repo, but not on contribib, for example. So they kind of need to be… either we need to figure out a way to keep them in sync, which is complicated.
Or would we need to be able to make sure that they are treated distinctly, and updated distinctly, if that makes sense.
in the docs automation, which might also be not that simple, but….
**TH Tiffany Hrabusa** 08:10 Yeah, okay. I think that that answers my question. So, the changes will need to be on the docs side.
I will work with our infrastructure experts to figure out exactly what…
we can do, and then I may need to come back here or, work with someone specifically to figure out,
which parts need to be updated with rich release. I'll try to figure that out on my own, but once I get some information from the infrastructure experts, I'll circle back. Thanks very much for the information.
**Jade Guiton** 08:48 Yeah, it's likely we'll need to make some changes on our end as well, first to…
Try to fix the releases process, and hopefully not make as many patch versions when it fails.
And also maybe communicate better about which versions on one repo correspond to which others, and which ones contain which artifacts it's been…
a struggle. Lots of different issues, but …
Yeah, I think there's definitely gonna be work on our end as well.
**TH Tiffany Hrabusa** 09:18 Thank you.
**Andrzej Stencel** 09:33 There's nothing else on the agenda.
So if nobody has anything else, we can wrap this up, right?
**Jade Guiton** 10:02 I think so.
**Andrzej Stencel** 10:05 Thanks, everyone.
Have a good day.
**Jade Guiton** 10:09 Thank you, everyone.
